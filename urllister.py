from sgmllib import SGMLParser
import urllib2
from bs4 import BeautifulSoup
import os
import re
import bleach

class URLLister(SGMLParser):
	def reset(self):
		SGMLParser.reset(self)
		self.urls = []

	def start_a(self, attrs):
		href = [v for k, v in attrs if k=='href']
		if href:
			self.urls.extend(href)

			
if __name__ == "__main__":
	print "Working"
	usock = urllib2.urlopen("file:///E:/content/language/sahityasahyam/0cf71.html")
	parser = URLLister()
	parser.feed(usock.read())
	parser.close()
	usock.close()
	ls1 = []
	#parser.urls = parser.urls[:-4]
	for u in parser.urls:
		print u
		ls1.append(u)
	raw_input()
	ls2 = filter(lambda x: x!= '#', ls1)
	ls = ["file:///E:/content/language/sahityasahyam/" + u for u in ls2]
	raw_input()
	for p in ls:
		print p
		
	directory = "malayalam_text_wikisource/malayalam_text_wikisource/content/language/sahityasahyam/"
	print "It's fine"
	raw_input()
	print len(ls)
	count = 0
	print "Counting"
	raw_input()
	for x in ls:
		print count
		print x
		filename = str(count)
		path_ = directory + filename + '.txt'
		target = open(path_,'w')
		try:
			hc = urllib2.urlopen(x)
			soup = BeautifulSoup(hc,"lxml")
			h = soup.find('div', {'class' : 'mw-content-ltr'})
			clean = bleach.clean(h, tags = [], strip = True)
			target.write(clean.encode('utf8'))
			count = count + 1
		except Exception:
			pass
	
raw_input()		
	