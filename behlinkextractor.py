import re
import sys

f='surat.log'
f=open(f,'r')
lines=f.readlines()

l=len(lines)
for i in range(l):
    match=re.search(r'search',lines[l-1-i])
    if match: lines.pop(l-i-1)
    elif lines[l-i-1]=='\n': lines.pop(l-i-1)
    else: lines[l-i-1]=(lines[l-i-1]).strip('\n')

l=len(lines)
for i in range(l/2):
    lines.pop(l-2*i-1)
for i in range(7):
    lines.pop(0)
for i in range(8):
    lines.pop(-1)




    



