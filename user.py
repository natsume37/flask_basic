# coding:utf-8
# USER: 冷不丁
# @FILE_NAME: user
# @TIME: 2023/10/31 19:13
from userLlist import *


class User:
    def __init__(self, user, password):
        self.user = user
        self.password = password

    @classmethod
    def save_list(cls, user, password):
        try:
            return add_user(user, password)
        except Exception as e:
            return False, e
