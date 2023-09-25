# coding:utf-8
# USER: 冷不丁
# @FILE_NAME: test
# @TIME: 2023/9/21 21:38

import requests

url = 'http://127.0.0.1:5000/get_data'
res = requests.post(url).text
print(res)