# Steam data research

I develope it for my galgame sale research.

## `steamspu.py`

```python
from steamspy import Scraper

appid = '315810' # a steam game id, it also used in steamspy

scraper = Scraper()
scraper.login() # you need a file named 'config.json' in directory to set username and password in steamspy
data1 = scraper.get_geography()
data2 = scraper.get_general()

# In REPL

>>> data1
[{'color': '#1f77b4',
  'key': 'Owners',
  'values': [{'label': 'United States', 'url': '/country/US', 'value': 24.7},
   {'label': 'China', 'url': '/country/CN', 'value': 18.15},
   {'label': 'United Kingdom', 'url': '/country/GB', 'value': 6.55},
   {'label': 'Canada', 'url': '/country/CA', 'value': 6.25},
   {'label': 'Japan', 'url': '/country/JP', 'value': 6.25},
   {'label': 'Germany', 'url': '/country/DE', 'value': 5.95},
   {'label': 'Korea', 'url': '/country/KR', 'value': 3.27},
   {'label': 'Russia', 'url': '/country/RU', 'value': 2.98},
   {'label': 'Australia', 'url': '/country/AU', 'value': 2.38},
   {'label': 'Thailand', 'url': '/country/TH', 'value': 1.49},
   {'label': 'Singapore', 'url': '/country/SG', 'value': 1.49},
   {'label': 'Austria', 'url': '/country/AT', 'value': 1.49},
   {'label': 'Poland', 'url': '/country/PL', 'value': 1.19},
   {'label': 'Italy', 'url': '/country/IT', 'value': 1.19},
   {'label': 'France', 'url': '/country/FR', 'value': 1.19},
   {'label': 'Hong Kong', 'url': '/country/HK', 'value': 0.89},
   {'label': 'Hungary', 'url': '/country/HU', 'value': 0.89},
   {'label': 'Sweden', 'url': '/country/SE', 'value': 0.89},
   {'label': 'Taiwan', 'url': '/country/TW', 'value': 0.89},
   {'label': 'Switzerland', 'url': '/country/CH', 'value': 0.6},
   {'label': 'Belgium', 'url': '/country/BE', 'value': 0.6},
   {'label': 'Finland', 'url': '/country/FI', 'value': 0.6},
   {'label': 'Mexico', 'url': '/country/MX', 'value': 0.6},
   {'label': 'Brazil', 'url': '/country/BR', 'value': 0.6},
   {'label': 'Malaysia', 'url': '/country/MY', 'value': 0.6},
   {'label': 'Czech Republic', 'url': '/country/CZ', 'value': 0.6},
   {'label': 'Indonesia', 'url': '/country/ID', 'value': 0.6},
   {'label': 'Israel', 'url': '/country/IL', 'value': 0.3},
   {'label': 'Slovakia', 'url': '/country/SK', 'value': 0.3},
   {'label': 'Greece', 'url': '/country/GR', 'value': 0.3},
   {'label': 'Other', 'url': '/country/', 'value': 6.25}]},
 {'color': '#d62728',
  'key': 'Players',
  'values': [{'label': 'United States', 'url': '/country/US', 'value': 16.67},
   {'label': 'China', 'url': '/country/CN', 'value': 16.67},
   {'label': 'United Kingdom', 'url': '/country/GB', 'value': 0},
   {'label': 'Canada', 'url': '/country/CA', 'value': 0},
   {'label': 'Japan', 'url': '/country/JP', 'value': 0},
   {'label': 'Germany', 'url': '/country/DE', 'value': 0},
   {'label': 'Korea', 'url': '/country/KR', 'value': 33.33},
   {'label': 'Russia', 'url': '/country/RU', 'value': 0},
   {'label': 'Australia', 'url': '/country/AU', 'value': 0},
   {'label': 'Thailand', 'url': '/country/TH', 'value': 0},
   {'label': 'Singapore', 'url': '/country/SG', 'value': 0},
   {'label': 'Austria', 'url': '/country/AT', 'value': 0},
   {'label': 'Poland', 'url': '/country/PL', 'value': 0},
   {'label': 'Italy', 'url': '/country/IT', 'value': 0},
   {'label': 'France', 'url': '/country/FR', 'value': 0},
   {'label': 'Hong Kong', 'url': '/country/HK', 'value': 0},
   {'label': 'Hungary', 'url': '/country/HU', 'value': 16.67},
   {'label': 'Sweden', 'url': '/country/SE', 'value': 0},
   {'label': 'Taiwan', 'url': '/country/TW', 'value': 16.67},
   {'label': 'Switzerland', 'url': '/country/CH', 'value': 0},
   {'label': 'Belgium', 'url': '/country/BE', 'value': 0},
   {'label': 'Finland', 'url': '/country/FI', 'value': 0},
   {'label': 'Mexico', 'url': '/country/MX', 'value': 0},
   {'label': 'Brazil', 'url': '/country/BR', 'value': 0},
   {'label': 'Malaysia', 'url': '/country/MY', 'value': 0},
   {'label': 'Czech Republic', 'url': '/country/CZ', 'value': 0},
   {'label': 'Indonesia', 'url': '/country/ID', 'value': 0},
   {'label': 'Israel', 'url': '/country/IL', 'value': 0},
   {'label': 'Slovakia', 'url': '/country/SK', 'value': 0},
   {'label': 'Greece', 'url': '/country/GR', 'value': 0},
   {'label': 'Other', 'url': '/country/', 'value': 0}]}]
   
>>> data2

{'Category': ['Single-player', 'Steam Trading Cards', 'Steam Cloud'],
 'Developer': ['minori'],
 'Genre': ['Adventure'],
 'Languages': ['English'],
 'Owners': 63027,
 'Owners_std': 6491,
 'Peak concurrent players yesterday': 11,
 'Players in the last 2 weeks': 875,
 'Players in the last 2 weeks_std': 765,
 'Players total': 35015,
 'Players total_std': 4838,
 'Playtime in the last 2 weeks': datetime.timedelta(0, 171),
 'Playtime in the last 2 weeks_median': datetime.timedelta(0, 235),
 'Price': 19.99,
 'Publisher': ['MangaGamer'],
 'Release date': datetime.datetime(2015, 1, 30, 0, 0),
 'Score rank': 0.96,
 'Tags': ['Anime',
  'Visual Novel',
  'Adventure',
  'Story Rich',
  'Singleplayer',
  'Romance',
  'Cute',
  'Great Soundtrack',
  'Nudity'],
 'Userscore': 0.96,
 'YouTube stats': '69,344\xa0views and 1,739\xa0comments for videos uploaded last week, 40\xa0new videos uploaded yesterday.'}
```