from BeautifulSoup import BeautifulSoup
import urllib2, time, re, util

ctr=3


#print source

while ctr<5:
    req = urllib2.Request("http://www.beeradvocate.com/beer/profile/2/"+str(ctr)+"/")
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.64 Safari/537.31')
    source = urllib2.urlopen(req).read()
    time.sleep(1)
    soup=BeautifulSoup(source)
    titles=str(soup.findAll("title"))

    print titles
    title=re.search(r'(?<=<title>).*?(?=</title>)',titles).group()


   # print title

    beer,brewery,city,beerad=title.split("|")
    print beer
    styles=str(soup.find("a",{"href":re.compile("/beer/style/(.+?)")}).find("b"))
    styles=styles.replace("<b>","")
    styles=styles.replace("</b>","")
    
    print styles
    ctr=ctr+1
