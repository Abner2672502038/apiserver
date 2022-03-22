# _*_ coding: utf-8 _*_
"""
@Time : 2022/3/8 9:46
@Author : 薛定谔的余项
@Description : 
"""
import logging
import os
from logging import Formatter, StreamHandler, FileHandler
from logging.handlers import HTTPHandler

from flask import Flask
from flask_cors import CORS
from  flask.logging import default_handler

import settings
# 创建flask对象
app=Flask(__name__)
app.config.from_object(settings.Dev)


app.logger.removeHandler(default_handler)
app.logger.setLevel(logging.INFO)

# 定义格式化的
formatter = Formatter(fmt="%(asctime)s %(name)s %(levelname)s: %(message)s", datefmt="%Y-%m-%d %H:%M:%S")

iohandler = StreamHandler()
iohandler.setFormatter(formatter)
iohandler.setLevel(logging.INFO)
app.logger.addHandler(iohandler)

filehanler = FileHandler("apiserver_log",encoding='UTF-8')
filehanler.setFormatter(formatter)
filehanler.setLevel(logging.WARNING)
app.logger.addHandler(filehanler)
#
httphandler = HTTPHandler(host="127.0.0.1:5000", url="/log/upload", method="POST")
httphandler.setLevel(logging.CRITICAL)
# 配置日志处理器
app.logger.addHandler(httphandler)


# 解决跨域问题
CORS.__init__(app)

# 初始化db
from models import db
db.init_app(app)



