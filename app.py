from flask import Flask, render_template
from flask_bootstrap import Bootstrap4

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
