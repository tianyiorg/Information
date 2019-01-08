# 登陆注册得相关业务逻辑都放在当前模块
from flask import Blueprint

passport_blue = Blueprint("passport", __name__,url_prefix="/passport")

from . import views
