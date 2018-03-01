from itertools import chain

class TweetCriteria(object):
	
	def __init__(self):
		self.maxTweets = 0
		self.within = "15mi"

	def __str__(self):
		strTwitCrit = "Search Query: "
		return  strTwitCrit + str(self.__dict__)
		
	def setUsername(self, username):
		self.username = username
		return self
		
	def setSince(self, since):
		self.since = since
		return self
	
	def setUntil(self, until):
		self.until = until
		return self
		
	def setQuerySearch(self, querySearch):
		self.querySearch = querySearch
		return self
	
	def setHashtagSearch(self, hashtagSearch):
		self.hashtagSearch = hashtagSearch
		return self
		
	def setMaxTweets(self, maxTweets):
		self.maxTweets = maxTweets
		return self

	def setTopTweets(self, topTweets):
		self.topTweets = topTweets
		return self
	
	def setNear(self, near):
		self.near = near
		return self

	def setWithin(self, within):
		self.within = within
		return self
