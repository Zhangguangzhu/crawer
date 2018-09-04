# -*- coding: utf-8 -*-

import urllib.request

url = "http://www.baidu.com/s?wd="
key = "一"
key_code = urllib.request.quote(key)
url_all = url + key_code
print(url_all)
req = urllib.request.Request(url_all)
data = urllib.request.urlopen(req).read()
fh = open("search.html", 'wb')
fh.write(data)
fh.close()