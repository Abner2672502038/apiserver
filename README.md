## 一、Flask实现api接口开发
1.创建环境（运行环境 virtualenv、conda）  
```
pip install flask flask-cors flask-blueprint flask-script pymysql flask-sqlalchemy redis
```
2.解决跨域问题 Flask-cors  
3.选择数据库操作框架(自定义dao+SQL SQLALCHEMY+Orm、基于元类自定义Orm)  
4.拆分项目结构(app，dao,utils,manage.py)  
5.数据交互json
   * 前端上传json数据，等待后端响应json数据结果
   * 后端接收json数据，响应  
开发者角色：  
 * 第一次github clone代码
 * 创建项目的运行环境
 * 安装requirements.txt依赖库
 * 启动项目
 * 接收开发需求
 * 任务code开发完成后、本地提交、上传服务器
 * 开发新任务、先更新别人代码
 ## 二、文件上传
 * 文件上传的两种方式：form标签和input的file类型的标签  
 * Ajax的DataForm方式上传文件  
 ### 2.1 表单标签上传
 * form表单的enctype为"multipart/form-data",且method=post
 
 ### 2.2 Ajax文件上传
 
 

 

