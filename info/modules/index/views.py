from flask import render_template, current_app

from . import index_blue


@index_blue.route('/')
def index():
    return render_template("news/index.html")


@index_blue.route('/favicon.ico')
def favicon():
    return current_app.send_static_file("news/favicon.ico")
