#!/usr/bin/python3
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
   
hangmanfolder = "../html/reading/hangman/"
name = form.getvalue('name')
url = form.getvalue('url')
imagename = name.replace(" ", "")
filepath = "./images/"+imagename+".jpg"
 
print("Content-Type: text/html;charset=utf-8")
print ("Content-type:text/html\r\n\r\n")
def addPrize(name, url):
	f = open(hangmanfolder+'prizes.json')
	json_string = f.read()
	data = json.loads(json_string)
	data[name] = url
	print(data)
	print("total prizes: " + str(len(data)))

	with open(hangmanfolder+'prizes.json', 'w') as outfile:
		json.dump(data, outfile)
		
 
def downloadimage(filepath,url):
  command = "curl -L " + url + " -o " + hangmanfolder+filepath
  subprocess.call(command, shell=True)
  print("<img width='100px' src='/reading/hangman/"+filepath+"'/img>")

addPrize(name, filepath )
downloadimage(filepath, url)




