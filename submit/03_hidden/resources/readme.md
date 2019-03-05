# http://192.168.99.100/.hidden/

`/robots.txt` contains another entry: `.hidden/`

the `.hidden/` folder contains lots of subfolders and each one of those has its own subfolders, and there is several levels of that;

at bottom of the directory tree there is a README file,

most of the README's contain the same text,

if someone wanted to check all the files that would be problematic because of the multitude of folders and subfolders

i wrote a little script to traverse the directory tree and extract the unique strings of text contained in README files

```
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
```


here is the output of the script
```
e1z2r8p32% ./hidden.py
scanning item #1
	Demande Ã  ton voisin de gauche  
 http://192.168.99.100/.hidden/amcbevgondgcrloowluziypjdh/acbnunauucfplzmaglkvqgswwn/ayuprpftypqspruffmkuucjccv/README
scanning item #2
	Non ce n'est toujours pas bon ...
 http://192.168.99.100/.hidden/amcbevgondgcrloowluziypjdh/acbnunauucfplzmaglkvqgswwn/becskiwlclcuqxshqmxhicouoj/README
scanning item #3
	Demande Ã  ton voisin du dessous 
 http://192.168.99.100/.hidden/amcbevgondgcrloowluziypjdh/acbnunauucfplzmaglkvqgswwn/cqqssunxyhjgdwjoafgyzoollx/README
scanning item #4
	Demande Ã  ton voisin du dessus  
 http://192.168.99.100/.hidden/amcbevgondgcrloowluziypjdh/acbnunauucfplzmaglkvqgswwn/dupoqdxhvrbqhaqokxsiigjnph/README
scanning item #6
	Toujours pas tu vas craquer non ?
 http://192.168.99.100/.hidden/amcbevgondgcrloowluziypjdh/acbnunauucfplzmaglkvqgswwn/ftzcgojutitjfpqrdadyfewfov/README
scanning item #12
	Demande Ã  ton voisin de droite  
 http://192.168.99.100/.hidden/amcbevgondgcrloowluziypjdh/acbnunauucfplzmaglkvqgswwn/lmpanswobhwcozdqixbowvbrhw/README
scanning item #13
	Tu veux de l'aide ? Moi aussi !  
 http://192.168.99.100/.hidden/amcbevgondgcrloowluziypjdh/acbnunauucfplzmaglkvqgswwn/mfmtemmsbpftlvuuuwitbydbbt/README
scanning item #15694
	99dde1d35d1fdd283924d84e6d9f1d820
 http://192.168.99.100/.hidden/whtccjokayshttvxycsvykxcfm/igeemtxnvexvxezqwntmzjltkt/lmpanswobhwcozdqixbowvbrhw/README
scanning item #18279
```

wow, all together 18279 readme files

this file `http://192.168.99.100/.hidden/whtccjokayshttvxycsvykxcfm/igeemtxnvexvxezqwntmzjltkt/lmpanswobhwcozdqixbowvbrhw/README`
contains a string that looks like a hash `99dde1d35d1fdd283924d84e6d9f1d820` and possibly .. a flag?

i am a little disappointed, because it doesn't explicitly say _"Hey, here is your flag"_ like before, and also the length seems odd,
this string is 33 characters long but all previous flags were 64 characters long


i am happy with the script and i think it would be cool to get a list of common folder and file names and then use a similar script to scan the web server root `http://192.168.99.100/`  ... who knows what i might discover

