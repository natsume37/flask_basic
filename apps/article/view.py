# coding:utf-8
# USER: 冷不丁
# @FILE_NAME: view
# @TIME: 2023/9/22 09:03
from flask import Blueprint

# 实例化蓝图
article_bp = Blueprint('article', __name__)
user_bp = Blueprint('user', __name__, template_folder='../templates', static_folder='../static')


@article_bp.route("/about")
def about_me():
    return "natsume"
