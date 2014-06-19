import urllib2,subprocess
from bs4 import BeautifulSoup

url="http://www.debian.org/mirror/list"
#if url[0:4] != "http":
#	url='http://'+url
#file=open("mirror","wb")
mirror_list=[]
soup=BeautifulSoup(urllib2.urlopen(url).read())
mirror_list=mirror_list+["ftp://"+h.getText() for h in soup.findAll('a',limit=(62))]
del mirror_list[0:13]
mirror_list.insert(0,'netselect')

proc=subprocess.Popen(mirror_list,stdout=subprocess.PIPE)
output=proc.stdout.read()
#print output
print output[6:]



