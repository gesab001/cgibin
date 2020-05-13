import json

f = open("../html/topics2.json", "r")
jsonbible = json.load(f)
topics = jsonbible["topics"]
del topics["immoral"]
data = {}
for title in topics:
    data[title] = []
    verses = topics[title]["verses"]
    for x in range(0, len(verses)):
      book = topics[title]["verses"][x]["book"]
      chapter  = topics[title]["verses"][x]["chapter"]
      verse = topics[title]["verses"][x]["verse"]
      word = topics[title]["verses"][x]["word"]["kjv"]
      jsonitem = {"book": book, "chapter": int(chapter), "verse": int(verse), "word": word }
      data[title].append(jsonitem)

with open("../html/topics3.json", "w") as outfile:
    json.dump(data, outfile)