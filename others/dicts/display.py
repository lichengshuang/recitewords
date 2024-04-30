#!/usr/bin/env python3
import os
import json


secretconfig = 'IELTS_3.json'
with open(secretconfig,'r') as f:
	news = json.loads(f.read())

lines2 = json.dumps(news,sort_keys=False,indent=4,ensure_ascii=False) + "\n"
print (lines2)


with open('newdicts.json','w') as f:
	f.write('%s\n' % lines2)
