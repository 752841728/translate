import requests
import json
from tkinter import *

# 有道翻译反爬虫，需要去掉 url 里的 "_o"
url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"

Headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
}

# *args绑定回车事件
def translate(*args):
    # 删除输出框中的内容
    text_output.delete(1.0, END)
    # 获取输入框中的字符串
    Data = {
        "i": input_tk.get(),
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
    # 爬虫
    html = requests.post(url,headers=Headers,data=Data)
    res = json.loads(html.text)
    res = res['translateResult'][0][0]['tgt']
    # 翻译内容
    text_output.insert(END,res)

'''
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
'''

# 界面
root_login = Tk()               # 创建窗口
root_login.title('中英翻译')    # 窗口标题
root_login['width'] = 310       # 窗口宽度
root_login['height'] = 205      # 窗口高度
root_login.resizable(0, 0)      # 不允许修改窗口大小

# 输入框
label_input = Label(root_login,text="输入:")
label_input.place(x=10, y=5, width=30, height=30)

input_tk = StringVar()          # 定义参数，获取输入框中的内容
entry_input = Entry(root_login, font=("Garamond",10), textvariable=input_tk)
entry_input.place(x=5, y=40, width=300, height=30)

# 输出框
label_output = Label(root_login,text="输出:")
label_output.place(x=10, y=75, width=30, height=30)

text_output = Text(root_login, font=("Garamond",10), pady=7)
text_output.place(x=5, y=110, width=300, height=30)

# 翻译按钮
# photo_login_button = PhotoImage(file="photo_login_button.png")
root_login.bind('<Return>', translate)      # 回车绑定翻译按钮
button_login = Button(root_login, text='翻译', command=translate, compound="center")
button_login.place(x=95, y=160, width=120, height=30)

root_login.mainloop()
