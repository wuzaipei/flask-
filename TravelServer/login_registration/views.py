from flask import Blueprint

login_register = Blueprint("login",__name__)

@login_register.route("/login")
def data_page():
    return "你好吗！"
