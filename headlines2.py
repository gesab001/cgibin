#!/usr/bin/python3
from subprocess import call
import cgitb
import cgi

import subprocess
import urllib.request
import requests
#import mysql.connector as conn
cgitb.enable()    
# Create instance of FieldStorage
form = cgi.FieldStorage()
#
# # Get data from fields
# #first_name = form.getvalue('first_name')
# #last_name  = form.getvalue('last_name')
news = form.getvalue('news')

print("Content-Type: text/html;charset=utf-8")
print ("Content-type:text/html\r\n\r\n")
rss = {"cnn": "http://rss.cnn.com/rss/edition.rss",
        "nzherald": "https://rss.nzherald.co.nz/rss/xml/nzhtsrsscid_000000698.xml",
        "smh": "https://www.smh.com.au/rss/feed.xml"}


url= rss[news]

response = requests.get(url)
print(response.text)
try:
 with open('../html/headlines.onecloudapps.net/'+news+'.xml', 'wb') as file:
    file.write(response.content)
except Exception as ex:
    print(ex)