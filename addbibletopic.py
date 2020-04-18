#!/usr/bin/env python
import subprocess
from subprocess import call
import cgitb
import cgi
import json
import string
import re
import datetime
#import mysql.connector as conn
cgitb.enable()

print("Content-Type: text/html;charset=utf-8")
print ("Content-type:text/html\r\n\r\n")


# # Create instance of FieldStorage
form = cgi.FieldStorage()

topic = form.getvalue('topic')
print(topic)

filename = "../html/bible.onecloudapps.net/topics.json"
github = "../html/gesab001/github-website/gesab001.github.io/topics.json"
data = {}
with open(filename) as json_file:
    data = json.load(json_file)

newobject = {"name": topic}
if newobject in data["topics"]:
   print("already exists")
else:
  data["topics"].append(newobject)
  print(topic + " " + "added")
data["topics"].sort()
for item in data["topics"]:
   print(item["name"])
   print("<br>")

with open(filename, 'w') as outfile:
    json.dump(data, outfile)

with open(github, 'w') as outfile:
    json.dump(data, outfile)
