import requests

URL = "https://rss.nzherald.co.nz/rss/xml/nzhtsrsscid_000000698.xml"

response = requests.get(URL)
try:
 with open('../html/headlines.onecloudapps.net/nzherald.xml', 'wb') as file:
    file.write(response.content)
except Exception as ex:
    print(ex)
