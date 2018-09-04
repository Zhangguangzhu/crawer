# -*- coding: utf-8 -*-

import urllib.request, re,sys

url = 'https://www.qiushibaike.com'
header = ("User-Agent", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36")
opener = urllib.request.build_opener()
opener.addheaders = [header]
urllib.request.install_opener(opener)
# pattern = '<div class=\"author clearfix\">.*?<h2>(\S+)</h2>.*?<div class=\"content\">(\S+)</div>'
pattern = r'<div class=\"author clearfix\">.*?<h2>\\n(\S+)\\n</h2>'

htmldoc = str(urllib.request.urlopen(url).read())
res = re.findall(pattern, htmldoc)

print(res)
for i in res:
	i = i.replace(r'\\', '\\')
	print(i,type(i))