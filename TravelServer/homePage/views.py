from flask import Blueprint

homePage = Blueprint("homePage",__name__)

@homePage.route("/micro_sites")
def data_page():
    return "微景点！"