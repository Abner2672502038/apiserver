# _*_ coding: utf-8 _*_
"""
@Time : 2022/3/8 9:46
@Author : 薛定谔的余项
@Description : 
"""
from flask import Flask
from flask_cors import CORS

import settings
# 创建flask对象
app=Flask(__name__)
app.config.from_object(settings.Dev)

# 解决跨域问题
CORS.__init__(app)

# 初始化db
from models import db
db.init_app(app)



