# _*_ coding: utf-8 _*_
"""
@Time : 2022/3/8 11:14
@Author : 薛定谔的余项
@Description : 
"""
from models import db
from sqlalchemy import Integer,String,Column

from models.role import Role
from models.user_role import user_role


class User(db.Model):
    id=Column(Integer,primary_key=True,autoincrement=True)
    name=Column(String(20),unique=True,nullable=False)
    auth_key=Column(String(100),unique=True,nullable=False)
    nick_name=Column(String(20),nullable=True)
    photo=Column(String(100))
    # 设置关联
    roles=db.relationship(Role,secondary=user_role)

