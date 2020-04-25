#!/usr/bin/python3
from subprocess import call
import cgitb
import cgi
import subprocess
import requests
import re
import json
from datetime import date
from datetime import datetime

#import mysql.connector as conn
cgitb.enable()  
form = cgi.FieldStorage()
  
news = form.getvalue('keyword')
rss = form.getvalue('url')
title = form.getvalue('title')

print("Content-Type: text/html;charset=utf-8")
print ("Content-type:text/html\r\n\r\n")
#news = input("news: " )
#rss = input("rss: " )
print(news)
print(rss)
print(title)


def getYoutubeXML(link):
	x = requests.get(link)
	string = x.text
	match = re.findall(r"channelId\\\":\\\"[a-zA-Z0-9]*\\\"", string)
	split = match[1].split(":")
	id = split[1].replace("\"","")
	id = id.replace("\\", "")
	url = "https://www.youtube.com/feeds/videos.xml?channel_id="+id
	print(url)
	return url
	

if "youtube" in rss:
	rss = getYoutubeXML(rss)
else:
    print("not a youtube link")

headlines_folder = "../html/headlines/"	
f = open(headlines_folder+'news.json')
json_string = f.read()
data = json.loads(json_string)
data[news] = rss
print(data)

with open(headlines_folder+'news.json', 'w') as outfile:
    json.dump(data, outfile)
 
f = open(headlines_folder+'newstitles.json')
json_string = f.read()
data = json.loads(json_string)
data[news] = title
print(data)
 
with open(headlines_folder+'newstitles.json', 'w') as outfile:
    json.dump(data, outfile)


f = open(headlines_folder+"news.json")
json_string = f.read()
rss = json.loads(json_string)
for news in rss:
   url= rss[news]
   print(url)
   try:
    command = "curl -L '" + url + "' -o " + headlines_folder+news + ".xml"
    subprocess.call(command, shell=True)
   
    print(news+".xml saved successfully" )
   except Exception as ex:
    print(ex)


# datetime object containing current date and time
now = datetime.now()
 
#print("now =", now)

# dd/mm/YY H:M:S
#time_string = now.strftime("%H:%M:%S")
#print("date and time =", dt_string)	
date_string = now.strftime("%A, %B %d %Y %r")
print(date_string)
#date=str(date_string)
#day, month, year = date.split(' ')     
#day_name = datetime.date(int(year), int(month), int(day)) 
#print(day_name.strftime("%A")) 

#today = date.today()
# Textual month, day and year	
#d2 = today.strftime("%B %d, %Y")
#print("d2 =", d2)

command = "echo " + str(date_string) + " NZ" + " >"+headlines_folder+"lastNewsUpdate.txt"
subprocess.call(command, shell=True) 



command = "./gitupdater.sh"
subprocess.call(command, shell=True)
