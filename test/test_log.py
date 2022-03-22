# _*_ coding: utf-8 _*_
"""
@Time : 2022/3/21 18:11
@Author : 薛定谔的余项
@Description : 测试日志
"""
import logging
# 导入日志处理器
import os
from logging import StreamHandler,FileHandler
from logging.handlers import HTTPHandler,SMTPHandler

# 格式化
from logging import Formatter

import settings
logger=logging.getLogger("apiserver_log")
class cofig_log():

    # 定义格式化的
    formatter= Formatter(fmt="%(asctime)s %(name)s %(levelname)s: %(message)s",datefmt="%Y-%m-%d %H:%M:%S")

    iohandler=StreamHandler()
    iohandler.setFormatter(formatter)
    iohandler.setLevel(logging.DEBUG)

    filehanler=FileHandler(os.path.join(settings.PROJECT_DIR,"apiserver.log"))
    filehanler.setFormatter(formatter)
    filehanler.setLevel(logging.WARNING)

    httphandler=HTTPHandler(host="localhost:5000",url="/log/upload",method="POST")
    httphandler.setFormatter(formatter)
    httphandler.setLevel(logging.ERROR)


    logger.addHandler(iohandler)
    logger.addHandler(filehanler)
    logger.addHandler(httphandler)
    logger.setLevel(logging.DEBUG)

cofig_log()
logger.debug("debug信息")
logger.info("info信息")
logger.warning("warning信息")
logger.error("error信息")
logger.critical("严重错误信息")
print(os.path.join(settings.PROJECT_DIR,"apiserver.log"))
