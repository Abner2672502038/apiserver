from mainapp import app
from flask_script import Manager
from  flask import render_template,request,redirect,url_for
from mainapp.views import user, bingdundun, logger
from models.user import db,User
from models.role import Role
from models.access import Access #使用Model创建表时需要声明表，否则创建不成功
from models.user_role import user_role
from utils import cache
from  flask import current_app


@app.before_request
def check_login():
    # app.logger.info(request.path+"被访问")
    # app.logger.error(request.path+"发生错误")
    print("===============================")
    if request.path not in ['/user/login','/log/upload']:
        print("------------------------------------")
        # 验证token有效
        token=request.cookies.get("token")
        if not token:
            return  redirect(url_for("userBlue.login"))
        else:
            user_id=cache.get_token_userId(token)
            if not user_id:
                return redirect(url_for("userBlue.login"))


@app.route('/')
def hello_world():
    current_app.logger.warning("current_app info信息")
    current_app.logger.error("curent_app---error 信息")
    current_app.logger.critical("curent_app----critical信息")

    token=request.cookies.get("token")
    print(token)
    user=User.query.get(int(cache.get_token_userId(token)))


    return render_template("index.html",user=user)

@app.route("/create_db")
def create_db():
    db.create_all()
    return "创建数据库中所用模型表成功"


@app.route("/delete_db")
def delete_db():
    db.drop_all()
    return "删除库中所有模型类对应的表"


if __name__ == '__main__':
    # 注册蓝图
    app.register_blueprint(user.blue)
    app.register_blueprint(bingdundun.blue)
    app.register_blueprint(logger.blue)
    app.run(threaded=True)
    #
    # manager:Manager=Manager(app)
    #
    # manager.run()
