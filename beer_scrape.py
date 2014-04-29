from BeautifulSoup import BeautifulSoup
import urllib2, time, re

ctr=1468

while ctr<1469:
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
    

    URL=str(soup.findAll(attrs={"name":re.compile("twitter:url")}))
    URL=re.search(r'(?<=content=").*?(?=")',URL).group()
    print str(URL)

    req=urllib2.Request(str(URL)+"?show_ratings=Y")
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.64 Safari/537.31')
    source = urllib2.urlopen(req).read()
    time.sleep(1)
    soup=BeautifulSoup(source)

    reviews=soup.findAll(attrs={"id":re.compile("rating_fullview_content_2")})
    for review in reviews:
        reviewers=re.search(r'(?<=<b>).*?(?=</b>)',str(review)).group()
        norm_score=re.search(r'(?<=BAscore_norm">).*?(?=</span)',str(review)).group()
        review_long=re.search(r'(?<=[\d]<br /><br />).*?(?=<br /><br />Serving)',str(review))
        if review_long is None:
            print str(reviewers)+" "+(norm_score)
        else:
            remove=['<br />','\r','\x93','\xc2','\x94']
            review_long=review_long.group()
            for i in remove:
                review_long=review_long.replace(i,'')
            print str(reviewers)+" "+(norm_score)+" "+str(review_long)
        #print reviewers
    #for i in reviews:
    #print reviewers
    
    #print reviews
    #print reviewers
    notes=re.findall(r'(?<=>look).*?(?=<br)',reviews,re.DOTALL)
    #print notes
    review=re.findall(r'(?<=[\d]<br /><br />).*?(?=<br /><br />)',reviews,re.DOTALL)
    #review=re.findall('
    #print review
    notes=[re.sub(r'[^\d.\s]+','',r) for r in notes]
    remove=['<br />','\r','\x93','\xc2','\x94']
 
    
    for x in range(0,3):
        print reviewers[x]+"\n"+notes[x]+"\n"+review[x]
        print "******************"
    
    ctr=ctr+1
