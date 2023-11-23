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

    # #增加设备信息
    def add_PON_device (self,IP_Address,Login_Status,Results,Log ):
        sqlstr="insert into pon_script (IP_Address,Login_Status,Results,Log ) " \
               "values( '"+IP_Address+"','"+Login_Status+"','"+Results+"','"+Log+"');"
        self.cur.execute(sqlstr)
        # 涉及写操作要注意提交
        self.conn.commit()

    #删除PON设备，根据设备IP删除
    def delete_PON_device(self, IP_Address):
        sqlstr="delete from pon_script where IP_Address = '" + IP_Address + "';"
        #拼接并执行sql语句
        self.cur.execute(sqlstr)
        # 涉及写操作要注意提交
        self.conn.commit()

    # #修改书籍    #先删除 后添加  来实现修改功能
    def update_PON_device(self,data,attribute,IP_Address):
        sqlstr = "UPDATE pon_script SET "+attribute+" = "+data+" where IP_Address = '" + IP_Address + "';"
        print(sqlstr)
        self.cur.execute(sqlstr)
        self.conn.commit()


    # 查找所有IP信息
    def query_all_PON_Script(self):
        self.cur.execute('SELECT IP_Address ,Login_Status,Results,Log FROM pon_script order by IP_Address')
        result = self.cur.fetchall()
        return result

    #查找指定设备信息(参数：IP) 根据IP查找设备
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
    # data = util.query_all_PON_Script()
    # print(data)
    util.update_PON_device('0','Results','127.0.0.1')
    data = util.query_all_PON_Script()
    print(data)