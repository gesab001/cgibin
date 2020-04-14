import cgi
form = cgi.FieldStorage()
url =  form.getvalue('url')
book  = form.getvalue('book')
chapter = form.getvalue('chapter')
verse = form.getvalue('verse')

#import os
from subprocess import call
#url = raw_input("url: ")
#book = raw_input("book: ")
#chapter = raw_input("chapter: ")
#verse = raw_input("verse: ")
filename = book + "_" + chapter + "_" + verse + ".jpg"
call(["curl", url, "--output", filename])
#result = os.popen("curl http://www.henrymorris3.com/wp-content/uploads/2016/08/In-the-Beginning-God-Created.jpg")
#print(result)
#with open('genesis.jpg', 'w') as outfile:
#    outfile.write(str(result))

import mysql.connector
#from subprocess import call
#call(["ls", "-l"])

mydb = mysql.connector.connect(
  host="localhost",
  user="gesab001",
  passwd="ch5t8k4u",
  database="bible"
)

mycursor = mydb.cursor()

#sql ="INSERT INTO memoryVerse(book, chapter, verse, word) select book, chapter, verse, word from kjv where book=%s and chapter=%s and verse=%s"
#val = (book, chapter, verse)
#mycursor.execute(sql, val)
#mydb.commit()

sql ="UPDATE kjv set image=%s where book=%s and chapter=%s and verse=%s"
val = (filename,book,chapter,verse)
mycursor.execute(sql, val)
mydb.commit()

