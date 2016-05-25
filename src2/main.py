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
	url = "http://roll.finance.sina.com.cn/finance/zq1/ssgs/index_1.shtml";
	saveFile=TimeUtil.prefix()+".txt"	
	
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
			timeValue = HtmlUtil.select_v(page, '.time-source')
			timeValue = StrUtil.trim(timeValue)
			print timeValue
			self.saveToFile(timeValue+"\n")
		except:
			msg= u"获取时间信息失败，你敢信？"
			print msg
			self.saveToFile(str(msg)+"\n")
		
		#区域2
		try:
			contentValue = HtmlUtil.select_vs(page, '#articleContent p')		
			for src in contentValue:
				print src
				self.saveToFile(str(src)+"\n")
		except:
			msg= u"获取内容失败，你敢信？"
			print msg
			self.saveToFile(str(msg)+"\n")
		
	
	def saveToFile(self, value):
		FileUtil.append(self.saveFile, value);
		
	def main(self):
		url2 = 'http://finance.sina.com.cn/roll/2016-05-25/doc-ifxsqtya6053789.shtml'
		self.getPageMore(url2)
		
if __name__ == '__main__':
	PageCrawler().main()