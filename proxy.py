# -*- coding: utf-8 -*-
import urllib.request,urllib.error


proxy_ip_list = ["118.116.41.24:8118","60.13.187.162:63000","61.135.217.7:80","114.113.126.83:80","118.31.223.194:3128","101.132.122.230:3128","112.115.57.20:3128","114.215.95.188:3128","118.89.38.21:8080","223.93.172.248:3128","218.60.8.83:3129"]
def use_proxy(proxy_ip, url):

	headers = ("User-Agent", "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:54.0) Gecko/20100101 Firefox/54.0")
	proxy = urllib.request.ProxyHandler({'http':proxy_ip})
	opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler(debuglevel=0))
	opener.addheaders = [headers]
	urllib.request.install_opener(opener)
	data = urllib.request.urlopen(url, timeout=15).read().decode('utf-8')
	return len(data)

for proxy_ip in proxy_ip_list:
	try:
		data = use_proxy(proxy_ip, 'http://blog.csdn.net')
		print(proxy_ip,data)
	except urllib.error.URLError as e:
		print(e,proxy_ip,e.reason)
		if hasattr(e,"code"):
			print(e.code)
	except Exception as e:
		print(e,proxy_ip,"$")