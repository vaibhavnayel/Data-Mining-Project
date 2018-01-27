import re
f=open(r'C:\Users\Vaibhav Nayel\Desktop\new.txt','r')
f=f.read()
l=re.findall('\.\.\/artists\/([\w\-,.]+)',f)
