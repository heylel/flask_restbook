from flask import Blueprint

__author__ = "gaowenfeng"


web = Blueprint('web', __name__)

# 在这里导入不同文件，完成视图函数的注册
from app.web import book
from app.web import user
