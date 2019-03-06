# http://192.168.99.100/index.php?page=redirect&site=instagram

at the bottom of the page there are some links to external social media websites

the urls have two parameters: **page** and **site** ... changing the **site** parameter to something else other than predefined words ("_facebook_", "_twitter_", "_instagram_") will yield the flag:

for example given the url `http://192.168.99.100/index.php?page=redirect&site=instagram1`

the page produces the flag:
```
GOOD JOB HERE IS THE FLAG : B9E775A0291FED784A2D9680FCFAD7EDD6B8CDF87648DA647AAF4BBA288BCAB3
```
