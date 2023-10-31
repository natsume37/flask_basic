# coding:utf-8
# USER: 冷不丁
# @FILE_NAME: user
# @TIME: 2023/10/31 19:13
from userLlist import *


class User:
    def __init__(self, user, password):
        self.user = user
        self.password = password

    @staticmethod
    def save_list(user, password):
        return UserList.add_user(user, password)
