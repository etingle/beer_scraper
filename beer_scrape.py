from BeautifulSoup import BeautifulSoup
import urllib2, time, re

ctr=3

while ctr<4:
    req = urllib2.Request("http://www.beeradvocate.com/beer/profile/2/"+str(ctr)+"/")
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.64 Safari/537.31')
    source = urllib2.urlopen(req).read()
    time.sleep(1)
    soup=BeautifulSoup(source)
    titles=str(soup.findAll("title"))
    title=re.search(r'(?<=<title>).*?(?=</title>)',titles).group()

    beer,brewery,city,beerad=title.split("|")

    styles=str(soup.find("a",{"href":re.compile("/beer/style/(.+?)")}).find("b"))
    styles=styles.replace("<b>","")
    styles=styles.replace("</b>","")
    
    reviews=str(soup.findAll(attrs={"id":re.compile("rating_fullview_content_2")}))
    reviewers=re.findall(r'(?<=<b>).*?(?=</b>)',reviews,re.DOTALL)
    notes=re.findall(r'(?<=>look).*?(?=<br)',reviews,re.DOTALL)
    
    review=re.findall(r'(?<=[\d]<br /><br />).*?(?=<br /><br />)',reviews,re.DOTALL)
    notes=[re.sub(r'[^\d.\s]+','',r) for r in notes]
    remove=['<br />','\r','\x93','\xc2','\x94']
    for i in remove:
        review=[r.replace(i,'') for r in review]
    
    for x in range(0,3):
        print reviewers[x]+"\n"+notes[x]+"\n"+review[x]
        print "******************"
    ctr=ctr+1
