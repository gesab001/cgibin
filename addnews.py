#!/usr/bin/python3
from subprocess import call
import cgitb
import cgi
import subprocess
import urllib.request
import json
#import mysql.connector as conn
cgitb.enable()  
form = cgi.FieldStorage()
  
keyword = form.getvalue('keyword')
title = form.getvalue('title')
url = form.getvalue('url')

print("Content-Type: text/html;charset=utf-8")
print ("Content-type:text/html\r\n\r\n")
#news = input("news: " )
#rss = input("rss: " )
print(keyword)
print(title)
print(url)
filepath = '../html/headlines.onecloudapps.net/news.json' 
f = open(filepath)
json_string = f.read()
data = json.loads(json_string)
data[keyword] = url
print(data)
f.close()


with open(filepath, 'w') as outfile:
    json.dump(data, outfile)
 
filepath = '../html/headlines.onecloudapps.net/newstitles.json' 
f = open(filepath)
json_string = f.read()
data = json.loads(json_string)
data[keyword] = title
print(data)
f.close()


with open(filepath, 'w') as outfile:
    json.dump(data, outfile)