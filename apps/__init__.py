# coding:utf-8
# USER: 冷不丁
# @FILE_NAME: __init__.py
# @TIME: 2023/9/22 09:01
from flask import Flask
from apps.article.view import article_bp

def create_app():
 #设置静态文件夹和模板文件夹的路径
    app=Flask(__name__,template_folder='../templates',static_folder='../static')
    app.register_blueprint(user_bp)  #注册蓝图
    return app    #返回Flask对象