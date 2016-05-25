#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 
# Author: felix_mao
# Date:2016年5月25日
#
import logging  
import logging.handlers  
from TimeUtil import TimeUtil

class LogUtil:
	'封装了日志记录的类'
	LOG_FILE = 'logs/'+TimeUtil.prefix()+'.log' 
	def __init__(self, v):
		handler = logging.handlers.RotatingFileHandler(self.LOG_FILE, maxBytes = 1024*1024, backupCount = 5)
		#实例化handler   
		fmt = '%(asctime)s - %(filename)s:%(lineno)s - %(name)s - %(message)s'
		formatter = logging.Formatter(fmt)   # 实例化formatter  
		handler.setFormatter(formatter)      # 为handler添加formatter  
		  
		self.logger = logging.getLogger(v)    # 获取名为tst的logger  
		self.logger.addHandler(handler)           # 为logger添加handler  
		self.logger.setLevel(logging.DEBUG)  
		
	def updateFile(self, logFile):
		self.LOG_FILE = logFile
		
	def info(self, msg):
		logger.info(msg)
		
	def debug(self, msg):
		logger.debug(msg)