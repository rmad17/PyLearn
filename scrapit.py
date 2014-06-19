import urllib2
from bs4 import BeautifulSoup

def scrapit(url):
	soup=BeautifulSoup(urllib2.urlopen(url).read())
	content=content.join([p.getText()+'\n' for p in soup.find_all({'title':True,'h1':True,'h2':True,'h3':True,'h4':True,'h5':True,'h6':True,'p':True})])
	content= '\n'+content
	return content
	
