# coding:utf-8
# USER: 冷不丁
# @FILE_NAME: user_list
# @TIME: 2023/10/31 19:13

user_list = {"natsume": "123"}


def is_user(user):
    if user in user_list.keys():
        return True
    return False


def add_user(user, password):
    bool = is_user(user)
    if bool:
        return False, "该用户已注册"
    else:
        user_list[user] = password
        print(user_list, "当前用户列表", user, password)
        return True, "用户添加成功"


def is_yz(user, password):
    bool = is_user(user)
    if bool:
        if password == user_list[user]:
            return True, "登录成功"
        else:
            return False, "用户名或密码错误"
    else:
        return False, "用户名错误"
