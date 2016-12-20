import urllib2
import requests
import re
from bs4 import BeautifulSoup
import glob
import os.path


docidcount = 1
duplicatecount = 1
for url in glob.glob('InputFiles/*.html'):
	fil = open(url)
	response = fil.read()
	soup = BeautifulSoup(response)
	for t in soup.findAll('h1', id = 'firstHeading'):
		title = t.text
		title = title.replace(" ", "")
	for ch in ['-','_']:
		if ch in title:
			title = title.replace(ch,"")
	if os.path.exists('Web Pages/' + title + '.txt'):
		f = open('Web Pages/' + title + str(duplicatecount) + ".txt", 'a')
		duplicatecount = duplicatecount + 1
	else:
		f = open('Web Pages/' + title + ".txt", 'a')
	f.write(str(docidcount) + " ")
	for search in soup.findAll('div', id = 'mw-content-text'):
		for para in search.findAll('p'):
			webContent = (para.text.lower() + " ")
			webCon = re.sub("\[[0-9]+\]", "", webContent)
			webCon = re.sub(r'(\s)http\w+', "", webCon)
			webCon = webCon.replace("'s", "")
			webCon = webCon.replace(" -", "")
			webCon = webCon.replace(" , ", "")
			webCon = webCon.replace(" . ", "")
			for ch in ['&','#','!','@','#','$','%','^','*','(',')','_','+','=','{','}','[',']',':',';','"',"'",'<','>','?','/','\\','~','`']:
				if ch in webCon:
					webCon = webCon.replace(ch, "")
			Content = webCon.replace(", ", " ")
			Content = Content.replace(". ", " ")
			Content = Content.replace(" - ", " ")
			Content = re.sub("\s\s+", " ", Content)
			f.write(Content.encode('utf-8'))
		for para in search.findAll('ul'):
			if para.parent == 'div' and id == 'mw-content-text':
				webContent = (para.text.lower() + " ")
				webCon = re.sub("\[[0-9]+\]", "", webContent)
				webCon = webCon.replace("'s", "")
				webCon = re.sub(r'(\s)http\w+', "", webCon)
				webCon = webCon.replace(" -", "")
				webCon = webCon.replace(" , ", "")
				webCon = webCon.replace(" . ", "")
				for ch in ['&','#','!','@','#','$','%','^','*','(',')','_','+','=','{','}','[',']',':',';','"',"'",'<','>','?','/','\\','~','`']:
					if ch in webCon:
						webCon = webCon.replace(ch, "")
				Content = webCon.replace(", ", " ")
				Content = Content.replace(". ", " ")
				Content = Content.replace(" - ", " ")
				Content = re.sub("\s\s+", " ", Content)
				f.write(Content.encode('utf-8'))	
	f.close
	docidcount = docidcount + 1

