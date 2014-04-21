from bs4 import BeautifulSoup
import urllib2, time

#base="http://www.beeradvocate.com/2/"
ctr=3


#print source

while ctr<5:
    req = urllib2.Request("http://www.beeradvocate.com/beer/profile/2/"+str(ctr)+"/")
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.64 Safari/537.31')
    source = urllib2.urlopen(req).read()
    time.sleep(1)
#    f=urllib.urlopen("http://direct.beeradvocate.com/"+str(ctr)+"/")
 #   f=grab_cloudflare("http://www.beeradvocate.com/2/3/")
    soup=BeautifulSoup(source)
    title=str(soup.findAll("title"))
    beer,brewery,city,beerad=title.split("|")
    print beer
    ctr=ctr+1
