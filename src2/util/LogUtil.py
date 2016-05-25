#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 
# Author: felix_mao
# Date:2016��5��25��
#
import logging  
import logging.handlers  
from TimeUtil import TimeUtil

class LogUtil:
	'��װ����־��¼����'
	LOG_FILE = 'logs/'+TimeUtil.prefix()+'.log' 
	def __init__(self, v):
		handler = logging.handlers.RotatingFileHandler(self.LOG_FILE, maxBytes = 1024*1024, backupCount = 5)
		#ʵ����handler   
		fmt = '%(asctime)s - %(filename)s:%(lineno)s - %(name)s - %(message)s'
		formatter = logging.Formatter(fmt)   # ʵ����formatter  
		handler.setFormatter(formatter)      # Ϊhandler���formatter  
		  
		self.logger = logging.getLogger(v)    # ��ȡ��Ϊtst��logger  
		self.logger.addHandler(handler)           # Ϊlogger���handler  
		self.logger.setLevel(logging.DEBUG)  
		
	def updateFile(self, logFile):
		self.LOG_FILE = logFile
		
	def info(self, msg):
		logger.info(msg)
		
	def debug(self, msg):
		logger.debug(msg)