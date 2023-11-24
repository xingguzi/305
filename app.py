#!/usr/bin/python3
#encoding: utf-8
'''
@File    :   test_app.py
@Time    :   2022/06/09 10:58:49
@Author  :   bzw
@Version :   1.0
@Contact :   3082723151A@qq.com
@WebSite :
'''
# Start typing your code from here

# from crypt import methods
from asyncio.log import logger
from cgitb import handler
from flask import Flask, render_template, flash, request, abort, redirect, url_for
# from models import User
#导入数据库操作工具类
from mysqlUtils import MysqlUtils
from PON_MysqlUtils import PON_MysqlUtils
#导入json包
import json
#导入日志
import logging
from logging.handlers import TimedRotatingFileHandler
from logging.handlers import SMTPHandler

#MVC模式model层
from booksystem_models.readerModel import readerModel
from booksystem_models.recordModel import recordModel
from booksystem_models.bookModel import bookModel
from booksystem_models.PON_Script_Model import PON_Script_Model
from telnet_test.excel分析.excel分析02 import convert2json
import xlrd

util = MysqlUtils('localhost', 'root', 'QAZplm86327169', 'library', 'utf8')
util2 = PON_MysqlUtils('localhost', 'root', 'QAZplm86327169', 'wczx_hlw', 'utf8')
#所有书籍信息
# u=util.query_all_book()

app = Flask(__name__)
app.secret_key = '123'  #flash加密
# app.config['SERVER_NAME'] = '192.168.1.1:5000'

@app.route('/')
def hello_world():
    flash("")  # 登陆注册提示信息
    content = "hello world"
    # return render_template("login.html", content=content)
    return render_template("login.html", content=content)


# 注册
@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == "POST":
        form = request.form
        username = form.get('username')
        password = form.get('password')
        password2 = form.get('password2')
        # 前端完成判断内容是否为空
        if not username:
            flash("请输入用户名")
            return render_template("register.html")
        if not password:
            flash("请输入密码")
            return render_template("register.html")
        if not password2:
            flash("请输入确认密码")
            return render_template("register.html")
        if not password == password2:
            flash("两次密码不一致")
            app.logger.warning('两次密码不一致'+username+':'+password+'!='+password2)
            return render_template("register.html")
        else:  # 注册信息无误，写入数据库
            util.register_Admin(username, password)
            flash("注册成功")
            app.logger.info('注册成功'+username+';'+password)
            return render_template("register.html")
    else:
        return render_template("register.html")
'''
    else:
        app.logger.warning('注册失败' + username + ';' + password)
        return render_template("register.html")
'''

#返回登录
@app.route('/backlogin', methods=['POST', 'GET'])
def backlogin():
    return render_template('login.html')


#返回注册
@app.route('/backregister', methods=['POST', 'GET'])
def backregister():
    return render_template('register.html')


# 登录界面路由
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        form = request.form
        username = form.get('username')
        password = form.get('password')
        if not username:
            flash("请输入用户名")
            return render_template("login.html", password=password)
        if not password:
            flash("请输入密码")
            return render_template("login.html", username=username)
        password2 = util.query_Password(username)  # 根据账号查询的密码
        if (password == password2):
            app.logger.info('登录成功'+username+';'+password)
            return render_template("addbook.html")
        else:
            flash("用户名或密码错误")
            app.logger.error('尝试登录失败'+username+';'+password)
            return render_template("login.html",
                                   username=username,
                                   password=password)
    else:  #请求方式为GET时
        return render_template("login.html")
        # if username == '123' and password == '123':
        #     flash("登录成功")
        #     # 默认显示为查询页面
        #     return render_template("addbook.html")
        #     # 先设置为跳转至百度
        #     # return redirect("http://www.baidu.com")


# util.add_book(number,name,author,publicationdate,location,remark)
# 增加书籍界面 # number ,name,author,publicationdate,location ,remark
@app.route('/addbook', methods=['POST', 'GET'])
def addbook():
    if request.method == "POST":
        form = request.form
        number = form.get('number') + ""
        name = form.get('bookname') + ""
        author = form.get('author') + ""
        publicationdate = form.get('pdate') + ""
        location = form.get('address') + ""
        remark = form.get('description') + ""
        if not number:
            flash("请输入id")
            return render_template("addbook.html", number=number)
        if not name:
            flash("请输入书名")
            return render_template("addbook.html", number=number, name=name)
        if not location:
            flash("请输入位置")
            return render_template("addbook.html",
                                   number=number,
                                   name=name,
                                   location=location)
        m = bookModel()
        m.add_book(number, name, author, publicationdate, location, remark)
        flash("添加图书成功")
        app.logger.info('添加图书成功:'+number)
        return render_template("addbook.html")
    else:
        return render_template("addbook.html")


# 删除书籍界面
@app.route('/deletebook', methods=['GET', 'POST'])
def deletebook():
    # u = util.query_all_book()
    #MVC模式重构
    m = bookModel()
    books = m.get_all_book_data()
    return render_template("deletebook.html", books=books)


#负责删除书籍的路由 带参数：书籍名称
@app.route('/deletebook2/<bookid>', methods=['GET'])
def deletebook2(bookid):
    #先删除所选书籍后查询
    # util.delete_book(bookid)
    # u = util.query_all_book()
    # MVC模式重构
    m = bookModel()
    m.delete_one_book_by_id(bookid)
    books = m.get_all_book_data()
    flash(bookid)
    app.logger.info('删除书籍成功:'+bookid)
    return render_template("deletebook.html", books=books)


# 修改书籍界面
@app.route('/changebook', methods=['POST', 'GET'])
def changebook():
    # u = util.query_all_book()
    # MVC模式重构
    m = bookModel()
    books = m.get_all_book_data()
    return render_template("changebook.html", books=books)


# 修改书籍界面 详细界面
@app.route('/changebookinfor/<bookid>', methods=['POST', 'GET'])
def changebookinfor(bookid):
    detail = util.query_one_book_byid(bookid)
    if request.method == "POST":
        form = request.form  # 若点击修改 则先删除 后添加
        number = form.get('number') + ""
        name = form.get('bookname') + ""
        author = form.get('author') + ""
        publicationdate = form.get('pdate') + ""
        location = form.get('address') + ""
        remark = form.get('description') + ""
        if not number:
            flash("请输入id")
            return render_template("changebookinfor.html")
        if not name:
            flash("请输入书名")
            return render_template("changebookinfor.html", number=number)
        if not location:
            flash("请输入位置")
            return render_template("changebookinfor.html",
                                   number=number,
                                   name=name)
        util.delete_book(bookid)
        util.add_book(number, name, author, publicationdate, location, remark)
        flash("修改图书成功")
        app.logger.info('修改图书成功:'+bookid)
        return render_template("changebookinfor.html", detail=detail)
    else:
        # app.logger.error('修改图书失败:'+bookid)
        return render_template("changebookinfor.html", detail=detail)


# 查询界面
@app.route('/querybook', methods=['POST', 'GET'])
def querybook():
    #operters 为设备可选操作项
    operters = ['关闭光猫','2','3']
    p = PON_Script_Model()
    PON_data = p.get_all_PON_Script_data()
    if request.method == "POST":
        IP = request.values.get('IP')
        #operter 为选择了的操作项
        operter = request.form.get('os')
        #模糊查询模式
        PON_data = p.get_vague_PON_Script_data(IP)
        file = request.files.get('file')
        if file is None:
            print('文件上传失败')
        else:
            f = file.read()
            clinic_file = xlrd.open_workbook(file_contents=f)
            # sheet1
            table = clinic_file.sheet_by_index(0)
            nrows = table.nrows
            for i in range(1, nrows):
                row_date = table.row_values(i)
                print(row_date)
            print('文件上传成功')
        #精准查询模式-------------------------------------------------------------------------------
        #PON_data = p.get_one_PON_Script_data(IP)
        #============================================================================================
        return render_template("querybook.html", datas=PON_data,operters = operters)
    else:
        return render_template("querybook.html", datas=PON_data,operters = operters)


#图书借阅信息界面
@app.route('/borrowrecord', methods=['POST', 'GET'])
def borrowrecord():
    # u = util.query_borrowrecord()
    # MVC模式重构
    m = recordModel()
    records = m.get_record_data()
    return render_template("borrowrecord.html", records=records)


#读者信息信息界面
@app.route('/readerinfor', methods=['POST', 'GET'])
def readerinfor():
    # u = util.query_readerinfor()
    #MVC模式重构
    m = readerModel()
    readers = m.get_reader_data()
    return render_template("readerinfor.html", readers=readers)


# 错误界面（异常处理）
@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")


if __name__ == '__main__':
    # handler = logging.FileHandler('flask.log')
    # handler = RotatingFileHandler('/SoftwareTest/booksystem/flask.log',
    #                               maxBytes=1024000,
    #                               backupCount=25)
    #时间划分日志
    formatter = logging.Formatter(
        "[%(asctime)s][%(filename)s:%(lineno)d][%(levelname)s][%(thread)d] - %(message)s"
    )
    handler = TimedRotatingFileHandler("log/falsk.log",
                                       when="D",
                                       interval=1,
                                       backupCount=15,
                                       encoding="UTF-8",
                                       delay=False,
                                       utc=True)
    app.logger.addHandler(handler)
    handler.setFormatter(formatter)
    # Email Handler
    # 针对error日志发送邮件
    mail_handler = SMTPHandler(
        mailhost=('smtp.163.com', 25),
        fromaddr='flaskbooksystem@163.com',
        toaddrs='820310027@qq.com',
        subject='User Loggin Error',
        credentials=('flaskbooksystem@163.com', 'OVGQVQRVGGMGBPID')
    )
    mail_handler.setLevel(logging.ERROR)
    mail_handler.setFormatter(logging.Formatter(
        "[%(asctime)s][%(module)s:%(lineno)d][%(levelname)s][%(thread)d] - %(message)s"
    ))
    app.logger.addHandler(mail_handler)
    app.run(host = "127.0.0.1", port = 5000,debug=None,load_dotenv=True)
