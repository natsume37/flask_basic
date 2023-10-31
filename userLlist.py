# coding:utf-8
# USER: 冷不丁
# @FILE_NAME: user_list
# @TIME: 2023/10/31 19:13

user_list = {"natsume": "123"}


class UserList:

    @classmethod
    def is_user(cls, user):
        if user in user_list.keys():
            return True
        return False

    @classmethod
    def add_user(cls, user, password):
        bool = cls.is_user(user)
        if bool:
            user_list[user] = password
            return True, "用户添加成功"
        else:
            return False, "该用户已注册"

    @classmethod
    def is_yz(cls, user, password):
        bool = cls.is_user(user)
        if bool:
            if password == user_list[user]:
                return True, "登录成功"
            else:
                return False, "用户名或密码错误"
        else:
            return False, "用户名错误"
