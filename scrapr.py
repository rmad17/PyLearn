import urllib2

from bs4 import BeautifulSoup

url="https://en.wikipedia.org/wiki/Asansol#"#raw_input("Enter the webpage you want to scrap\n")http://developertimes.wordpress.com/2013/07/03/why-i-should-use-linux/#https://en.wikipedia.org/wiki/Asansol#http://www.goal.com/en/news/archive/1
if url[0:4] != "http":
	url='http://'+url
#file=open("pywiki.txt","wb")
content=" "
header=""
soup=BeautifulSoup(urllib2.urlopen(url).read())
#soup.prettify()
#print soup.getText()
#header=content.join([h.getText() for h in soup.findAll(re.compile('^h'))])
#header=header+content.join([h.getText() for h in soup.find_all('a')
content=content.join([p.getText()+'\n' for p in soup.find_all({'title':True,'h1':True,'h2':True,'h3':True,'h4':True,'h5':True,'h6':True,'p':True})])
content='\n'+header+'\n\n'+content
print content
#file.write(str(content))
#file.close()


