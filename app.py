from flask import Flask, render_template, request,redirect,url_for
from flask_bootstrap import Bootstrap4
from user import *
from userLlist import *
import settings

app = Flask(__name__)
# app.config.from_object(settings)
bootstrap = Bootstrap4(app)


@app.route('/')
def index():  # put application's code here
    return render_template("index.html")
    # return "你好"


@app.route('/login')
def login():
    return render_template('logo_re.html')


@app.route('/login/egypt', methods=['POST', "GET"])
def login_egypt():
    if request.method == 'POST':
        name = request.form.get("username")
        password = request.form.get("password")
        res = UserList.is_yz(name, password)
        print(name, password)
        print(res, user_list)
        if res[0]:
            return redirect(url_for('index'))
        else:
            return redirect(url_for('login'))


@app.route('/register/egypt', methods=['POST', "GET"])
def user_add():
    if request.method == 'POST':
        name = request.form.get("username")
        password = request.form.get("password")
        bool = UserList.is_user(name)
        if bool:
            return redirect(url_for('register'))
        UserList.add_user(name, password)
        return redirect(url_for('login'))
#TODO 注册事件的BUG、注册完后列表未刷新

@app.route('/register')
def register():
    return render_template('register.html')


@app.route("/get_data", methods=['post'])
def data():
    return "登录成功"


@app.route("/about")
def about():
    return "个人介绍页面"


if __name__ == '__main__':
    app.run()
