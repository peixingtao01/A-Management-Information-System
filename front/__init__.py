# 2
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
import pymysql
pymysql.install_as_MySQLdb()

csrfya = CSRFProtect()
models = SQLAlchemy()

# 蓝图
from flask import Blueprint
main = Blueprint('main',__name__)
from . import views

def create_front():
    fronts = Flask(__name__)
    fronts.config.from_object("config.DebugConfig")
    csrfya.init_app(fronts)
    models.init_app(fronts)
    fronts.register_blueprint(main)
    return fronts