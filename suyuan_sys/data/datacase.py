import xlrd

#登录验证数据
class Excel1():
    def __init__(self, Excelpath: object, sheetname: object = "Sheet1"):
        self.data = xlrd.open_workbook(Excelpath)
        self.table = self.data.sheet_by_name(sheetname)
        # 取第一行的关键词
        self.keys = self.table.row_values(0)
        # 获取总行数
        self.rowNUM = self.table.nrows
        # 获取总列数
        self.colNUM = self.table.ncols

    def login_data(self):
        result = []
        # 按行读取表格内容添加到result列表中，方便调用
        for line in range(self.rowNUM):
            shuju = self.table.row_values(line)
            result.append(shuju)
        # print(result)
        return result
# 真实物流码，防伪码
class Excel2():
    def __init__(self, Excelpath: object, sheetname: object = "Sheet2"):
        self.data = xlrd.open_workbook(Excelpath)
        self.table = self.data.sheet_by_name(sheetname)
        # 取第一行的关键词
        # self.keys = self.table.row_values(0)
        # 获取总行数
        self.rowNUM = self.table.nrows
        # 获取总列数
        self.colNUM = self.table.ncols

    def wlm_data(self):
        result = []
        # 按行读取表格内容添加到result列表中，方便调用
        self.wlm=self.table.col_values(0)
        for i in range(len(self.wlm)):
            wlm_shuju = self.wlm[i]
            result.append(wlm_shuju)
        # print(result)
        return result

    def fwm_data(self):
        result=[]
        self.fwm = self.table.col_values(1)
        for i in range(len(self.fwm)):
            fwm_shuju = self.fwm[i]
            result.append(fwm_shuju)
        # print(result)
        return result

#物流码不存在数据
class Excel3():
    def __init__(self, Excelpath: object, sheetname: object = "Sheet3"):
        self.data = xlrd.open_workbook(Excelpath)
        self.table = self.data.sheet_by_name(sheetname)
        # 获取总列数
        self.colNUM = self.table.ncols
        # 获取对应的数值（第三列——不存在的物流码）
        self.zhi = self.table.col_values(0)

    def nul_wm_data(self):
        result = []
        # 按行读取表格内容添加到result列表中，方便调用
        for i in range(len(self.zhi)):
            shuju = self.zhi[i]
            result.append(shuju)
        # print(result)
        return result

#新增流程类别数据
class Excel4():
    def __init__(self, Excelpath: object, sheetname: object = "Sheet4"):
        self.data = xlrd.open_workbook(Excelpath)
        self.table = self.data.sheet_by_name(sheetname)
        # 获取总列数
        self.colNUM = self.table.ncols
        # 获取总行数
        self.rowNUM = self.table.nrows

    def lclb_data(self):
        result = []
        for line in range(self.rowNUM):
            shuju=self.table.row_values(line)
            result.append(shuju)
        # print(result)
        return result

class Excel5():
    def __init__(self, Excelpath: object, sheetname: object = "Sheet5"):
        self.data = xlrd.open_workbook(Excelpath)
        self.table = self.data.sheet_by_name(sheetname)
        # 获取总列数
        self.colNUM = self.table.ncols
        # 获取总行数
        self.rowNUM = self.table.nrows

    def sysl_data(self):
        result = []
        for line in range(self.rowNUM):
            shuju=self.table.row_values(line)
            result.append(shuju)
        # print(result)
        return result
#溯源记录搜索数据（有效的）
class Excel6():
    def __init__(self,Excelpath:object,sheetname:object="Sheet6"):
        self.data=xlrd.open_workbook(Excelpath)
        self.table=self.data.sheet_by_name(sheetname)
        self.colNUM=self.table.ncols
        self.rowNUM=self.table.nrows
#有效记录
    def valid_record(self):
        jl=self.table.col_values(0)
        # print(jl)
        return jl

#溯源记录搜索数据（无效的）
class Excel7():
    def __init__(self, Excelpath: object, sheetname: object = "Sheet7"):
        self.data = xlrd.open_workbook(Excelpath)
        self.table = self.data.sheet_by_name(sheetname)
        self.colNUM = self.table.ncols
        self.rowNUM = self.table.nrows
#无效记录
    def invalid_record(self):
        jl = self.table.col_values(0)
        # print(jl)
        return jl

class Excel8():  #防伪码ID段
    def __init__(self, Excelpath: object, sheetname: object = "Sheet8"):
        self.data = xlrd.open_workbook(Excelpath)
        self.table = self.data.sheet_by_name(sheetname)
        self.colNUM = self.table.ncols
        self.rowNUM = self.table.nrows

    # 防伪码ID段提取
    def fdh(self):
        jl = self.table.col_values(0)
        print(jl)
        return jl





# if __name__ == '__main__':
    # pax = r'C:\Users\Administrator\PycharmProjects\suyuan_sys\data\qqlogin.xlsx'
    # E = Excel8(pax)
    # E.fdh()

