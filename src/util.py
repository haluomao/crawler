###########################
# Interface to use urllib2
###########################

import urllib2

def open(url):
	request=urllib2.request(url)
	response=urllib2.urlopen(request)
	print response.read();

print open("http://www.baidu.com")
