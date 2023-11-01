from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap4
from user import *
from userLlist import *
from settings import logger
from songs import *
from func_list import *
app = Flask(__name__)
# app.config.from_object(settings)
bootstrap = Bootstrap4(app)


@app.route('/')
def index():  # put application's code here
    fire_songs = songs(urls_dic["新歌榜"])
    biaos = songs(urls_dic["飙升榜"])
    yuans = songs(urls_dic["原创榜"])

    return render_template("index.html", **locals())
    # return "你好"


@app.route('/login')
def login():
    return render_template('logo_re.html')


@app.route('/login/egypt', methods=['POST', "GET"])
def login_egypt():
    if request.method == 'POST':
        name = request.form.get("username")
        password = request.form.get("password")
        res = is_yz(name, password)
        print(name, password)
        print(res, user_list)
        if res[0]:
            return redirect(url_for('index'))
        else:
            return redirect(url_for('login'))


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/register/egypt', methods=['POST', "GET"])
def user_add():
    if request.method == 'POST':
        name = request.form.get("username")
        password = request.form.get("password")
        print(name, password, "user_add")
        user = User(name, password)
        res = user.save_list(name, password)
        if res[0]:
            logger.debug("注册成功！")
            return redirect(url_for('login'))
        else:
            return redirect(url_for('register'))


# @app.route("/search/<music_name>")
# def search_music(music_name):



if __name__ == '__main__':
    app.run()
