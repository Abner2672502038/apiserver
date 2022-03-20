# _*_ coding: utf-8 _*_
"""
@Time : 2022/3/8 12:55
@Author : 薛定谔的余项
@Description : 
"""
import os
import uuid
from datetime import datetime, timedelta

from werkzeug.datastructures import FileStorage

import settings
from utils import cache

from flask import Blueprint, redirect, jsonify
from flask import request,render_template
from models.user import User
from models import db
from utils.crypt import pwd
blue=Blueprint("userBlue",__name__,url_prefix="/user")

@blue.route("/upload",methods=["POST"])
def upload_profile():
    token=request.cookies.get("token")
    user=User.query.get(int(cache.get_token_userId(token)))

    user_photo:FileStorage=request.files.get("userprofile")
    filename=uuid.uuid4().hex+os.path.splitext(user_photo.filename)[-1]
    filepath=os.path.join(settings.USERIMGS_DIR,filename)
    user_photo.save(filepath)
    # 删除原来的头像
    # 更新数据库
    user.photo="imgs/user/"+filename
    db.session.commit()

    return jsonify({
        "msg":"文件上传成功",
        "path":'imgs/user/'+filename

    })




@blue.route("/modify",methods=["GET","POST"])
def modify():
   #  获取个人信息
   token = request.cookies.get("token")
   user_id=cache.get_token_userId(token)
   #可以把用户保存到缓存中，从缓存中获取
   user=User.query.get(int(user_id))
   msg = ''
   if request.method=="POST":
       upload_file:FileStorage=request.files.get("user_profile")
       print("文件名：",upload_file.filename)
       print("文件大小：",upload_file.content_length)
       print("文件类型：",upload_file.content_type)
       # 文件类型为图片
       if not upload_file.content_type.startswith("image/"):
           msg="上传文件必须是图像"
       else:
           # 修改文件名
           filename=uuid.uuid4().hex+os.path.splitext(upload_file.filename)[-1]
           filepath=os.path.join(settings.USERIMGS_DIR,filename)
           # 保存文件
           upload_file.save(filepath)
           user.photo="imgs/user/"+filename
           db.session.commit()
   return render_template("user/personinfo.html",user=user,msg=msg)


@blue.route("/login",methods=['GET','POST'])
def login():
    # print("-------------------------------")
    # data={
    #     "cookies":request.cookies,
    #     "base_url":request.base_url
    # }
    msg=''
    if request.method=="POST":
        # 获取参数
        phone=request.form.get("phone")
        passwd=request.form.get("pwd")
        # 查询用户
        login_user=db.session.query(User).filter(db.and_(User.name.__eq__(phone),User.auth_key.__eq__(pwd(passwd)))).all()
        if login_user:
            # uuid生成token
            token=uuid.uuid4().hex
            # cookie设置token
            resp=redirect("/")
            resp.set_cookie("token",token,expires=(datetime.now()+timedelta(minutes=30)))
            # redis存放token
            cache.create_token(token,login_user[0].id)
            return  resp
        else:
            msg="用户名或密码错误"

    # ctrl+p弹出日志信息
    return render_template("user/login.html",msg=msg)

@blue.route("/logout")
def logout():
    token=request.cookies.get("token")
    cache.delete_token(token)
    resp=redirect("/user/login")
    resp.delete_cookie("token")
    return resp


