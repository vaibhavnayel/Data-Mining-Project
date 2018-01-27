import requests
from bs4 import BeautifulSoup
import re
import csv
import json
from StringIO import StringIO
import csv

'''html= requests.get(r'https://www.artstation.com/users/prashant0t4.json')
text=html.content
json=json.loads(text)'''

f=open('artstationlinks.txt','r')
text=f.read()
links=text.split(',')
info=[]
f=open('artstationdata.csv','w')

for i  in range(len(links)):
    info.append([])
    try:
        html= requests.get(links[i])
        text=html.content
        j=json.loads(text)
        info[i].append(str(j['full_name']))
        skills=''
        for dic in j['skills']:
            skills=skills+str(dic['name'])+'+ '
        info[i].append(skills)
        info[i].append(str(j['project_views_count']))
        info[i].append(str(j['city']))
        info[i].append(str(j['artstation_url']))
        info[i].append(str(j['linkedin_url']))
        info[i].append(str(j['deviantart_url']))
        info[i].append(str(j['tumblr_url']))
        info[i].append(str(j['google_plus_url']))
        info[i].append(str(j['facebook_url']))
        info[i].append(str(j['twitter_url']))
        info[i].append(str(j['youtube_url']))
        info[i].append(str(j['instagram_url']))
        info[i].append(str(j['vimeo_url']))
    except:
        print 'error'
    print i

    



