# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 18:30:55 2016

@author: yiyuezhuo
"""

import requests
import webbrowser
import json
import datetime
from bs4 import BeautifulSoup
import re

def fff(content, temp_name = 'temp.html'):
    if type(content) == bytes:
        content = str(content)
    elif type(content) == requests.models.Response:
        content = str(content.content)
    with open(temp_name, 'w')as f:
        f.write(content)
    webbrowser.open(temp_name)
        
def get_user_info(config_path = 'config.json'):
    with open(config_path) as f:
        config = json.load(f)
    return config
    
def get_date(delta_days):
    date = datetime.date.today() - datetime.timedelta(days = delta_days)
    return datetime.datetime.strftime(date,'%Y-%m-%d')

data_url = 'http://steamspy.com/ajax/slowdata.php'
login_url = 'http://steamspy.com/login/'
root_url = 'http://steamspy.com/app/'

def need_login(method):
    def _method(self, *args, **kwargs):
        if self.logined == False:
            self.login()
        return method(self, *args, **kwargs)
    return _method

class Scraper(object):
    def __init__(self, info = None):
        self.session = requests.session()
        if info == None:
            self.info = get_user_info()
        else:
            self.info = info
        self.logined = False
    
    def login(self):
        self.session.get(login_url)
        form =self.info.copy()
        form.update({'keeplogged' : 1,
                     'submit'     : '',
                     'doLogin'    : 1})
        self.logined = True
        return self.session.post(login_url, data = form)
    
    @need_login
    def get_geography(self, appid):
        form = { 'request'    : 'App Geography',
                 'appid'      : appid,
                 'YesterdayD' : get_date(1),
                 'FreeDateD'  : get_date(91)}
        res = self.session.post(data_url, data = form)
        rd = json.loads(res.content.decode('utf8'))
        assert rd['result'] == 'Success'
        data = json.loads(rd['html'][rd['html'].index('['):rd['html'].rindex(']')+1])
        return data
    
    def get_general(self, appid):
        url = root_url + appid
        html = self.session.get(url).content
        return enhance_general(parse_general(html))
        
class list_map_escape:
    pass
        
def list_map(term_map):
    # 还是另请高明吧
    def _func(tree, *args, **kwargs):
        rl = []
        for node in tree:
            if type(node) == list:
                rl.append(_func(node, *args, **kwargs))
            else:
                r = term_map(node, *args, **kwargs)
                if r != list_map_escape:
                    rl.append(r)
        return rl
    return _func
    
@list_map
def to_text(node):
    if hasattr(node,'text'):
        s = node.text
    else:
        s = node.__str__()
    if s.strip() == '':
        return list_map_escape
    else:
        return s

def test():
    scraper = Scraper()
    scraper.login()
    print(scraper.get_geography())
    
if __name__ == '__main__':
    '''
    scraper = Scraper()
    scraper.login()
    data = scraper.get_geography('315810')
    '''

''' test record
session = requests.session()
res1 = session.get(login_url)
form1 = get_user_info() # get username and password by json file config.json
form1.update({'keeplogged' : 1,
             'submit'     : '',
             'doLogin'    : 1})
res2 = session.post(login_url, data = form1)
form2 = {'request'    : 'App Geography',
         'appid'      : '315810',
         'YesterdayD' : '2016-08-01',
         'FreeDateD'  : '2016-05-03'}
res3 = session.post(data_url, data = form2)
rd = json.loads(res3.content.decode('utf8'))
assert rd['result'] == 'Success'
rd2 = json.loads(rd['html'][rd['html'].index('['):rd['html'].rindex(']')+1])
'''

def parse_general(html):
    soup = BeautifulSoup(html, 'lxml')
    el = list(soup.find(attrs = {'class' : 'p-r-30'}))[2]
    dic = {}
    cut = []
    for child in el.children:
        if child.name == 'strong':
            dic[cut[0].text] = to_text(cut[1:])
            cut = [child]
        else:
            cut.append(child)
    
    rd = {}
    # remove vervose key char :
    for key in dic.keys():
        if len(key)>0:
            value = dic[key]
            if key[-1] == ':':
                rd[key[:-1]] = value
            else:
                rd[key] = value
    # reduction list 
    one_term_list = ['Owners',
                     'Peak concurrent players yesterday',
                     'Players in the last 2 weeks',
                     'Players total',
                     'Playtime in the last 2 weeks',
                     'Price',
                     'Release date',
                     'Score rank',
                     'Userscore',
                     'YouTube stats']
    for key in one_term_list:
        value = rd[key][0]
        if value[0] == ':':
            value = value[1:]
        rd[key] = value.strip()
    
    # special process
    rd['Tags'] = [value for i,value in enumerate(rd['Tags']) if i%2==0]
    rd['Category'] = [cat.strip() for cat in rd['Category'][0].split(',')]
    return rd
    
def enhance_general(string_dic, time_process = True):
    
    rd = string_dic.copy()
    
    for key in ['Owners',
                'Players in the last 2 weeks',
                'Players total']:
        value = string_dic[key]
        index = value.find('(')
        if index != -1:
            value = value[:index]
        # default is mean/average
        rd[key],rd[key + '_std'] = value.replace(',', '').split('±')
        rd[key],rd[key + '_std'] = int(rd[key]),int(rd[key + '_std'])
    
    for key in ['Score rank','Userscore']:
        value = float(string_dic[key][:-1])/100
        rd[key] = value
    rd['Price'] = float(string_dic['Price'][1:]) # remove $ char
    rd['Peak concurrent players yesterday'] = int(rd['Peak concurrent players yesterday'])
    
    if time_process:
        rd['Release date'] = datetime.datetime.strptime(string_dic['Release date'],'%b %d, %Y')
        
        average, median = re.match(r'(.+)\(average\)(.+)\(median\)',string_dic['Playtime in the last 2 weeks']).groups()
        average_m,average_s = average.strip().split(':')
        median_m,median_s = median.strip().split(':')
        rd['Playtime in the last 2 weeks'] = datetime.timedelta(seconds = int(average_m) * 60 + int(average_s))
        rd['Playtime in the last 2 weeks_median'] = datetime.timedelta(seconds = int(median_m) * 60 + int(median_s))
    
    return rd
