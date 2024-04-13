import os
import bs4
import requests


def post_download(url):
    print("url:", url)
    # url =" https://www.ptt.cc/bbs/Beauty/M.1698672037.A.9
    dirname = os.path.join("beauty", url.split("/")[-1])
    if not os.path.exists(dirname):
        os.makedirs(dirname)
    c = {"over18": "1"}
    h = {

        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"

    }
    response = requests.get(url, cookies=c)
    html = bs4.BeautifulSoup(response.text, "html.parser")
    reserved = ["jpg", "jpeg", "png", "gif"]
    links = html.find_all("a")
    for l in links:
        href = l["href"]
        sub = href.split(".")[-1]
        if sub.lower() in reserved:
            print(href)
            fp = os.path.join(dirname, href.split("/")[-1])
            response = requests.get(href, stream=True, headers=h)
            img = response.raw.read()
            f = open(fp, "wb")
            f.write(img)
            f.close()
            print("-" * 30)
