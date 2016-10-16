import urllib2
from bs4 import BeautifulSoup
import os
import re
import bleach

def make_dir(directory):
	if not os.path.exists(directory):
			os.makedirs(directory) 

url_list = [["file:///C:/Users/ADMIN/Desktop/Pali_GRETEL/2_pali/2_parcan/milind1u.htm",
			 "file:///C:/Users/ADMIN/Desktop/Pali_GRETEL/2_pali/2_parcan/milind2u.htm",
			 "file:///C:/Users/ADMIN/Desktop/Pali_GRETEL/2_pali/2_parcan/milindou.htm",
			 "file:///C:/Users/ADMIN/Desktop/Pali_GRETEL/2_pali/2_parcan/milindpu.htm",
			 "file:///C:/Users/ADMIN/Desktop/Pali_GRETEL/2_pali/2_parcan/nettip_u.htm",
			 "file:///C:/Users/ADMIN/Desktop/Pali_GRETEL/2_pali/2_parcan/petako_u.htm"],
			["file:///C:/Users/ADMIN/Desktop/Pali_GRETEL/2_pali/3_chron/dhatuvau.htm",
			 "file:///C:/Users/ADMIN/Desktop/Pali_GRETEL/2_pali/3_chron/dipav_2u.htm",
			 "file:///C:/Users/ADMIN/Desktop/Pali_GRETEL/2_pali/3_chron/dipava1u.htm",
			 "file:///C:/Users/ADMIN/Desktop/Pali_GRETEL/2_pali/3_chron/dipava2u.htm",
			 "file:///C:/Users/ADMIN/Desktop/Pali_GRETEL/2_pali/3_chron/dipavmsu.htm",
			 "file:///C:/Users/ADMIN/Desktop/Pali_GRETEL/2_pali/3_chron/hattha_u.htm",
			 "file:///C:/Users/ADMIN/Desktop/Pali_GRETEL/2_pali/3_chron/mahava_u.htm"],
			["file:///C:/Users/ADMIN/Desktop/Pali_GRETEL/2_pali/4_comm/buvismou.htm",
			 "file:///C:/Users/ADMIN/Desktop/Pali_GRETEL/2_pali/4_comm/buvismpu.htm",
			 "file:///C:/Users/ADMIN/Desktop/Pali_GRETEL/2_pali/4_comm/samp_1ou.htm",
			 "file:///C:/Users/ADMIN/Desktop/Pali_GRETEL/2_pali/4_comm/samp_1pu.htm",
			 "file:///C:/Users/ADMIN/Desktop/Pali_GRETEL/2_pali/4_comm/samp_2ou.htm",
			 "file:///C:/Users/ADMIN/Desktop/Pali_GRETEL/2_pali/4_comm/samp_2pu.htm",
			 "file:///C:/Users/ADMIN/Desktop/Pali_GRETEL/2_pali/4_comm/samp_3ou.htm",
			 "file:///C:/Users/ADMIN/Desktop/Pali_GRETEL/2_pali/4_comm/samp_3pu.htm",
			 "file:///C:/Users/ADMIN/Desktop/Pali_GRETEL/2_pali/4_comm/samp_4ou.htm",
			 "file:///C:/Users/ADMIN/Desktop/Pali_GRETEL/2_pali/4_comm/samp_4pu.htm",
			 "file:///C:/Users/ADMIN/Desktop/Pali_GRETEL/2_pali/4_comm/samp_5ou.htm",
			 "file:///C:/Users/ADMIN/Desktop/Pali_GRETEL/2_pali/4_comm/samp_5pu.htm",
			 "file:///C:/Users/ADMIN/Desktop/Pali_GRETEL/2_pali/4_comm/samp_6ou.htm",
			 "file:///C:/Users/ADMIN/Desktop/Pali_GRETEL/2_pali/4_comm/samp_6pu.htm",
			 "file:///C:/Users/ADMIN/Desktop/Pali_GRETEL/2_pali/4_comm/samp_7ou.htm",
			 "file:///C:/Users/ADMIN/Desktop/Pali_GRETEL/2_pali/4_comm/samp_7pu.htm",
			 "file:///C:/Users/ADMIN/Desktop/Pali_GRETEL/2_pali/4_comm/visudd_u.htm"],
			 
			["file:///C:/Users/ADMIN/Desktop/Pali_GRETEL/2_pali/6_suanco/lokapp_u.htm",
			 "file:///C:/Users/ADMIN/Desktop/Pali_GRETEL/2_pali/6_suanco/upasak_u.htm"],
			 
			["file:///C:/Users/ADMIN/Desktop/Pali_GRETEL/2_pali/9_phil/dhkariku.htm",
			 "file:///C:/Users/ADMIN/Desktop/Pali_GRETEL/2_pali/9_phil/mkacbheu.htm",
			 "file:///C:/Users/ADMIN/Desktop/Pali_GRETEL/2_pali/9_phil/yaskacsu.htm"],
			["file:///C:/Users/ADMIN/Desktop/Pali_GRETEL/2_pali/9_phil/lex/abhidh_u.htm"],
			["file:///C:/Users/ADMIN/Desktop/Pali_GRETEL/2_pali/9_phil/rhet/subodh_u.htm"]]
																													

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
	
	
	
raw_input("Press:")	