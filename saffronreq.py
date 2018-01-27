import requests
from bs4 import BeautifulSoup
import re
import json
from StringIO import StringIO
import csv
headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language':'en-US,en;q=0.8',
    'Cache-Control':'max-age=0',
    'Connection':'keep-alive',
    'Content-Length':'18363',
    'Content-Type':'application/x-www-form-urlencoded',
    'Cookie':'ASP.NET_SessionId=tsapqa2vjov2r4eqpl2taqla; __lc.visitor_id.1584081=S1462901457.23f7d64add; JsCookieCheck=IsCookieEnabled=1; __utmt=1; __utma=89430809.1510805748.1462901458.1463152657.1463156104.3; __utmb=89430809.5.10.1463156104; __utmc=89430809; __utmz=89430809.1462901458.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); lc_window_state=minimized',
    'Host':'www.saffronart.com',
    'Origin':'http://www.saffronart.com',
    'Referer':'http://www.saffronart.com/Artist/ArtistList.aspx',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
}


url='http://www.saffronart.com/Artist/ArtistList.aspx'
html= requests.get(url, headers=headers).content
soup=BeautifulSoup(html,'html.parser')
'''
try:
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

'''
#import scraperwiki
import mechanize
import re

# ASPX pages are some of the hardest challenges because they use javascript and forms to navigate
# Almost always the links go through the function function __doPostBack(eventTarget, eventArgument)
# which you have to simulate in the mechanize form handling library

# This example shows how to follow the Next page link

url = 'http://escorpio.csd.gob.es/BusquedaPublicaMapa/Pages/Ficha/Visor.aspx?43575A49306D4B376F675650496E386D3555796770513D3D=4C715546365263665A476B3D&4D6378664A3349666E67513D=69466856304B484E524F773D'
br = mechanize.Browser()

    # sometimes the server is sensitive to this information
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
response = br.open(url)
html = response.read()
print html
for pagenum in range(1):
    html = response.read()
    print "Page %d  page length %d" % (pagenum, len(html))
    print "Clinicians found:", re.findall("</td><td align=\"left\">.*?", html)


    br.select_form(name='aspnetForm')
    br.form.set_all_readonly(False)
    br['__EVENTTARGET'] = 'ctl00$ContentPlaceHolder2$grdRecords$ctl05$lnkViewEdit'
    br['__EVENTARGUMENT'] = ''
    response = br.submit()
html= response.read()
print html
print "Clinicians found:", re.findall("</td><td align=\"left\">.*?", html)

#import scraperwiki
import mechanize
import re

# ASPX pages are some of the hardest challenges because they use javascript and forms to navigate
# Almost always the links go through the function function __doPostBack(eventTarget, eventArgument)
# which you have to simulate in the mechanize form handling library

# This example shows how to follow the Next page link

url = 'http://gvaup.in/frmApplicantLogin.aspx?d=23&c=1&s=2'
br = mechanize.Browser()

    # sometimes the server is sensitive to this information
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
response = br.open(url)
html = response.read()
print html
for pagenum in range(1):
    html = response.read()
    print "Page %d  page length %d" % (pagenum, len(html))
    print "Clinicians found:", re.findall("</td><td align=\"left\">(.*?)</td>", html)


    br.select_form(name='aspnetForm')
    br.form.set_all_readonly(False)
    br['__EVENTTARGET'] = 'ctl00$ContentPlaceHolder2$grdRecords$ctl05$lnkViewEdit'
    br['__EVENTARGUMENT'] = ''
    response = br.submit()
html= response.read()
print html
print "Clinicians found:", re.findall("<td>(.*?)\\r\\n</td>", html,re.DOTALL)
'''

        

    
