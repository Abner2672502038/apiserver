# _*_ coding: utf-8 _*_
"""
@Time : 2022/3/21 18:06
@Author : 薛定谔的余项
@Description : 日志上传
"""
from flask import Blueprint, jsonify, request

blue=Blueprint("logerBlue",__name__,url_prefix="/log")

@blue.route("/upload",methods=["POST"])
def log():
    print("------------------------------------")
    print(request.form)
    return jsonify({
        "msg":"日志上传成功"
    })
