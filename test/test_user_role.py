# _*_ coding: utf-8 _*_
"""
@Time : 2022/3/17 16:04
@Author : 薛定谔的余项
@Description : 
"""
from unittest import TestCase
from mainapp import app
from models.user import User
from models.role import Role
from utils.crypt import pwd
from models import db

class TestUser(TestCase):

    # 方法名以test_开头
    def test_add_user(self):
        app.app_context().push()

        u=User()
        u.name="嘉林"
        u.auth_key=pwd("123456")
        u.nick_name="Host_52Hz"
        db.session.add(u)
        print("add之后user_id:",u.id)
        db.session.commit()
        print("commit之后：",u.id)

    def test_add_role(self):
        app.app_context().push()

        r1=Role(name="超级管理员")
        r2=Role(name="普通用户")
        db.session.add_all((r1,r2))
        db.session.commit()


    def test_user_role(self):
        app.app_context().push()

        user=User.query.get(1)
        admin_role=Role.query.filter(Role.name.__eq__("超级管理员")).one()
        print(user.name,admin_role.name)
        # 将角色对象添加给用户
        user.roles.append(admin_role)
        db.session.commit()




