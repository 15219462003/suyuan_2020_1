import time
from selenium import webdriver
# from ddt import ddt,data,unpack
from data import datacase

class Log_test():
    driver = webdriver.Firefox()

     #登录
    def denglu(self):
        self.driver.get("http://123.57.140.190/manage/")
        pax = r'C:\Users\Administrator\PycharmProjects\suyuan_sys\data\qqlogin.xlsx'
        E = datacase.Excel1(pax)
        li = E.login_data()
        # print(len(li))
        for i in range(len(li)):
            name=li[i][0]
            pwd=li[i][1]
            time.sleep(1)
            self.driver.find_element_by_css_selector("[placeholder='管理员帐号']").send_keys(name)
            self.driver.find_element_by_css_selector("[placeholder='管理员密码']").send_keys(pwd)
            self.driver.find_element_by_css_selector("[value='管理登录']").click()
            # time.sleep(1)
            # try:
            #     a=self.driver.find_element_by_link_text("产品管理").text
            #     print(a)
            #     if not a:
            #         print("登录失败")
            #     else:
            #         print("登录成功")
            # except Exception as c:
            #     print(c)

        time.sleep(1)

# if __name__ == '__main__':
# d=Log_test()
# d.denglu()
