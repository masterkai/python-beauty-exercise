# import random
#
# print(1+1)
# list = ["孝","子","博","漢"]
#
# index = random.randint(0,len(list)-1)
#
# print(list[index])

import bs4
import requests
from beauty import post_download

url = "https://www.ptt.cc/bbs/Beauty/index.html"
c = {
    "over18": "1"
}
response = requests.get(url, cookies=c)
html = bs4.BeautifulSoup(response.text, "html.parser")
# print(html)
posts = html.find_all("div", {"class": "title"})

for post in posts:
    link = post.find("a")
    if not link == None:
        href = "https://www.ptt.cc" + link["href"]
        print(href)
        post_download(href)

