# -*- coding: utf-8 -*-

import urllib.request,re

url = 'https://list.jd.com/list.html?cat=670,677,679&page=1'
htmldoc = urllib.request.urlopen(url).read()
print(type(htmldoc))
html_pat1 = '<div id="plist" class="goods-list-v2 J-goods-list gl-type-1 ">.+?<div class="page clearfix">'
res1 = re.compile(html_pat1).findall(str(htmldoc))
html_pat2 = '<img width="220" height="220" data-img="1" data-lazy-img="//(.+?jpg)">'
res2 = re.compile(html_pat2).findall(res1[0])
print(res2)
x = 0
for picurl in res2:
	try:
		picurl = "http://" + picurl
		picname = "./"+str(x)+".jpg"
		urllib.request.urlretrieve(picurl,filename=picname)
	except urllib.error.URLError as e:
		if hasattr(e, "code"):
			print(e.code)
		print(e.reason)
	finally:
		x += 1