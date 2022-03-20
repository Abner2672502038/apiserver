# _*_ coding: utf-8 _*_
"""
@Time : 2022/3/8 11:04
@Author : 薛定谔的余项
@Description : 
"""
import os

PROJECT_DIR=os.path.dirname(os.path.abspath(__file__))
Base_DIR=os.path.join(PROJECT_DIR,"mainapp")
STATIC_DIR=os.path.join(Base_DIR,"static")
USERIMGS_DIR=os.path.join(STATIC_DIR,"imgs/user")
class Dev():
    ENV="development"
    DEBUG=True
    # sqlalchemy的配置
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:Abner@127.0.0.1:3306/edu'
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    SQLALCHEMY_COMMIT_ON_TEARDOWN=True
    SQLALCHEMY_ECHO=True
