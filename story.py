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
chapter = form.getvalue('chapter')
verse = form.getvalue('verse')


print ("title: " + title)
print ("filename: " + filename)
print ("caption: " + caption)
print ("book: " + book)
print ("chapter: " + chapter)
print ("verse: " + verse)

print ("<form action='../story.onecloudapps.net/index.php' method='post'>")
print ("<input type='hidden' name='title' value='"+title+"'/>")
print ("<input type='submit' value='go back'/>")
print ("</form>")
