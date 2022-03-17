# _*_ coding: utf-8 _*_
"""
@Time : 2022/3/8 9:49
@Author : 薛定谔的余项
@Description : 
"""
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer,Column,String
# 创建db对象
db=SQLAlchemy()

# 基模型
class BaseModel(db.Model):
    __abstract__=True # 不会创建模型对应的表
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(20), unique=True, nullable=False)
