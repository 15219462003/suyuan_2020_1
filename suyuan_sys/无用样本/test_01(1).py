
import time
from 产品溯源系统.public import login1
DL=login1.Test_Denglu()

class XZCP():
     def xzlcleb(self):
         time.sleep(5)
         DL.driver.find_element_by_css_selector(".sub-menu:nth-child(3) span:nth-child(2)").click()
         DL.driver.find_element_by_link_text("新增流程类别").click()
         DL.driver.find_element_by_xpath("/html/body/section/section/section/div/div/section/div/form/div[1]/div[1]/input").send_keys("5荒原帅苹果入库")
         DL.driver.find_element_by_css_selector("div.form-group:nth-child(2) > div:nth-child(2) > input:nth-child(1)").send_keys("1")
         DL.driver.find_element_by_id("zt").click()
         DL.driver.find_element_by_css_selector("option:nth-child(1)").click()
         DL.driver.find_element_by_css_selector(".btn").click()
         time.sleep(5)

     def xzlcl_FAN(self):
         time.sleep(5)
         DL.driver.find_element_by_css_selector(".sub-menu:nth-child(3) span:nth-child(2)").click()
         DL.driver.find_element_by_link_text("新增流程类别").click()
         DL.driver.find_element_by_xpath("/html/body/section/section/section/div/div/section/div/form/div[1]/div[1]/input").send_keys("5荒原帅苹果入库")
         DL.driver.find_element_by_css_selector("div.form-group:nth-child(2) > div:nth-child(2) > input:nth-child(1)").send_keys("1")
         DL.driver.find_element_by_id("zt").click()
         DL.driver.find_element_by_css_selector("option:nth-child(1)").click()
         DL.driver.find_element_by_css_selector(".btn").click()
         time.sleep(5)
         try:
            c=DL.driver.find_element_by_class_name("layui-layer-content")
            d="流程类别名有重复!"
            DL.driver.assertEqual(c,d,"输入有重复")
         except Exception as e:
                    print("异常为：",e)
     def test_04(self):
         DL.driver.find_element_by_css_selector(".sub-menu:nth-child(3) span:nth-child(2)").click()
         DL.driver.find_element_by_link_text("流程类别管理").click()
         DL.driver.find_element_by_name("lcname").send_keys("5荒原帅苹果入库")
         DL.driver.find_element_by_css_selector(".btn.btn-success").click()

     def test_05(self):
         DL.driver.find_element_by_css_selector(".sub-menu:nth-child(3) span:nth-child(2)").click()
         DL.driver.find_element_by_link_text("流程类别管理").click()
         DL.driver.find_element_by_name("lcname").send_keys("5荒原帅苹果入库")
         DL.driver.find_element_by_css_selector(".btn.btn-success").click()






