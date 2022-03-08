# _*_ coding: utf-8 _*_
"""
@Time : 2022/3/8 11:04
@Author : 薛定谔的余项
@Description : 
"""
class Dev():
    ENV="development"
    DEBUG=True
    # sqlalchemy的配置
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:Abner@127.0.0.1:3306/edu'
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    SQLALCHEMY_COMMIT_ON_TEARDOWN=True
    SQLALCHEMY_ECHO=True
