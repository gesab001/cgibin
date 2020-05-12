import json


filename = "../html/topics2.json"

data = {}
f = open(filename, "r")
topicsjson = json.load(f)
print (topicsjson["topiclist"])
for topic in topicsjson["topiclist"]:
    json_data = {}
    json_data[topic] = topicsjson["topics"][topic]
    f = open("../html/bibletopics/"+topic+"-topic.json", "w")
    f.write(json.dumps(json_data))
    f.close()

