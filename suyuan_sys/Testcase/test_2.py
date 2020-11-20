from common import Login_sz
import time
from data import datacase

dl=Login_sz.Log_test()
class Flow_test():
    pax = r'C:\Users\Administrator\PycharmProjects\suyuan_sys\data\qqlogin.xlsx'
    lc = datacase.Excel4(pax)
    li = lc.lclb_data()
    def flow_xz(self): #新增流程类别正常新增信息/选择禁用
        dl.driver.find_element_by_link_text("流程记录管理").click()
        dl.driver.find_element_by_link_text("新增流程类别").click()
        for i in range(len(self.li)):
            dl.driver.find_element_by_css_selector("[class='form-control'][name='lcname']").send_keys(self.li[i][0])
            dl.driver.find_element_by_css_selector("[name='paixi'][class='form-control']").send_keys(self.li[i][1])
            dl.driver.find_element_by_css_selector("[class='form-control'][id='zt']").click()
            time.sleep(1)
            if i+1 == 1:
                dl.driver.find_element_by_css_selector("option:nth-child(1)").click()
                time.sleep(1)
            elif i+1==2:
                dl.driver.find_element_by_css_selector("option:nth-child(2)").click()
                time.sleep(1)
            dl.driver.find_element_by_css_selector("[type='submit']").click()
            time.sleep(0.5)

    def flow_xzn(self):#新增流程类别新增一条重复信息
        # dl.driver.find_element_by_xpath("/html/body/section/aside/div/ul/li[3]/a/span[1]").click()
        dl.driver.find_element_by_css_selector("[href='add_lc.php']").click()
        for i in range(len(self.li)):
            dl.driver.find_element_by_css_selector("[class='form-control'][name='lcname']").send_keys(self.li[i][0])
            dl.driver.find_element_by_css_selector("[name='paixi'][class='form-control']").send_keys(self.li[i][1])
            dl.driver.find_element_by_css_selector("[class='form-control'][id='zt']").click()
            dl.driver.find_element_by_css_selector("option:nth-child(1)").click()
            dl.driver.find_element_by_css_selector("[type='submit']").click()
            time.sleep(2)

    def flow_ss(self): #流程类别管理窗口搜索功能
        # dl.driver.find_element_by_xpath("/html/body/section/aside/div/ul/li[3]/a/span[1]").click()
        # time.sleep(1)
        dl.driver.find_element_by_css_selector("[href='list_lc.php']").click()
        time.sleep(2)
        dl.driver.find_element_by_css_selector("[placeholder='输入流程分类名']").send_keys("取消装箱")
        time.sleep(1)
        dl.driver.find_element_by_css_selector("[type='submit'][class='btn btn-success']").click()
        time.sleep(2)

    def flow_ssn(self):#流程类别管理搜索不存在流程分类
        dl.driver.find_element_by_css_selector("[href='list_lc.php']").click()
        time.sleep(2)
        dl.driver.find_element_by_css_selector("[placeholder='输入流程分类名'][name='lcname']").send_keys("hllkhlh")
        dl.driver.find_element_by_css_selector("[class='btn btn-success']").click()
        time.sleep(5)
        print("搜索不存在的")

    def flow_bj(self): #流程类别管理编辑按钮
        # dl.driver.find_element_by_link_text('流程记录管理').click()
        dl.driver.find_element_by_link_text("流程类别管理").click()
        time.sleep(2)
        dl.driver.find_element_by_css_selector(".table > tbody:nth-child(2) > tr:nth-child(5) > td:nth-child(7) > a:nth-child(1)").click()
        time.sleep(2)

        dl.driver.find_element_by_xpath("/html/body/section/section/section/div/div/section/div/form/div[4]/div/button").click()
        time.sleep(0.5)

    def flow_sc(self): #流程类别管理单条删除按钮
        # dl.driver.find_element_by_xpath("/html/body/section/aside/div/ul/li[3]/a/span[1]").click()
        dl.driver.find_element_by_css_selector("[href='list_lc.php']").click()
        dl.driver.find_element_by_css_selector("html body.has-js section#container section#main-content section.wrapper form#myform div.row div.col-md-12 section.panel table.table.table-striped.table-advance.table-hover tbody tr td span.label.label-danger.label-mini.ew80_ontext").click()
        time.sleep(3)
        dl.driver.find_element_by_css_selector("[class='layui-layer-btn0']").click()
        print("单条删除")
        time.sleep(5)

    def flow_plsc(self):# 流程类别管理批量删除功能
        # dl.driver.find_element_by_xpath("/html/body/section/aside/div/ul/li[3]/a/span[1]").click()
        # time.sleep(2)
        dl.driver.find_element_by_css_selector("[href='list_lc.php']").click()
        dl.driver.find_element_by_css_selector("[onclick='CheckAll(this.form)']").click()
        time.sleep(2)
        inputs=dl.driver.find_elements_by_tag_name("input")
        for input in inputs:
           if input.get_attribute('type')=="checkbox":
               input.click()
               time.sleep(1)
        dl.driver.find_element_by_xpath("//*[@id='del']").click()
        time.sleep(5)
        tk = dl.driver.switch_to.alert
        time.sleep(2)
        tk.accept()
        time.sleep(2)
        tt = dl.driver.switch_to.alert
        time.sleep(2)
        tt.accept()
        print("批量删除")
        time.sleep(5)

    def flow_lcjl(self): #录入流程记录正常录入
        dl.driver.find_element_by_css_selector("[href='add_lczs.php']").click()
        time.sleep(2)
        dl.driver.find_element_by_css_selector(".searchable-select-caret").click()
        dl.driver.find_element_by_css_selector(".hover").click()
        time.sleep(1)
        dl.driver.find_element_by_css_selector("[placeholder='一行一个，回车换行 , 支持扫描枪']").send_keys("18389664")
        dl.driver.find_element_by_css_selector("[placeholder='在此输入流程记录的简要说明']").send_keys("装箱准备发货")
        dl.driver.find_element_by_css_selector("[name='zrr'][class='form-control']").send_keys("熊大")
        dl.driver.find_element_by_id("czdate").clear()
        dl.driver.find_element_by_id("czdate").send_keys("2020-11-1 15:23:30")
        dl.driver.find_element_by_css_selector("[class='btn btn-danger'][name='Submit']").click()
        time.sleep(2)

    def flow_lcjln(self):#录入流程记录不规范录入
        # dl.driver.find_element_by_link_text("流程记录管理").click()
        dl.driver.find_element_by_css_selector("[href='add_lczs.php']").click()
        time.sleep(2)
        nwm = datacase.Excel3(self.pax)
        li=nwm.nul_wm_data()
        for i in range(len(li)):
            dl.driver.find_element_by_css_selector(".searchable-select-caret").click()
            dl.driver.find_element_by_css_selector(".hover").click()
            time.sleep(1)
            dl.driver.find_element_by_css_selector("[placeholder='一行一个，回车换行 , 支持扫描枪']").send_keys(li[i])
            dl.driver.find_element_by_css_selector("[placeholder='在此输入流程记录的简要说明']").send_keys("装箱准备发货")
            dl.driver.find_element_by_css_selector("[name='zrr'][class='form-control']").send_keys("熊大")
            dl.driver.find_element_by_id("czdate").clear()
            dl.driver.find_element_by_id("czdate").send_keys("2020-11-1 15:23:30")
            dl.driver.find_element_by_css_selector("[class='btn btn-danger'][name='Submit']").click()
            time.sleep(0.5)

    def flow_jlgl(self): #流程记录管理搜索功能
        dl.driver.find_element_by_css_selector("[href='list_lcsy.php']").click()
        dl.driver.find_element_by_css_selector("[placeholder='录入或扫码条形码']").send_keys("18389664")
        dl.driver.find_element_by_css_selector("[class='btn btn-success']").click()
        time.sleep(2)

    def flow_jlgln(self):  #流程记录管理搜索不存在条码功能
        dl.driver.find_element_by_css_selector("[href='list_lcsy.php']").click()
        pax = r'C:\Users\Administrator\PycharmProjects\suyuan_sys\data\qqlogin.xlsx'
        nwm = datacase.Excel3(pax)
        li = nwm.nul_wm_data()
        for i in range(len(li)):
            dl.driver.find_element_by_css_selector("[placeholder='录入或扫码条形码']").send_keys(li[i])
            dl.driver.find_element_by_css_selector("[class='btn btn-success']").click()
            time.sleep(2)

    def flow_jlbj(self):  #流程记录管理编辑功能
        # dl.driver.find_element_by_xpath("/html/body/section/aside/div/ul/li[3]/a/span[1]").click()
        dl.driver.find_element_by_css_selector("[href='list_lcsy.php']").click()
        dl.driver.find_element_by_css_selector("[class='label label-success label-mini']").click()
        time.sleep(2)
        dl.driver.find_element_by_class_name("searchable-select-caret").click()
        dl.driver.find_element_by_xpath("/html/body/section/section/section/div/div/section/div/form/div[1]/div[1]/div/div[2]/div/div[2]/div[3]").click()
        time.sleep(2)
        dl.driver.find_element_by_css_selector("[class='form-control'][name='lcsm']").send_keys("黑科技就是牛")
        dl.driver.find_element_by_css_selector("[name='zrr']").send_keys("小小")
        dl.driver.find_element_by_css_selector("[id='zt']").click()
        dl.driver.find_element_by_css_selector("option:nth-child(2)")
        dl.driver.find_element_by_css_selector("[id='czdate']").clear()
        dl.driver.find_element_by_css_selector("[id='czdate']").send_keys("2020-05-11 08:50:30")
        dl.driver.find_element_by_css_selector("[type='submit']").click()
        time.sleep(0.5)

    def flow_dtsc(self):
        # dl.driver.find_element_by_xpath("/html/body/section/aside/div/ul/li[3]/a/span[1]").click()
        dl.driver.find_element_by_css_selector("[href='list_lcsy.php']").click()
        dl.driver.find_element_by_css_selector("[class='label label-danger label-mini  ew80_ontext']").click()
        time.sleep(2)
        dl.driver.find_element_by_class_name("layui-layer-btn0").click()
        time.sleep(0.5)

    def flow_jlglsc(self):#流程记录管理批量删除
        # dl.driver.find_element_by_xpath("/html/body/section/aside/div/ul/li[3]/a/span[1]").click()
        dl.driver.find_element_by_css_selector("[href='list_lcsy.php']").click()
        time.sleep(2)
        count=0
        dl.driver.find_element_by_css_selector("[title='全选']").click()
        inputs=dl.driver.find_elements_by_tag_name("input")
        for input in inputs:
            if input.get_attribute("type")=="checkbox":
                count += 1
                input.click()
                time.sleep(1)
                if count==4:
                    break
        dl.driver.find_element_by_css_selector("[id='del'][type='submit']").click()
        time.sleep(2)
        tk=dl.driver.switch_to.alert
        tk.accept()
        time.sleep(0.5)














































if __name__ == '__main__':
    f=Flow_test()
    f.test_02_fl()
    f.test_03_fl()
    f.test_04_fl()
    f.test_05_fl()
    f.test_06_fl()
    f.test_07_fl()
    f.test_08_fl()





