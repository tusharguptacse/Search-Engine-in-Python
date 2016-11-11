import urllib2
from bs4 import BeautifulSoup
import time

def crawl(seed, depth,i):

	if depth != 0 :
		source = urllib2.urlopen(seed)
		soup = BeautifulSoup(source, 'html.parser')
		for item in soup.findAll('a'):
			var1 = item.get('href')
			if var1 != None:
				if '#' not in var1 and ':' not in var1:
					if var1.find('/wiki/') == 0:
						var2 = item.text.lower()
						if 'solar' in var2 or 'solar' in var1:
							urltemp = 'https://en.wikipedia.org' + var1
							if(urltemp not in list_done):
								i+=1
								list_done.append(urltemp)
								crawl(urltemp,depth-1,i)
	else:
		return


def crawler():
	global list_done
	list_done = list()
	seed = 'https://en.wikipedia.org/wiki/Sustainable_energy'
	depth = 5
	i = 0
	crawl(seed, depth,i)
	print
	print
	print
	print "              Number of Pages Crawled:              "
        print "===================================================="
        print
	print len(list_done)
	thefile = open('Task2B-URL.txt', 'w')
	for item in list_done:
		thefile.writelines("%s\n" % item)

crawler()
