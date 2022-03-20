# _*_ coding: utf-8 _*_
"""
@Time : 2022/3/8 9:49
@Author : 薛定谔的余项
@Description : 
"""
from redis import Redis

# 设置redis
# decode_responses=True redis拿到的数据是字节码，需要解码
redis=Redis(host="127.0.0.1",port=6379,db=8,decode_responses=True)
