# _*_ coding: utf-8 _*_
"""
@Time : 2022/3/17 15:53
@Author : 薛定谔的余项
@Description : 加密
"""
import hashlib
import uuid


def pwd(txt):
    # 设置秘钥，防止被破解
    secret_key="@fefregt4%3*^"
    md5=hashlib.md5()
    md5.update(txt.encode("utf-8"))
    md5.update(secret_key.encode("utf-8"))
    return md5.hexdigest()

if __name__ == '__main__':
    print(uuid.uuid4().hex)
    # print(pwd("imu"))
