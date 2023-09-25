from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

import settings

app = Flask(__name__)
# app.config.from_object(settings)
bootstrap = Bootstrap5(app)




@app.route('/')
def hello_world():  # put application's code here
    return render_template("index.html")


@app.route("/get_data", methods=['post'])
def data():
    return "登录成功"

@app.route("/about")
def about():
    return "个人介绍页面"


if __name__ == '__main__':
    app.run()

