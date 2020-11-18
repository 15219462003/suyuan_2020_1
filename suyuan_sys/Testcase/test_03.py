from common import Login_sz
import time
from selenium.webdriver.common.keys import Keys
from data import datacase

dl=Login_sz.Log_test()
dl.driver.maximize_window()
class Fwmgl_test():
    pax = r'C:\Users\Administrator\PycharmProjects\suyuan_sys\data\qqlogin.xlsx'
    wlm=datacase.Excel2(pax)
    hm=datacase.Excel8(pax)
    fwmh=time.strftime("%Y%m%d%H%M%S",time.localtime(int(time.time())))
#批量生成防伪码
    def fwmgl_plsc(self):
        time.sleep(1)
        dl.driver.find_element_by_xpath("/html/body/section/aside/div/ul/li[2]/ul/li[1]/a").click()
        dl.driver.find_element_by_css_selector("[name='riqi']").clear()
        dl.driver.find_element_by_css_selector("[name='riqi']").send_keys(self.fwmh)
        time.sleep(1)
        dl.driver.find_element_by_css_selector("[name='code_length']").clear()
        dl.driver.find_element_by_css_selector("[name='code_length']").send_keys("16")
        dl.driver.find_element_by_name("code_pre").clear()
        dl.driver.find_element_by_name("code_pre").send_keys("FW")
        dl.driver.find_element_by_id("code_type").click()
        time.sleep(1)
        dl.driver.find_element_by_css_selector("#code_type > option:nth-child(3)").click()
        time.sleep(1)
        dl.driver.find_element_by_id("txm_type").click()
        dl.driver.find_element_by_css_selector("#txm_type > option:nth-child(1)").click()
        dl.driver.find_element_by_css_selector("[name='txm_num']").clear()
        dl.driver.find_element_by_css_selector("[name='txm_num']").send_keys("10")
        time.sleep(1)
        dl.driver.find_element_by_css_selector("[name='code_count']").clear()
        dl.driver.find_element_by_css_selector("[name='code_count']").send_keys('5')
        time.sleep(1)
        dl.driver.find_element_by_xpath("/html/body/section/section/section/div/div/section/div/form/div[7]/div[1]/div/span").click()
        time.sleep(1)
        dl.driver.find_element_by_xpath("/html/body/section/section/section/div/div/section/div/form/div[7]/div[1]/div/div[2]/div/div[2]/div[5]").click()
        time.sleep(2)
        dl.driver.find_element_by_xpath("/html/body/section/section/section/div/div/section/div/form/div[8]/div[1]/div/span").click()
        dl.driver.find_element_by_xpath("/html/body/section/section/section/div/div/section/div/form/div[8]/div[1]/div/div[2]/div/div[2]/div[8]").click()
        time.sleep(2)
        dl.driver.find_element_by_css_selector("[id='qiyong']").click()
        dl.driver.find_element_by_css_selector("#qiyong > option:nth-child(1)").click()
        time.sleep(1)
        dl.driver.find_element_by_css_selector("[value='开始批量生成']").click()
        time.sleep(0.5)
        try:
            a=dl.driver.find_element_by_css_selector("[class='layui-layer-ico layui-layer-ico1']")
            if a:
                print("生成成功")
            else:
                print("生成失败")
        except Exception as e:
            print(e)
        time.sleep(2)

    # 单个生成防伪码
    def fwmgl_dg(self):
        dl.driver.find_element_by_xpath("/html/body/section/aside/div/ul/li[2]/ul/li[2]/a").click()
        time.sleep(1)
        dl.driver.find_element_by_css_selector(".col-sm-3 > input:nth-child(1)").clear()
        dl.driver.find_element_by_css_selector(".col-sm-3 > input:nth-child(1)").send_keys(self.fwmh)
        time.sleep(1)
        dl.driver.find_element_by_css_selector("[name='txm']").clear()
        dl.driver.find_element_by_css_selector("[name='txm']").send_keys("5555555555")
        time.sleep(1)
        dl.driver.find_element_by_xpath("/html/body/section/section/section/div/div/section/div/form/div[4]/div[1]/div/span").click()
        time.sleep(1)
        dl.driver.find_element_by_xpath("/html/body/section/section/section/div/div/section/div/form/div[4]/div[1]/div/div[2]/div/div[2]/div[8]").click()
        time.sleep(1)
        dl.driver.find_element_by_xpath("/html/body/section/section/section/div/div/section/div/form/div[5]/div[1]/div/span").click()
        time.sleep(1)
        dl.driver.find_element_by_xpath("/html/body/section/section/section/div/div/section/div/form/div[5]/div[1]/div/div[2]/div/div[2]/div[5]").click()
        time.sleep(1)
        dl.driver.find_element_by_id("qiyong").click()
        dl.driver.find_element_by_css_selector("#qiyong > option:nth-child(1)").click()
        dl.driver.find_element_by_css_selector("[type='submit']").click()
        time.sleep(2)
        try:
            a=dl.driver.find_element_by_css_selector("[class='layui-layer-ico layui-layer-ico1']")
            if a:
                print("单个生成成功")
            else:
                print("单个生成失败")
        except Exception as e:
            print(e)
        time.sleep(2)
#按物流码批量修改
    def fwmgl_plxg_wm(self):
        dl.driver.find_element_by_xpath("/html/body/section/aside/div/ul/li[2]/ul/li[3]/a").click()
        time.sleep(1)
        ma=self.wlm.wlm_data()
        for i in range(len(ma)):
            dl.driver.find_element_by_id("txm").send_keys(ma[i])
            dl.driver.find_element_by_id("txm").send_keys(Keys.ENTER)
            time.sleep(1)
        dl.driver.find_element_by_css_selector("div.row:nth-child(1) > div:nth-child(1) > section:nth-child(1) > div:nth-child(2) > form:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2)").click()
        dl.driver.find_element_by_xpath("/html/body/section/section/section/div[1]/div/section/div/form/div[2]/div[1]/div/div[2]/div/div[2]/div[10]").click()
        time.sleep(1)
        dl.driver.find_element_by_xpath("/html/body/section/section/section/div[1]/div/section/div/form/div[3]/div[1]/div/div[1]").click()
        dl.driver.find_element_by_xpath("/html/body/section/section/section/div[1]/div/section/div/form/div[3]/div[1]/div/div[2]/div/div[2]/div[5]").click()
        time.sleep(1)
        dl.driver.find_element_by_css_selector("div.row:nth-child(1) > div:nth-child(1) > section:nth-child(1) > div:nth-child(2) > form:nth-child(1) > div:nth-child(4) > div:nth-child(1) > button:nth-child(1)").click()
        time.sleep(0.5)
        try:
            a=dl.driver.find_element_by_css_selector("[class='layui-layer-ico layui-layer-ico1']")
            if a:
                print("按物流码批量修改成功")
            else:
                print("按物流码批量修改失败")
        except Exception as e:
            print(e)
        time.sleep(2)

        # 按防伪码ID段批量修改
    def fwmgl_plxg_id(self):
        weizhi = dl.driver.find_element_by_xpath(
            "/html/body/section/section/section/div[2]/div/section/div/form/div[1]/label")
        dl.driver.execute_script("return arguments[0].scrollIntoView();", weizhi)
        time.sleep(1)
        dm=self.hm.fdh()
        for i in range(len(dm)):
            if i==0:
                dl.driver.find_element_by_css_selector("[placeholder='开始ID']").send_keys(dm[i])
            elif i==1:
                dl.driver.find_element_by_css_selector("[placeholder='结束ID']").send_keys(dm[i])
        time.sleep(1)
        dl.driver.find_element_by_xpath("/html/body/section/section/section/div[2]/div/section/div/form/div[2]/div[1]/div/span").click()
        dl.driver.find_element_by_xpath("/html/body/section/section/section/div[2]/div/section/div/form/div[2]/div[1]/div/div[2]/div/div[2]/div[8]").click()
        time.sleep(1)
        dl.driver.find_element_by_xpath("/html/body/section/section/section/div[2]/div/section/div/form/div[3]/div[1]/div/span").click()
        dl.driver.find_element_by_xpath("/html/body/section/section/section/div[2]/div/section/div/form/div[3]/div[1]/div/div[2]/div/div[2]/div[8]").click()
        time.sleep(1)
        dl.driver.find_element_by_xpath("/html/body/section/section/section/div[2]/div/section/div/form/div[4]/div/button").click()
        time.sleep(0.5)
        try:
            a=dl.driver.find_element_by_css_selector("[class='layui-layer-ico layui-layer-ico1']")
            if a:
                print("按id段批量修改成功")
            else:
                print("按id段批量修改失败")
        except Exception as e:
            print(e)
        time.sleep(2)

    #按批次批量修改
    def fwmgl_plxg_pc(self):
        dl.driver.find_element_by_xpath("/html/body/section/aside/div/ul/li[2]/ul/li[3]/a").click()
        time.sleep(2)
        # weizhi=dl.driver.find_element_by_xpath("/html/body/section/section/section/div[3]/div/section/div/form/div[1]/div[2]/p/span")
        # dl.driver.execute_script("return arguments[0].scrollIntoView();",weizhi)
        # time.sleep(1)
        dl.driver.find_element_by_xpath("/html/body/section/section/section/div[3]/div/section/div/form/div[1]/div[1]/div/span").click()
        time.sleep(1)
        dl.driver.find_element_by_xpath("/html/body/section/section/section/div[3]/div/section/div/form/div[1]/div[1]/div/div[2]/div/div[2]/div[6]").click()
        dl.driver.find_element_by_xpath("/html/body/section/section/section/div[3]/div/section/div/form/div[2]/div[1]/div/span").click()
        time.sleep(1)
        dl.driver.find_element_by_xpath("/html/body/section/section/section/div[3]/div/section/div/form/div[2]/div[1]/div/div[2]/div/div[2]/div[11]").click()
        dl.driver.find_element_by_xpath("/html/body/section/section/section/div[3]/div/section/div/form/div[3]/div[1]/div/span").click()
        time.sleep(1)
        dl.driver.find_element_by_xpath("/html/body/section/section/section/div[3]/div/section/div/form/div[3]/div[1]/div/div[2]/div/div[2]/div[2]").click()
        time.sleep(1)
        dl.driver.find_element_by_xpath("/html/body/section/section/section/div[3]/div/section/div/form/div[4]/div/button").click()
        time.sleep(2)
        try:
            a=dl.driver.find_element_by_css_selector("[class='layui-layer-ico layui-layer-ico1']")
            if a:
                print("按批次批量修改成功")
            else:
                print("按批次批量修改失败")
        except Exception as e:
            print(e)
        time.sleep(2)

    #按产品名批量次改
    def fwmgl_cpm(self):
        weizhi = dl.driver.find_element_by_xpath("/html/body/section/section/section/div[4]/div/section/div/form/div[2]/label")
        dl.driver.execute_script("return arguments[0].scrollIntoView();", weizhi)
        time.sleep(1)
        dl.driver.find_element_by_xpath("/html/body/section/section/section/div[4]/div/section/div/form/div[1]/div[1]/div/span").click()
        dl.driver.find_element_by_xpath("/html/body/section/section/section/div[4]/div/section/div/form/div[1]/div[1]/div/div[2]/div/div[2]/div[10]").click()
        time.sleep(1)
        dl.driver.find_element_by_xpath("/html/body/section/section/section/div[4]/div/section/div/form/div[2]/div[1]/div/span").click()
        dl.driver.find_element_by_xpath("/html/body/section/section/section/div[4]/div/section/div/form/div[2]/div[1]/div/div[2]/div/div[2]/div[8]").click()
        time.sleep(1)
        dl.driver.find_element_by_xpath("/html/body/section/section/section/div[4]/div/section/div/form/div[3]/div/button").click()
        time.sleep(0.5)
        try:
            a=dl.driver.find_element_by_css_selector("[class='layui-layer-ico layui-layer-ico1']")
            if a:
                print("按产品名批量修改成功")
            else:
                print("按产品名批量修改失败")
        except Exception as e:
            print(e)
        time.sleep(2)

        # 按日期批量次改
    def fwmgl_rq(self):
        weizhi = dl.driver.find_element_by_xpath("/html/body/section/section/section/div[5]/div/section/div/form/div[3]/label")
        dl.driver.execute_script("return arguments[0].scrollIntoView();", weizhi)
        time.sleep(1)
        dl.driver.find_element_by_xpath("/html/body/section/section/section/div[5]/div/section/div/form/div[1]/div[1]/div/span").click()
        dl.driver.find_element_by_xpath("/html/body/section/section/section/div[5]/div/section/div/form/div[1]/div[1]/div/div[2]/div/div[2]/div[2]").click()
        time.sleep(1)
        dl.driver.find_element_by_xpath("/html/body/section/section/section/div[5]/div/section/div/form/div[2]/div[1]/div/span").click()
        dl.driver.find_element_by_xpath("/html/body/section/section/section/div[5]/div/section/div/form/div[2]/div[1]/div/div[2]/div/div[2]/div[11]").click()
        time.sleep(1)
        dl.driver.find_element_by_xpath("/html/body/section/section/section/div[5]/div/section/div/form/div[3]/div[1]/div/span").click()
        dl.driver.find_element_by_xpath("/html/body/section/section/section/div[5]/div/section/div/form/div[3]/div[1]/div/div[2]/div/div[2]/div[2]").click()
        time.sleep(1)
        dl.driver.find_element_by_xpath("/html/body/section/section/section/div[5]/div/section/div/form/div[4]/div/button").click()
        time.sleep(0.5)
        try:
            a = dl.driver.find_element_by_css_selector("[class='layui-layer-ico layui-layer-ico1']")
            if a:
                print("按日期名批量修改成功")
            else:
                print("按日期名批量修改失败")
        except Exception as e:
            print(e)
        time.sleep(2)







































































































































































