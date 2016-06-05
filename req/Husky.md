##项目的流程说明
1. 爬虫编写
	1. 抓取公司新闻
	2. 抓取证券交易所的*信息披露*
		1. [上海证券交易所](http://www.sse.com.cn/disclosure/overview/)
		http://www.sse.com.cn/disclosure/listedinfo/listing/ 标题
		2. [深圳证券交易所](http://www.szse.cn/main/disclosure/)



		#################################################################################################
		#>3. [新浪财经](http://roll.finance.sina.com.cn/finance/zq1/ssgs/index.shtml)			#
		#>4. [东方财富网](http://finance.eastmoney.com/news/cssgs.html)					#
		#												#
		#https://github.com/TimePi/Python/blob/master/spyder/WebSpyder.py				#
		#https://github.com/TimePi/Python/blob/master/Stock/DFCF_CompanyTextDataDownloader.py		#
		#												#
		#【全量抓取和动态抓取要注意】									#
		#												#
		#												#
		#												#
		#时间，标题，url，来源，内容（存放在TXT里）							#
		#################################################################################################
		5. `以后可能还要抓很多`

2. 文本分析
	1. 文本分句，分词，停用词过滤
	2. 情感分析，关键词提取，
	3. 相似度判断（过滤相同的文本）
3. 结果呈现
	1. 采用Echarts来展示（H5，JS）`动态散点图`，`关系图等等`
