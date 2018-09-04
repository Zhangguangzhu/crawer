 #! /usr/bin/env python3.5

import urllib.request,urllib.parse

url = "http://www.iqianyue.com/mypost/"
postdata = urllib.parse.urlencode({"name":"zz", "pass":"dd"}).encode('utf-8')
print(postdata)
req = urllib.request.Request(url, postdata)
req.add_header("User-Agent", "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:54.0) Gecko/20100101 Firefox/54.0")
data = urllib.request.urlopen(req).read()
print(data)
