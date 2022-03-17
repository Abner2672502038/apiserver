from mainapp import app
from flask_script import Manager
from  flask import render_template
from mainapp.views import user,bingdundun
from models.user import db,User
from models.role import Role
from models.access import Access #使用Model创建表时需要声明表，否则创建不成功
from models.user_role import user_role

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route("/create_db")
def create_db():
    db.create_all()
    return "创建数据库中所用模型表成功"


@app.route("/delete_db")
def delete_db():
    db.drop_all()
    return "删除库中所有模型类对应的表"


if __name__ == '__main__':
    app.register_blueprint(user.blue)
    app.register_blueprint(bingdundun.blue)
    manager=Manager(app)
    manager.run()