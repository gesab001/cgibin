f = open("../html/video.onecloudapps.net/batman-filtered.srt")
text = f.readlines()
f.close()
vtt = "WEBVTT\n\n"
for line in text:

    if "-->" in line:
       line = line.replace(",", ".")
       vtt+= line
    else:
      vtt+= line

f = open("../html/video.onecloudapps.net/batman.vtt", "w")
f.write(vtt)
f.close()