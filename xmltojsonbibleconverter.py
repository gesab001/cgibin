import json
import xml.etree.ElementTree as ET
# parse an xml file by name

tree = ET.parse('../html/bibleapi/Bible_Cebuano.xml')
bible = tree.getroot()
bibleversion = bible.get("biblename")
json_data = {"version_ref": bibleversion, "version": {}}
for book in bible:
    bookname = book.get("bname")
    booknumber = book.get("bnumber")
    json_data["version"][booknumber] = {"book_name": bookname, "book_nr": booknumber, "book": {}}
    for chapter in book:
        chapternumber = chapter.get("cnumber")
        json_data["version"][booknumber]["book"][chapternumber] = {"chapter_nr": int(chapternumber), "chapter": {}}
        for verse in chapter:
            versenumber = verse.get("vnumber")
            json_data["version"][booknumber]["book"][chapternumber]["chapter"][versenumber] = {"verse_nr": int(versenumber), "verse" : verse.text}

print(json_data)



with open("../html/bibleapi/"+bibleversion.lower()+"-version.json", "w") as outfile:
    json.dump(json_data, outfile)