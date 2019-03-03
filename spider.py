#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

base = 'http://10.114.100.30/index.php?page=upload'
base = 'http://10.114.100.30/index.php?page=searchimg'

req = requests.get(base)
with open('index.html', 'w') as fp:
    fp.write(req.text)
    fp.close()

soup = BeautifulSoup(req.text, 'html.parser')
for e in soup.find_all():
    if e.has_attr('src'):
        print('src', e['src'])
    if e.has_attr('href'):
        print('href', e['href'])

