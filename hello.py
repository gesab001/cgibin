#!/usr/bin/python3

import cgitb
import cgi

cgitb.enable()    


print("Content-Type: text/html;charset=utf-8")
print ("Content-type:text/html\r\n\r\n")


def beginning(string):
    list = string.split(" ")
    for x in list:
       print (x)
       print ("<br>")

string = "In the beginning God created the heaven and the earth. Genesis 1:1"
beginning(string)
