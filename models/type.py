# _*_ coding: utf-8 _*_
"""
@Time : 2022/3/20 18:08
@Author : 薛定谔的余项
@Description : 元类实现ORM
"""
from flask import logging
from  flask import g
# python中的元类
"""
 1.type
 2.meteclass
"""
# class User():
#
#     def test(self,msg):
#         print("hi,%s"%msg)

# 使用元类创建类
# type(classname,parent_class,attrs)
# classname:类名
# parent_class:继承的父类，是一个元组（）
# attrs；类中的属性
def test(self,msg):
         print("hi,%s"%msg)
User=type('User',(),{
    "say":test,
    "hello":lambda self,msg:"请说%s"%msg
})

class BaseFiled():
    pass
class IntFiled(BaseFiled):
    pass
class CharFiled(BaseFiled):
    def __init__(self,len):
        self.length=len


class BaseModelMeta(type):
    def __new__(cls, name,bases,attrs):
        print("---BaseModelMeta---",name)
        print("---BaseModelMeta---",bases)
        print("---BaseModelMeta---",attrs)
        if name=="Model":
             return type.__new__(cls,name,bases,attrs)

        fileds={}
        for key,filed in attrs.items():
            if isinstance(filed,BaseFiled):
                fileds[key]=filed
        table=attrs.get("__tablename",name.lower())
        attrs['fileds']=fileds
        attrs['table']=table
        return type.__new__(cls,name,bases,attrs)


class Model(metaclass=BaseModelMeta):
    def create(self):
        print("__create__")
        sql="create table %s(%s)"
        table_name=self.table
        colums=[ "%s %s"% (key,'varchar(%s)'%filed.length if isinstance(filed,CharFiled) else "Integer") for key ,filed in self.fileds.items()]
        sql=sql%(table_name,','.join(colums))
        print(sql)

    def save(cls):
        pass

    def update(cls):
        pass

    def delete(cls):
        pass

    def query(cls):
        pass

class Person(Model):
    __tablename__="person"
    id=IntFiled()
    name=CharFiled(20)
    city=CharFiled(10)



if __name__ == '__main__':

    # user=User()
    # user.say("pig")
    # print(user.hello("hello"))
    u=Person()
    u.create()



