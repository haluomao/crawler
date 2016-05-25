#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 
# Author: felix_mao
# Date:2016年5月25日
#
from  datetime  import  *  
import time

class TimeUtil:
	'封装了时间处理的类'
	
	@staticmethod 
	def today():
		return date.today()
		
	@staticmethod 
	def nowTime():
		return time.localtime(time.time());
		
	@staticmethod 	
	def format(dateObj, format):
		return dateObj.strftime(format)
		
	@staticmethod
	def simpleFormat(dateObj):
		formatStr='%Y-%m-%d %H:%M:%S'
		return format(dateObj, formatStr)
	
	
	@staticmethod
	def quickTime(timeObj):
		formatStr='%Y-%m-%d %H:%M:%S'
		return  time.strftime(formatStr, timeObj)
	
	@staticmethod
	def time2Date(timeObj):
		return date.fromtimestamp(timeObj)
		
	@staticmethod
	def prefix():
		return format(date.today(), '%Y-%m-%d')
		
if __name__ == '__main__':	
	print 'date.today():' , date.today()  
	print 'date.fromtimestamp():' , date.fromtimestamp(time.time())   
	print TimeUtil.quickTime( time.localtime(time.time()))
	print TimeUtil.prefix()