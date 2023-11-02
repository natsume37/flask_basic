from flask import Flask, render_template, request, redirect, url_for, jsonify,flash
from flask_bootstrap import Bootstrap4
from user import *
from userLlist import *
from settings import logger
from songs import *
from func_list import *

app = Flask(__name__)
app.secret_key = 'natsume37'
# app.config.from_object(settings)
bootstrap = Bootstrap4(app)


@app.route('/')
def index():  # put application's code here
    fire_songs = songs(url=urls_dic["热歌榜"])
    biaos = songs(url=urls_dic["飙升榜"])
    yuans = songs(url=urls_dic["新歌榜"])
    return render_template("index.html", fire_songs=fire_songs, biaos=biaos, yuans=yuans)
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

        if res[0]:
            return redirect(url_for('index'))
        else:
            flash("用户名或密码错误请重新登录！")
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
            flash("注册成功")
            return redirect(url_for('login'))
        else:
            flash("注册失败、该用户名已注册")
            return redirect(url_for('register'))


@app.route("/search/<music_name>")
def search_music(music_name):
    songs = clean_json(music_name)
    return render_template('search.html', **locals())


# @app.route("/search/<music_name>")
# def search_music(music_name):
#     songs = clean_json(music_name)
#     return render_template('search.html', **locals())

@app.route("/fire")
def fire():
    fire_songs = songs(url=urls_dic["热歌榜"],)
    biaos = songs(url=urls_dic["飙升榜"])
    yuans = songs(url=urls_dic["新歌榜"])

    return render_template("fire_file.html", fire_songs=fire_songs, biaos=biaos, yuans=yuans)


if __name__ == '__main__':
    app.run()
