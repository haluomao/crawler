import urllib  
import urllib2  
import re

class spider:
	
	def __init__(self):
		self.siteURL = 'http://roll.finance.sina.com.cn/finance/zq1/ssgs/index_';

	def getPage(url):		
		user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)' ;
		values = {'username' : 'cqc',  'password' : 'XXXX' }  ;
		headers = { 'User-Agent' : user_agent }  ;
		request = urllib2.Request(url, '', headers); 
		response = urllib2.urlopen(request);
		return response.read();
		
	def getContents(self, url):
		page = self.getPage(url)
        pattern = re.compile('<div class="list-item".*?pic-word.*?<a href="(.*?)".*?<img src="(.*?)".*?<a class="lady-name.*?>(.*?)</a>.*?<strong>(.*?)</strong>.*?<span>(.*?)</span>',re.S)
        items = re.findall(pattern,page)
        for item in items:
            print item[0],item[1],item[2],item[3],item[4]
		
	'''
	url = 'http://www.server.com/login'
	user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'  
	values = {'username' : 'cqc',  'password' : 'XXXX' }  
	headers = { 'User-Agent' : user_agent }  
	data = urllib.urlencode(values)  
	request = urllib2.Request(url, data, headers)  
	response = urllib2.urlopen(request)  
	page = response.read() 
	'''
	
spider = Spider()
spider.getContents(1)
	url = "http://roll.finance.sina.com.cn/finance/zq1/ssgs/index_1.shtml";
	print getPage(url);
	os.system("pause");