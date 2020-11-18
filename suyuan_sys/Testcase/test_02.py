from common import Login_sz
import time
from data import datacase
from selenium.webdriver.common.keys import Keys
dl=Login_sz.Log_test()
class Sysl_test():
    pax = r'C:\Users\Administrator\PycharmProjects\suyuan_sys\data\qqlogin.xlsx'
    sl=datacase.Excel5(pax)
    ma=datacase.Excel2(pax)
    man=datacase.Excel3(pax)
    syjl=datacase.Excel6(pax)
    syjln=datacase.Excel7(pax)

    #新增溯源实例新增内容
    def sysl_xz(self):
        dl.driver.find_element_by_xpath("/html/body/section/aside/div/ul/li[4]/a/span[1]").click()
        time.sleep(1)
        dl.driver.find_element_by_css_selector("[href='add_suyuan.php']").click()
        time.sleep(2)
        dl.driver.find_element_by_css_selector("html body.has-js section#container section#main-content section.wrapper div.row div.col-lg-12 section.panel div.panel-body form.form-horizontal.tasi-form div.form-group div.col-sm-4 input.form-control").send_keys("品质")
        time.sleep(1)
        dl.driver.switch_to.frame(0)
        dl.driver.find_element_by_xpath("/html/body").send_keys(Keys.TAB)
        dl.driver.find_element_by_xpath("/html/body").send_keys("质量问题")
        dl.driver.switch_to.default_content()
        dl.driver.find_element_by_css_selector("[type='submit']").click()
        time.sleep(0.5)
        try:
            a=dl.driver.find_element_by_css_selector("html body.has-js div#layui-layer1.layui-layer.layui-layer-dialog.layui-layer-border.layui-layer-msg div.layui-layer-content.layui-layer-padding").text
            if a=="恭喜，溯源增加成功！":
                print("新增成功")
            else:
                print("新增失败")
        except Exception as e:
            print(e)
        time.sleep(2)
    #新增溯源实例 搜索存在的
    def sysl_slgl(self):
        dl.driver.find_element_by_css_selector("[href='list_suyuan.php']").click()
        time.sleep(2)
        dl.driver.find_element_by_css_selector("[placeholder='请输入溯源实例名称']").send_keys("品质")
        dl.driver.find_element_by_css_selector("[class='btn btn-success']").click()
        time.sleep(0.5)
        try:
            a=dl.driver.find_element_by_css_selector("html body.has-js section#container section#main-content section.wrapper form#myform div.row div.col-md-12 section.panel table.table.table-striped.table-advance.table-hover tbody tr td b").text
            if a=="品质":
                print("搜索匹配")
            else:
                print("搜索不匹配")
        except Exception as e:
            print(e)
        time.sleep(2)
#新增溯源实例 搜索不存在的
    def sysl_slgln(self):
        dl.driver.find_element_by_css_selector("[href='list_suyuan.php']").click()
        time.sleep(2)
        li=self.sl.sysl_data()
        for i in range(len(li)):
            dl.driver.find_element_by_css_selector("[placeholder='请输入溯源实例名称']").send_keys(li[i])
            dl.driver.find_element_by_css_selector("[class='btn btn-success']").click()
            time.sleep(2)

    # 新增溯源实例编辑按钮
    def sysl_bj(self):
        dl.driver.find_element_by_css_selector("[href='list_suyuan.php']").click()
        time.sleep(1)
        dl.driver.find_element_by_css_selector("[class='label label-success label-mini']").click()
        time.sleep(2)
        dl.driver.find_element_by_css_selector("[class='form-control']").clear()
        dl.driver.find_element_by_css_selector("[class='form-control']").send_keys("静安寺")
        dl.driver.switch_to.frame(0)
        dl.driver.find_element_by_css_selector("html body.ke-content").send_keys(Keys.TAB)
        dl.driver.find_element_by_css_selector("html body.ke-content").send_keys("牛排要全熟")
        dl.driver.switch_to.default_content()
        dl.driver.find_element_by_css_selector("[type='submit']").click()
        time.sleep(0.5)
        try:
            a=dl.driver.find_element_by_css_selector("[class='layui-layer-ico layui-layer-ico1']")
            if a:
                print("修改成功")
            else:
                print("修改失败")
        except Exception as e:
            print(e)
        time.sleep(2)

    # 溯源实例删除按钮
    def sysl_scyg(self):
        dl.driver.find_element_by_css_selector("[href='list_suyuan.php']").click()
        time.sleep(1)
        dl.driver.find_element_by_css_selector("[class='label label-danger label-mini  ew80_ontext']").click()
        dl.driver.find_element_by_css_selector("[class='layui-layer-btn0']").click()
        time.sleep(0.5)
        try:
            a=dl.driver.find_element_by_css_selector("[class='layui-layer-ico layui-layer-ico1']")
            if a:
                print("删除成功")
            else:
                print("删除失败")
        except Exception as e:
            print(e)
        time.sleep(2)
    #溯源实例管理中查看功能
    def sysl_ck(self):
        dl.driver.find_element_by_css_selector("[href='list_suyuan.php']").click()
        time.sleep(1)
        dl.driver.find_element_by_css_selector("[class='ew80_ontext']").click()
        time.sleep(1)
        try:
            a=dl.driver.find_element_by_css_selector("[class='layui-layer-title']").text
            if a=="预览":
                print("查看成功")
            else:
                print("查看失败")
        except Exception as e:
            print(e)
        dl.driver.find_element_by_css_selector("[class='layui-layer-ico layui-layer-close layui-layer-close1']").click()
        time.sleep(1)
    #新增溯源实例批量删除
    def sysl_plsc(self):
        dl.driver.find_element_by_css_selector("[href='list_suyuan.php']").click()
        time.sleep(1)
        count=0
        dl.driver.find_element_by_id("chkAll").click()
        inputs = dl.driver.find_elements_by_tag_name("input")
        for input in inputs:
            if input.get_attribute('type')=="checkbox":
                input.click()
                count+=1
                time.sleep(1)
                if count==6:
                    break
        dl.driver.find_element_by_id("del").click()
        time.sleep(2)
        tk=dl.driver.switch_to.alert
        time.sleep(2)
        tk.accept()
        time.sleep(2)
        print(tk.text)
        tk.accept()
        time.sleep(1)
#批量溯源操作---按物流码批量操作
    def sysl_pl_wlm(self):
        dl.driver.find_element_by_css_selector("[href='edit_suyuan_all.php']").click()
        time.sleep(2)
        wm=self.ma.wlm_data()
        for i in range(len(wm)):
            dl.driver.find_element_by_id("txm").send_keys(wm[i])
            dl.driver.find_element_by_id("txm").send_keys(Keys.ENTER)
        dl.driver.find_element_by_css_selector("[class='searchable-select-caret']").click()
        time.sleep(1)
        dl.driver.find_element_by_css_selector("[class='searchable-select-item']").click()
        dl.driver.find_element_by_css_selector("[class='btn btn-danger']").click()
        time.sleep(0.5)
        try:
            a=dl.driver.find_element_by_css_selector("[class='layui-layer-ico layui-layer-ico1']")
            if a:
                print("批量操作成功")
            else:
                print("批量操作失败")
        except Exception as e:
            print(e)
        time.sleep(2)

    # 批量溯源操作---按物流码批量操作,输入不存在的
    def sysl_pl_wlmn(self):
        dl.driver.find_element_by_css_selector("[href='edit_suyuan_all.php']").click()
        time.sleep(2)
        wmn=self.man.nul_wm_data()
        for i in range(len(wmn)):
            dl.driver.find_element_by_id("txm").send_keys(wmn[i])
            dl.driver.find_element_by_id("txm").send_keys(Keys.ENTER)
        dl.driver.find_element_by_css_selector("[class='searchable-select-caret']").click()
        time.sleep(1)
        dl.driver.find_element_by_css_selector("[class='searchable-select-item']").click()
        dl.driver.find_element_by_css_selector("[class='btn btn-danger']").click()
        time.sleep(0.5)
        try:
            a=dl.driver.find_element_by_css_selector("[class='layui-layer-ico layui-layer-ico1']")
            if a:
                print("批量操作成功")
            else:
                print("批量操作失败")
        except Exception as e:
            print(e)
        time.sleep(2)

    # 批量溯源操作---按防伪码码段码批量操作,输入存在的
    def sysl_fwm(self):
        dl.driver.find_element_by_css_selector("[href='edit_suyuan_all.php']").click()
        time.sleep(2)
        weizhi=dl.driver.find_element_by_css_selector("[class='col-sm-2 col-sm-2 control-label']")
        dl.driver.execute_script("return arguments[0].scrollIntoView();",weizhi)
        time.sleep(1)
        fm=self.ma.fwm_data()
        for i in range(len(fm)):
            if i==0:
                dl.driver.find_element_by_css_selector("[placeholder='开始ID']").send_keys(fm[i])
                dl.driver.find_element_by_css_selector("[placeholder='结束ID']").send_keys(fm[i+1])
        dl.driver.find_element_by_xpath("/html/body/section/section/section/div[2]/div/section/div/form/div[2]/div[1]/div/span").click()
        time.sleep(1)
        dl.driver.find_element_by_xpath("/html/body/section/section/section/div[2]/div/section/div/form/div[2]/div[1]/div/div[2]/div/div[2]/div[3]").click()
        time.sleep(1)
        dl.driver.find_element_by_xpath("/html/body/section/section/section/div[2]/div/section/div/form/div[3]/div/button").click()
        time.sleep(0.5)
        try:
            a=dl.driver.find_element_by_css_selector("[class='layui-layer-ico layui-layer-ico1']")
            if a:
                print("批量操作成功")
            else:
                print("批量操作失败")
        except Exception as e:
            print(e)
        time.sleep(2)

    # 批量溯源操作---按防伪码码段码批量操作,输入不存在的
    def sysl_fwmn(self):
        dl.driver.find_element_by_css_selector("[href='edit_suyuan_all.php']").click()
        time.sleep(2)
        weizhi = dl.driver.find_element_by_css_selector("[class='col-sm-2 col-sm-2 control-label']")
        dl.driver.execute_script("return arguments[0].scrollIntoView();", weizhi)
        fwmn = self.man.nul_wm_data()
        for i in range(len(fwmn)):
            if i == 0:
                dl.driver.find_element_by_css_selector("[placeholder='开始ID']").send_keys(fwmn[i])
                dl.driver.find_element_by_css_selector("[placeholder='结束ID']").send_keys(fwmn[i + 1])
        dl.driver.find_element_by_xpath("/html/body/section/section/section/div[2]/div/section/div/form/div[2]/div[1]/div/span").click()
        time.sleep(1)
        dl.driver.find_element_by_xpath("/html/body/section/section/section/div[2]/div/section/div/form/div[2]/div[1]/div/div[2]/div/div[2]/div[3]").click()
        time.sleep(1)
        dl.driver.find_element_by_xpath(
            "/html/body/section/section/section/div[2]/div/section/div/form/div[3]/div/button").click()
        time.sleep(0.5)
        try:
            a = dl.driver.find_element_by_css_selector("[class='layui-layer-ico layui-layer-ico1']")
            if a:
                print("批量操作成功")
            else:
                print("批量操作失败")
        except Exception as e:
            print(e)
        time.sleep(2)

    # 批量溯源操作---按防伪码批量操作
    def sysl_fw(self):
        dl.driver.find_element_by_css_selector("[href='edit_suyuan_all.php']").click()
        time.sleep(2)
        weizhi=dl.driver.find_element_by_css_selector("[class='col-sm-2 col-sm-2 control-label']")
        dl.driver.execute_script("return arguments[0].scrollIntoView();",weizhi)
        time.sleep(1)
        dl.driver.find_element_by_css_selector("[class='searchable-select-caret']").click()
        dl.driver.find_element_by_css_selector("html body.has-js section#container section#main-content section.wrapper div.row div.col-lg-12 section.panel div.panel-body form.form-horizontal.tasi-form div.form-group div.col-sm-3 div.searchable-select div.searchable-select-dropdown div.searchable-scroll div.searchable-select-items div.searchable-select-item").click()
        dl.driver.find_element_by_xpath("/html/body/section/section/section/div[3]/div/section/div/form/div[3]/div/button").click()
        try:
            a=dl.driver.find_element_by_css_selector("[class='layui-layer-ico layui-layer-ico1']")
            if a:
                print("第三批量成功")
            else:
                print("第三批量失败")
        except Exception as e:
            print(e)
        time.sleep(2)

    # 批量溯源操作---按产品名批量操作
    def sysl_cpm(self):
        dl.driver.find_element_by_css_selector("[href='edit_suyuan_all.php']").click()
        time.sleep(2)
        weizhi=dl.driver.find_element_by_css_selector("[class='col-sm-2 col-sm-2 control-label']")
        dl.driver.execute_script("return arguments[0].scrollIntoView();",weizhi)
        dl.driver.find_element_by_xpath("/html/body/section/section/section/div[4]/div/section/div/form/div[1]/div[1]/div/span").click()
        time.sleep(1)
        dl.driver.find_element_by_xpath("/html/body/section/section/section/div[4]/div/section/div/form/div[1]/div[1]/div/div[2]/div/div[2]/div[2]").click()
        time.sleep(1)
        dl.driver.find_element_by_xpath("/html/body/section/section/section/div[4]/div/section/div/form/div[2]/div[1]/div/span").click()
        dl.driver.find_element_by_xpath("/html/body/section/section/section/div[4]/div/section/div/form/div[2]/div[1]/div/div[2]/div/div[2]/div[27]").click()
        time.sleep(1)
        dl.driver.find_element_by_xpath("/html/body/section/section/section/div[4]/div/section/div/form/div[3]/div/button").click()
        try:
            a=dl.driver.find_element_by_css_selector("[class='layui-layer-ico layui-layer-ico1']")
            if a:
                print("第四批量成功")
            else:
                print("第四批量失败")
        except Exception as e:
            print(e)
        time.sleep(2)

#批量溯源操作---按日期批量操作
    def sysl_rq(self):
        dl.driver.find_element_by_css_selector("[href='edit_suyuan_all.php']").click()
        time.sleep(2)
        weizhi=dl.driver.find_element_by_css_selector("[class='col-sm-2 col-sm-2 control-label']")
        dl.driver.execute_script("return arguments[0].scrollIntoView();",weizhi)
        dl.driver.find_element_by_xpath("/html/body/section/section/section/div[5]/div/section/div/form/div[1]/div[1]/div/div[1]").click()
        dl.driver.find_element_by_xpath("/html/body/section/section/section/div[5]/div/section/div/form/div[1]/div[1]/div/div[2]/div/div[2]/div[2]").click()
        time.sleep(1)
        dl.driver.find_element_by_xpath("/html/body/section/section/section/div[5]/div/section/div/form/div[2]/div[1]/div/span").click()
        dl.driver.find_element_by_xpath("/html/body/section/section/section/div[5]/div/section/div/form/div[2]/div[1]/div/div[2]/div/div[2]/div[20]").click()
        time.sleep(1)
        dl.driver.find_element_by_xpath("/html/body/section/section/section/div[5]/div/section/div/form/div[3]/div/button").click()
        try:
            a = dl.driver.find_element_by_css_selector("[class='layui-layer-ico layui-layer-ico1']")
            if a:
                print("第5批量成功")
            else:
                print("第5批量失败")
        except Exception as e:
            print(e)
        time.sleep(2)
#溯源操作记录，搜索存在内容
    def sysl_czjl(self):
        dl.driver.find_element_by_css_selector("[href='history_suyuan.php']").click()
        time.sleep(2)
        valid=self.syjl.valid_record()
        for i in range(len(valid)):
            dl.driver.find_element_by_css_selector("[placeholder='输入操作记录内容关键词']").send_keys(valid[i])
            dl.driver.find_element_by_css_selector("[class='btn btn-success']").click()
            time.sleep(1)
            try:
                a=dl.driver.find_element_by_css_selector("[class='label label-danger label-mini  ew80_ontext']").text
                if a:
                    print("搜索准确")
                else:
                    print("搜索不到")
            except Exception as e:
                print(e)
            time.sleep(2)

    # 溯源操作记录，搜索不存在内容
    def sysl_czjln(self):
        dl.driver.find_element_by_css_selector("[href='history_suyuan.php']").click()
        time.sleep(2)
        invalid = self.syjln.invalid_record()
        for i in range(len(invalid)):
            dl.driver.find_element_by_css_selector("[placeholder='输入操作记录内容关键词']").send_keys(invalid[i])
            dl.driver.find_element_by_css_selector("[class='btn btn-success']").click()
            time.sleep(2)
            try:
                a = dl.driver.find_element_by_css_selector("[class='label label-danger label-mini  ew80_ontext']").text
                if a:
                    print("搜索准确")
                else:
                    print("搜索不到")
            except Exception as e:
                print(e)
            time.sleep(2)

    # 溯源操作记录,单个删除
    def sysl_dtsc(self):
        dl.driver.find_element_by_css_selector("[href='history_suyuan.php']").click()
        time.sleep(2)
        dl.driver.find_element_by_css_selector("[class='label label-danger label-mini  ew80_ontext']").click()
        time.sleep(1)
        dl.driver.find_element_by_css_selector("[class='layui-layer-btn0']").click()
        time.sleep(0.5)
        try:
            a=dl.driver.find_element_by_css_selector("[class='layui-layer-ico layui-layer-ico1']")
            if a:
                print("单条删除成功")
            else:
                print("单条删除失败")
        except Exception as e:
            print(e)
        time.sleep(2)

    # 溯源操作记录,批量删除
    def sysl_plsc2(self):
        dl.driver.find_element_by_css_selector("[href='history_suyuan.php']").click()
        time.sleep(2)
        dl.driver.find_element_by_css_selector("[title='全选']").click()
        count=0
        inputs=dl.driver.find_elements_by_tag_name('input')
        for input in inputs:
            if input.get_attribute('type')=="checkbox":
                count+=1
                input.click()
                time.sleep(1)
                if count==4:
                    break
        time.sleep(1)
        dl.driver.find_element_by_id("del").click()
        time.sleep(1)
        tk=dl.driver.switch_to.alert
        time.sleep(1)
        tk.accept()
        time.sleep(1)
        a=tk.text
        try:
            if a=="批量删除成功":
                print("批量删除成功")
            else:
                print("批量删除失败")
        except Exception as e:
            print(e)
        time.sleep(2)
        tk.accept()























# if __name__ == '__main__':
