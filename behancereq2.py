import requests
from bs4 import BeautifulSoup
import re
import json
from StringIO import StringIO
import csv
headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
    'Accept-Encoding':'gzip, deflate'
    'Accept-Language':'en-US,en;q=0.8'
    'Cache-Control':'max-age=0'
    'Connection':'keep-alive'
    'Content-Length':'18363'
    'Content-Type':'application/x-www-form-urlencoded'
    'Cookie':'ASP.NET_SessionId=tsapqa2vjov2r4eqpl2taqla; __lc.visitor_id.1584081=S1462901457.23f7d64add; JsCookieCheck=IsCookieEnabled=1; __utmt=1; __utma=89430809.1510805748.1462901458.1463152657.1463156104.3; __utmb=89430809.5.10.1463156104; __utmc=89430809; __utmz=89430809.1462901458.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); lc_window_state=minimized'
    'Host':'www.saffronart.com'
    'Origin':'http://www.saffronart.com'
    'Referer':'http://www.saffronart.com/Artist/ArtistList.aspx'
    'Upgrade-Insecure-Requests':'1'
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
}
url='http://www.saffronart.com/Artist/ArtistList.aspx'
html= requests.get(url, headers=headers).content
soup=BeautifulSoup(html,'html.parser')

    '''try:
        name=str(soup.find_all('span',{'class':"breadcrumb-text"},{'classes':"breadcrumb"})[1].text)
        info.append([ name])
    except:
        info.append(['none'])
        
    info[i].append(url)

    try:
        project_views=str(soup.find_all('a',{'class':"js-project-views-count"})[0].text)
        info[i].append(project_views)
    except:
        info[i].append('none')

    try:
        city=str(soup.find_all('a',{'class':'profile-location-link beicons-pre beicons-pre-location'})[0].text)
        info[i].append(city)
    except:
        info[i].append('none')
    fields=''
    try:
        for tag in soup.find_all('a',{'class':'field'}):
            fields=fields+', '+str(tag.text)
        info[i].append(fields)
    except:
        info[i].append('none')
    social=''
    try:
        for tag in soup.find_all('a',{'class':'ss-social'}):
            social=social+', '+str(tag.get('href'))
        info[i].append(social)
    except:
        info[i].append('none')
    try: 
        website=str(soup.find_all('a',{'id':'profile-website'})[0].text)
        info[i].append(website)
    except:
        info[i].append('none')
    try:
        email=re.search(r'([\w.]+@[\w.]+\.com)',html).group()
        info[i].append(email)
    except:
        info[i].append('none')
    print city, i

f=open('behanceall5.csv','w')
writer=csv.writer(f)
for row in info:
    writer.writerow(row)
f.close()'''




        

    
