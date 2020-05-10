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
#cgitb.enable()

print("Content-Type: text/html;charset=utf-8")
print ("Content-type:text/html\r\n\r\n")


# # Create instance of FieldStorage
#form = cgi.FieldStorage()

#topic = form.getvalue('topic')
#print(topic)
bibles = []

file = open("bible.json", "r")
json_data = json.load(file)

def getTranslation(book, chapter, verse, word):
    versions = {}
    versions["kjv"] = word
    return versions;

def searchBible(topic):
    bible = json_data["bible"]
    matchFound = []
    for item in bible:
        if topic in item["word"]:
            book = item["book"]
            chapter = item["chapter"]
            verse = item["verse"]
            word = getTranslation(book, chapter, verse, item["word"])
            # print(book+str(chapter)+str(verse)+word)
            newitem = {"book": book, "chapter": int(chapter), "verse": int(verse), "word":word}
            matchFound.append(newitem)
    return matchFound


filename = "../html/topics2.json"
data = {"topics": {}, "topiclist": []}

f = open(filename, "r")
topicsjson = json.load(f)

for item in topicsjson["topics"]:
    topic = item["name"]
    if topic in data["topiclist"]:
       print("already exists")
    else:
      versesFound = searchBible(topic)
      data["topics"][topic] = {}
      data["topics"][topic]["verses"] = []
      data["topics"][topic]["verses"] = versesFound
      data["topiclist"].append(topic)
      print(topic + " " + "added")
    data["topiclist"].sort()


with open(filename, 'w') as outfile:
    json.dump(data, outfile)
"""
with open(github, 'w') as outfile:
    json.dump(data, outfile)
"""