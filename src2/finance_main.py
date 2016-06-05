# -*- coding: utf-8 -*-
"用于抓取特定网站的链接和内容"
from util.FileUtil import FileUtil
from util.HtmlUtil import HtmlUtil
from util.HttpUtil import HttpUtil
from util.StringUtil import StrUtil
from util.TimeUtil import TimeUtil
from util.LogUtil import LogUtil

debug=False
Log = LogUtil('PageCrawler')

class PageCrawler:
	url = 'http://finance.eastmoney.com/news/cssgs.html'
	saveFile='data/finance_'+TimeUtil.prefix()+'_home.txt'	
	
	def getPage(self, url):
		"获取第一页的内容，返回标题和url"
		page = HttpUtil.getPage(self.url);
		res = HtmlUtil.select_href_text(page, 'ul li a')
		return res
		
	def getPageMore(self, url):
		"获取第二页的内容，返回文件"
		#page2 = HttpUtil.getPage(url)
		#FileUtil.append('2.txt', page2);
		page = FileUtil.read('2.txt')
		#区域1
		try:	
			timeValue = HtmlUtil.select(page, '.time-source')
			timeValue = StrUtil.trim(str(timeValue))
			print timeValue
			self.saveToFile(timeValue+"\n")
		except:
			msg= u"获取时间信息失败，你敢信？"
			print msg
			self.saveToFile(str(msg)+"\n")
		#区域2
		try:
			contentValue = HtmlUtil.select_all(page, '#articleContent p')		
			for src in contentValue:
				print src
				self.saveToFile(str(src)+"\n")
		except:
			msg= u"获取内容失败，你敢信？"
			print msg
			self.saveToFile(str(msg)+"\n")
		
	
	def saveToFile(self, value):
		FileUtil.append(self.saveFile, value);
	
	def getHomePage(self):				
		FileUtil.put(self.saveFile, '');	
		page = HttpUtil.getPage(self.url);
		res = HtmlUtil.select_href_text(page, '.mainCont .listBox .list ul li a')
		for (k,v) in res.items():
			#print k+'|'+v
			FileUtil.appendline(saveFile, k+'|'+v );
			
	def getDetailPage(self):
		content=FileUtil.readlines(self.saveFile)
		for s in content:
			title=s.split('|')[0] #标题
			url=s.split('|')[1]	#url
			print url			
			page = HttpUtil.getPage(url);
			arr = HtmlUtil.select_all(page, '.newText .Info span')
			date=''
			source=''
			#获取时间/来源
			for k in arr:
				if k is not None:
					if "年" in str(k):
						date=str(k);
					if "来源" in str(k):
						source=str(k);
			content_review = HtmlUtil.select_v(page, '#ContentBody .c_review')
			
			if content_review is None:
				content_review=''
			arr = HtmlUtil.select_text(page, '#ContentBody p')
			#记录到文件
			newFile="data/finance"+url.split(',')[1][:-6]+".txt"
			FileUtil.put(newFile, '')
			FileUtil.appendline(newFile, title+"\n")
			FileUtil.appendline(newFile, url)
			FileUtil.appendline(newFile, date+"\n")
			FileUtil.appendline(newFile, source+"\n")
			FileUtil.appendline(newFile, content_review+"\n")
			for k in arr:
				try:
					FileUtil.appendline(newFile, str(k))
				except:
					continue;
		
	def main(self):
		#获取首页链接
		#self.getHomePage()
		#分析链接文件
		self.getDetailPage()
		
if __name__ == '__main__':
	PageCrawler().main()
	#pageCrawler=PageCrawler()
	
	#print res.decode('utf-8')
	#FileUtil.put(saveFile, str(res) );