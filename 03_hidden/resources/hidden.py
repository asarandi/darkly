#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

base = 'http://192.168.99.100/.hidden/'

uniq = set()
count = 0

def folder_scan(url):
    global uniq, count
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'html.parser')
    for a in soup.find_all('a', href=True):
        link = a['href']
        if link[:2] == '..':
            continue
        elif link[-1] == '/':
            folder_scan(url + link)
        else:
            count += 1
            print('\rscanning item #%d' %  (count,), end='')
            req2 = requests.get(url + link)
            if req2.text not in uniq:
                uniq.add(req2.text)
                print('\n\t' + req2.text, url + link)

if __name__ == '__main__':
    folder_scan(base)
