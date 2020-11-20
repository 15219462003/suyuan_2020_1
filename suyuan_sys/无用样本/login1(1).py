'''
项目名称:产品溯源系统
所属模块:登录
日期:2020/11/04
作者:毛展
版本:version:1.0
'''
from selenium import webdriver

import time

class Test_Denglu():
    driver=webdriver.Firefox()
    def Denglu(self):
       self.driver.get(r"http://123.57.140.190/manage/index.php")
       self.driver.implicitly_wait(2)
       self.driver.find_element_by_css_selector("input.form-control:nth-child(1)").send_keys("admin")
       self.driver.find_element_by_css_selector("input.form-control:nth-child(2)").send_keys("admin999")
       self.driver.find_element_by_css_selector(".btn").click()
       time.sleep(5)

       #     try:
       #         c = self.driver.title
       #         d = "甘肃锶泽信息科技有限公司"
       #         self.assertEqual(c, d, "没有成功登录锶泽")
       #     except Exception as e:
       #         print("异常为：", e)
       #         time.sleep(3)
dl=Test_Denglu()
dl.Denglu()