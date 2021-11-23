from bs4 import BeautifulSoup
import requests
import lxml

html_text = requests.get('http://www.columbiarecords.com/artists/').text
soup = BeautifulSoup(html_text, 'lxml')
artist_name_21 = soup.find_all('h2')
print(artist_name_21)

import pandas as pd
import numpy as np
for name in artist_name_21:
    print(name)

import seaborn as sns