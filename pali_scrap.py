#using bleach and BeautifulSoup for scraping from GRETIL

import urllib2
from bs4 import BeautifulSoup
import os
import re
import bleach

def make_dir(directory):
	if not os.path.exists(directory):
			os.makedirs(directory) 

url_list = []
#working on it																													

foldername = ["2_parcan","3_chron","4_comm","6_suanco","9_phil","9_phil/lex","9_phil/rhet"]




k = 1
for j in (1,7):
	folder = foldername[k-1]
	directory = "pali_texts_GRETIL/" + folder
	make_dir(directory)
	for u in url_list[k-1]:
		url = u
		print u
		print k-1
		hc = urllib2.urlopen(url)
		soup = BeautifulSoup(hc,"lxml")
		h = soup.find('body')
		file_name = url[-12:-4] 
		path_=directory+"/" + file_name + ".txt"
		target = open(path_,'w')
		clean = bleach.clean(h, tags = [], strip = True)
		target.write(clean.encode('utf8'))
	k = k + 1	
