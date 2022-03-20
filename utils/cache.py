# _*_ coding: utf-8 _*_
"""
@Time : 2022/3/18 11:45
@Author : 薛定谔的余项
@Description : redis缓存API
"""
from utils import redis


def create_token(token,user_id):
    redis.set(token,user_id)
    redis.expire(token,time=3*24*3600)

def get_token_userId(token):
    return redis.get(token)

def delete_token(token):
    redis.delete(token)



