#!/usr/bin/python3
import subprocess
from subprocess import call
import cgitb
import cgi
import json
import string
import re
import datetime

cgitb.enable()

print("Content-Type: text/html;charset=utf-8")
print ("Content-type:text/html\r\n\r\n")


# # Create instance of FieldStorage
form = cgi.FieldStorage()
#
# # Get data from fields
# #first_name = form.getvalue('first_name')
# #last_name  = form.getvalue('last_name')

title = form.getvalue('title')
filename = form.getvalue('filename')
caption = form.getvalue('caption')
book = form.getvalue('book')
chapter = (form.getvalue('chapter'))
verse = form.getvalue('verse')
word = ""

print ("title: " + title)
print("<br>")
print ("filename: " + filename)
print("<br>")
print ("caption: " + caption)
print("<br>")
print ("book: " + book)
print("<br>")
print ("chapter: " + chapter)
print("<br>")
print ("verse: " + verse)
print ("<br>")
print ("<img src='../pictures/"+title.lower()+"/"+filename+"'>")
f = open("bible.json", "r")
jsonString = f.read()
bibleJson = json.loads(jsonString)
bible = bibleJson["bible"]
for item in bible:
   if item["book"]==book:
      if int(item["chapter"])==int(chapter):
           if int(item["verse"])==int(verse):
               word = item["word"]
print("<br>")
print ("word: " + word)

path = "../html/story.onecloudapps.net/"+title.lower()+"/imagedata.json"
f = open(path)
jsonString = f.read()
imageJson = json.loads(jsonString)
newJsonData = {"title": title, "filename": filename, "caption": caption, "bible": {"book": book, "chapter": chapter, "verse": int(verse)}}
imageJson["slides"].append(newJsonData)
f.close()
with open(path, 'w') as outfile:
    json.dump(imageJson, outfile)

print ("<form action='../story.onecloudapps.net/index.php' method='post'>")
print ("<input type='hidden' name='title' value='"+title+"'/>")
print ("<input type='submit' value='go back'/>")
print ("</form>")
