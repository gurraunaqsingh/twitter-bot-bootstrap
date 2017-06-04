import requests
import json

api_url = "http://40.media.tumblr.com/9a8853151648a911fd09735c2d6a61b5/tumblr_n48rj4W4AS1qz6pqio1_1280.png"

req = requests.get(api_url)
content = req.text

data = json.loads(content)

filename = 'temp.jpg'
request = requests.get(api_url, stream=True)
if request.status_code == 200:
    with open(filename, 'wb') as image:
        for chunk in request:
            image.write(chunk)
else:
    print("Unable to download image")

# print("content : " + data['content'])
# print("picture_url : " + data['picture_url'])
# print("Author : " + data['author']['name'])
# print(type((data)))