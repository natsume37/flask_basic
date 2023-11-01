# coding:utf-8
# USER: 冷不丁
# @FILE_NAME: test
# @TIME: 2023/9/21 21:38

import requests
input_user = "十年"
url = f"https://music.163.com/api/search/get?s={input_user}&type=1&limit=3"

res = requests.get(url)
print(res.json())