from system.app import app

# 配置路由,总路由
from homePage.views import homePage
from login_registration.views import login_register

app.register_blueprint(login_register,url_prefix="/login_register")
app.register_blueprint(homePage,url_prefix="/homePage")
