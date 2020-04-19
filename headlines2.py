#!/usr/bin/python3
from subprocess import call
import cgitb
import subprocess
import urllib.request
import requests
#import mysql.connector as conn
cgitb.enable()    


print("Content-Type: text/html;charset=utf-8")
print ("Content-type:text/html\r\n\r\n")
rss = {"rss":[{"cnn": "http://rss.cnn.com/rss/edition.rss"},
              {"nzherald": "https://rss.nzherald.co.nz/rss/xml/nzhtsrsscid_000000698.xml"}]}
url = rss["rss"][1]["nzherald"]
#print(url)
html = ""
r = requests.get(url)
with urllib.request.urlopen(url ) as response:
   html = response.read()
#text = unicode(str(r.text), errors='ignore')
#print ((r.text))
#print(str(html))
def beginning(string):
    list = string.split(" ")
    for x in list:
       print (x)
       print ("<br>")

string = "In the beginning God created the heaven and the earth. Genesis 1:1"
#beginning(string)
#subprocess.call("poweroff", shell=True)

#f = open("nzherald.xml", "w")
#result = html
#f.write(str(html))


URL = url

response = requests.get(URL)
#print(response.text)
with open('../html/headlines.onecloudapps.net/nzherald.xml', 'wb') as file:
    file.write(response.content)
