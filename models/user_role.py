# _*_ coding: utf-8 _*_
"""
@Time : 2022/3/17 15:43
@Author : 薛定谔的余项
@Description : 
"""
from models import db
from sqlalchemy import Table,Integer,Column,ForeignKey

# 模型之间的关系不需要创建第三个模型类来实现第三张关系表创建
# 创建user和role之间的关系表
user_role=db.Table("user_role",
                Column("user_id",Integer,ForeignKey("user.id")),
                Column("role_id",Integer,ForeignKey('role.id')))

