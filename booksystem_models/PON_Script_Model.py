#Model层

#导入数据库操作工具类
from PON_MysqlUtils import PON_MysqlUtils

#书籍bean类 属性number name author publiccationdate location remark
class PON_Script(object):
    def __init__(self, IP_Address ,Login_Status,Results,Log):
        self.IP_Address = IP_Address
        self.Login_Status = Login_Status
        self.Results = Results
        self.Log=Log


#书籍model
class PON_Script_Model(object):

    #初始化 建立数据库连接
    def __init__(self):
        self.util = PON_MysqlUtils('localhost', 'root', 'QAZplm86327169', 'wczx_hlw', 'utf8')

    #查询所有书籍
    def get_all_PON_Script_data(self):
        self.u = self.util.query_all_PON_Script()
        PON_Script_list = []
        for i in self.u:
            PON_Script_list.append(PON_Script(i[0], i[1], i[2], i[3]))
        return PON_Script_list

    #查询一本书
    def get_one_PON_Script_data(self,IP_Adress):
        self.u = self.util.query_one_PON_Script(IP_Adress)
        one_PON_Script_list = []
        for i in self.u:
            one_PON_Script_list.append(PON_Script(i[0], i[1], i[2], i[3]))
        return one_PON_Script_list

    #根据id删除一本书
    def delete_one_book_by_id(self,bookid):
        self.util.delete_book(bookid)

    #添加书籍
    def add_book(self,number,name,author,publicationdate,location,remark):
        self.util.add_book(number,name,author,publicationdate,location,remark)


