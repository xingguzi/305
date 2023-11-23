# 导入mysql数据库
import pymysql

class PON_MysqlUtils():
    #初始化
    def __init__(self,host,user,password,db,charset):

        self.host=host
        self.user=user
        self.password=password
        self.db=db
        self.charset=charset
        self.conn = pymysql.connect(host=host, user=user, password=password, db=db, charset=charset)
        self.cur = self.conn.cursor()

    # #增加书籍
    def add_book(self,number,name,author,publicationdate,location ,remark):
        sqlstr="insert into book (number,name,author,publicationdate,location ,remark) " \
               "values( '"+number+"','"+name+"','"+author+"','"+publicationdate+"','"+location+"','"+remark+"');"
        self.cur.execute(sqlstr)
        # 涉及写操作要注意提交
        self.conn.commit()

    #删除书籍  根据书籍id删除
    def delete_book(self, bookid):
        sqlstr="delete from book where number = '" + bookid + "';"
        #拼接并执行sql语句
        self.cur.execute(sqlstr)
        # 涉及写操作要注意提交
        self.conn.commit()

    # #修改书籍    #先删除 后添加  来实现修改功能
    #  def change_book(self,number,name,author,publicationdate,location ,remark):
    #      delete_book(self,bookid)
    #      add_book(self,number,name,author,publicationdate,location,remark)


    # 查找所有IP信息
    def query_all_PON_Script(self):
        self.cur.execute('SELECT IP_Address ,Login_Status,Results,Log FROM pon_script order by IP_Address')
        result = self.cur.fetchall()
        return result

    #查找指定书籍(参数：书名) 根据书籍名称查询书籍
    def query_one_PON_Script(self,IP_Adress):
        sqlstr="SELECT IP_Address ,Login_Status,Results,Log FROM pon_script WHERE IP_Address = '"+IP_Adress+"'"
        self.cur.execute(sqlstr)
        result = self.cur.fetchall()
        return result

    # 查找指定书籍(参数：书籍id) 根据书籍名称查询书籍
    def query_one_book_byid(self, id):
        sqlstr = "SELECT number ,name,author,publicationdate,location ,remark FROM BOOK WHERE number = '" + id + "'"
        self.cur.execute(sqlstr)
        result = self.cur.fetchall()
        return result

    # 借阅记录查询
    def query_borrowrecord(self):
        sqlstr = "SELECT number ,name,location ,borrowname,borrowtime FROM BOOK WHERE isborrow = 1"
        self.cur.execute(sqlstr)
        result = self.cur.fetchall()
        return result

    # 查找读者信息
    def query_readerinfor(self):
        sqlstr = "SELECT name,class,learnnumber,phonenumber,borrownumber FROM student order by id"
        self.cur.execute(sqlstr)
        result = self.cur.fetchall()
        return result

    #注册管理员(参数：账号，密码)
    def register_Admin(self,uername,password):
        # 添加单条数据
        sqlstr = "insert into user (username,psw) values( '" + uername + "','" + password + "');"
        self.cur.execute(sqlstr)
        # 涉及写操作要注意提交
        self.conn.commit()

    #管理员登录(通过账号查询密码)
    def query_Password(self,username):
        sqlstr = "SELECT psw FROM user WHERE username='" + username + "'"
        self.cur.execute(sqlstr)
        result = self.cur.fetchall()
        for row in result:
            password=str(row[0])
            return password


if __name__ == '__main__':
    util = PON_MysqlUtils('localhost', 'root', 'QAZplm86327169', 'wczx_hlw', 'utf8')
    data = util.query_one_PON_Script('127.0.0.1')
    print(data)