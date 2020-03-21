import requests
import json

# 有道翻译反爬虫，需要去掉 url 里的 "_o"
url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"

Headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
}


def translate():
    html = requests.post(url,headers=Headers,data=Data)
    res = json.loads(html.text)
    res = res['translateResult'][0][0]['tgt']
    # print(type(res))
    export = "输出：" + res + "\n"
    print(export)


print("欢迎进入中英翻译（输入'0'退出翻译）")
while 1:
    entry = input("输入：")

    Data = {
        "i": entry,
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": "15846062836902",
        "sign": "fa814046cdda533ac0d4b86f6cb09d17",
        "ts": "1584606283690",
        "bv": "70244e0061db49a9ee62d341c5fed82a",
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_CLICKBUTTION",
    }

    if entry == "0":
        break
    else:
        translate()