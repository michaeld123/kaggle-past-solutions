#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib.request
import urllib.error
import re
import os

# put out.txt in script dir
full_path = os.path.realpath(__file__)
target = open(os.path.dirname(full_path) + "/out.txt", 'w+')

# Make URLs a set to that they are unique
output = set()

# Loop over all winners interviews pages, their are currently 16 pages
for jj in range(1,20):
    try:
        url = 'http://blog.kaggle.com/category/winners-interviews/page/' +str(jj)
        print( "Requesting URL: "+ url)
        req = urllib.request.Request(url)
        resp = urllib.request.urlopen(req)
        respData = resp.read()
    except urllib.error.URLError:
        print("URL doesnt exist " + url )
        break

    # Find all urls from page
    paragraphs = re.findall(r'"http://blog.kaggle.com/(.*?)"',str(respData))

    # Cull some unwanted URLs and add to set
    for line in paragraphs:
        if line[:2] == "20" and "comments" not in line:
           output.add("http://blog.kaggle.com/"+line)

# Sort output and write out
out2=list(output)
out2.sort()
for url in out2:
   target.write(url + "\n")
target.close()




