import json


filename = "../html/topics2.json"

version = {"topics": {}}
data = {}
f = open(filename, "r")
topicsjson = json.load(f)
print (topicsjson["topiclist"])
versionslist = topicsjson["versionslist"]
print(versionslist)
for version in versionslist:
    for topic in topicsjson["topiclist"]:
        json_data = {"topics": {}}
        json_data["topics"][topic] = {"verses" : []}
        try:
          verses = topicsjson["topics"][topic]["verses"]
          for verse in verses:
              book = verse["book"]
              chapter = verse["chapter"]
              versenumber = verse["verse"]
              json_data["topics"][topic]["verses"].append({"book" : book, "chapter": chapter, "verse": versenumber, "word": {version: verse["word"][version]}})
          f = open("../html/bibletopics/"+version+"-version-" + topic + "-.json", "w")
          f.write(json.dumps(json_data))
          f.close()
        except Exception as ex:
          print(ex)


