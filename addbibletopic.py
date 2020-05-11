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
bibles = ["korean", "tagalog", "maori", "cebuano", "hebrew", "hebrewmodern", "textusreceptus", "greekot"]
versionsdic = {"tagalog": "Tagalog", "korean": "Korean", "maori": "Maori", "cebuano": "Cebuano", "hebrew": "Hebrew", "hebrewmodern": "Modern Hebrew", "textusreceptus": "Greek Textus Receptus", "greekot": "Greek Old Testament"}
jsonbibles = {}
booklist = {"Genesis": "1", "Exodus": "2", "Leviticus": "3", "Numbers": "4", "Deuteronomy": "5", "Joshua": "6", "Judges": "7", "Ruth": "8", "1 Samuel": "9", "2 Samuel": "10", "1 Kings": "11", "2 Kings": "12", "1 Chronicles": "13", "2 Chronicles": "14", "Ezra": "15", "Nehemiah": "16", "Esther": "17", "Job": "18", "Psalms": "19", "Proverbs": "20", "Ecclesiastes": "21", "Song of Solomon": "22", "Isaiah": "23", "Jeremiah": "24", "Lamentations": "25", "Ezekiel": "26", "Daniel": "27", "Hosea": "28", "Joel": "29", "Amos": "30", "Obadiah": "31", "Jonah": "32", "Micah": "33", "Nahum": "34", "Habakkuk": "35", "Zephaniah": "36", "Haggai": "37", "Zechariah": "38", "Malachi": "39", "Matthew": "40", "Mark": "41", "Luke": "42", "John": "43", "Acts (of the Apostles)": "44", "Romans": "45", "1 Corinthians": "46", "2 Corinthians": "47", "Galatians": "48", "Ephesians": "49", "Philippians": "50", "Colossians": "51", "1 Thessalonians": "52", "2 Thessalonians": "53", "1 Timothy": "54", "2 Timothy": "55", "Titus": "56", "Philemon": "57", "Hebrews": "58", "James": "59", "1 Peter": "60", "2 Peter": "61", "1 John": "62", "2 John": "63", "3 John": "64", "Jude": "65", "Revelation": "66"}
for bible in bibles:
    filename = "../html/bibleapi/"+bible+"-version.json"
    file = open(filename, "r")
    json_data = json.load(file)
    jsonbibles[bible] = json_data
file = open("bible.json", "r")
json_data = json.load(file)

def getTranslation(book, chapter, verse, word):
    versions = {}
    versions["kjv"] = word
    booknumber = booklist[book]
    for version in bibles:
        bibledata = jsonbibles[version]
        try:
         translatedword = bibledata["version"][str(booknumber)]["book"][str(chapter)]["chapter"][str(verse)]["verse"]
         versions[version] = translatedword
        except:
         translatedword = "no translation for this version"
         versions[version] = translatedword
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

for topic in topicsjson["topics"]:
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

data["versionslist"] = bibles
data["versionslist"].sort()
data["versionoptions"] = versionsdic
with open(filename, 'w') as outfile:
    json.dump(data, outfile)
"""
with open(github, 'w') as outfile:
    json.dump(data, outfile)
"""