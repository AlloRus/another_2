from flask import Flask, url_for, request, render_template, redirect
from loginform import LoginForm

application = Flask(__name__)
application.config["SECRET_KEY"] = "yandex_123"


@application.route("/")
def index():
    param = {"title": "Title template"}
    return render_template("mars_1.html", **param)


if __name__ == "__main__":
    application.run(port=8080, host="127.0.0.1")
