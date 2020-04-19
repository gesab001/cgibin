#!/usr/bin/python3
from subprocess import call
import cgitb
import subprocess
import urllib.request

#import mysql.connector as conn
#cgitb.enable()


print("Content-Type: text/html;charset=utf-8")
print ("Content-type:text/html\r\n\r\n")
rss = {"rss":[{"cnn": "http://rss.cnn.com/rss/edition.rss"},
              {"nzherald": "https://rss.nzherald.co.nz/rss/xml/nzhtsrsscid_000000698.xml"}]}
url = rss["rss"][1]["nzherald"]
#print(url)
html = ""

with urllib.request.urlopen(url ) as response:
   html = response.read()

print(str(html))
try:
 f = open("../html/headlines.onecloudapps.net/nzherald.xml", "w")
 f.write(html.decode("utf-8"))
except Exception as ex:
 #f.close()
 print(ex)
#f = open("../html/headlines.onecloudapps.net/nzherald.xml")
#string = f.read()
#print(str(string))
