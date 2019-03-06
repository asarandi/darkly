#!/usr/bin/env python3

import requests

#base = 'http://192.168.99.100/'
base = 'http://192.168.99.100/index.php?page='

wl = None
with open('wordlist.txt') as fp:
    wl = fp.read().splitlines()
    fp.close()

visited = set()

for w in wl:
    r = requests.get(base + w)
    if r.status_code == 404:
        continue
    h = hash(r.text)
    if h not in visited:
        visited.add(h)
        print(base + w, '\t\t', r.status_code)
