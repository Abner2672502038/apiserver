# _*_ coding: utf-8 _*_
"""
@Time : 2022/3/8 12:55
@Author : 薛定谔的余项
@Description : 
"""
from flask import Blueprint
from flask import request,render_template
blue=Blueprint("userBlue",__name__,url_prefix="/user")

@blue.route("/login",methods=['GET','POST'])
def login():
    print("-------------------------------")
    data={
        "cookies":request.cookies,
        "base_url":request.base_url
    }
    return render_template("user/login.html",**data)