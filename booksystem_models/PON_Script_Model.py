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

    #查询所有设备
    def get_all_PON_Script_data(self):
        self.u = self.util.query_all_PON_Script()
        PON_Script_list = []
        for i in self.u:
            PON_Script_list.append(PON_Script(i[0], i[1], i[2], i[3]))
        return PON_Script_list

    #按IP地址查询设备
    def get_one_PON_Script_data(self,IP_Adress):
        self.u = self.util.query_one_PON_Script(IP_Adress)
        one_PON_Script_list = []
        for i in self.u:
            one_PON_Script_list.append(PON_Script(i[0], i[1], i[2], i[3]))
        return one_PON_Script_list

    #根据IP地址删除一个设备
    def delete_one_PON_device(self,IP_Address):
        self.util.delete_PON_device(IP_Address)

    #添加书籍
    def add_PON_device(self,IP_Address,Login_Status,Results,Log):
        self.util.add_PON_device(IP_Address,Login_Status,Results,Log)

    #修改设备信息
    def update_PON_device(self,data,attribute,IP_Address):
        self.util.update_PON_device(data,attribute,IP_Address)


