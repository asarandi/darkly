#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

base='http://192.168.99.100/?page=feedback'

for i in range(256):
    req = requests.post(base, data = {
	    'txtName':'',
	    'mtxtMessage': chr(i),
	    'btnSign': 'Sign Guestbook'
	    })
    soup = BeautifulSoup(req.text, 'html.parser')
    subj = soup.find('form').find_next_sibling()
    if subj.name != 'table':
        print("%03d %02x %c" % (i, i, chr(i)))
