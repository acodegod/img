import re

list = []
with open("img.txt", "r", encoding="utf-8") as urls:
    for urls in urls.readlines():
        urls_path = re.findall('https://girls-1258640085.cos.ap-chengdu.myqcloud.com/(.*?)/.*', urls)[0]
        with open("{}.txt".format(urls_path), "a", encoding="utf-8") as addd:
            addd.write(urls)



