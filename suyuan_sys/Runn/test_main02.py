import unittest
from common import Login_sz
from Testcase import test_2

log = Login_sz.Log_test()
jlgl=test_2.Flow_test()


class test_size(unittest.TestCase):
    # @classmethod
    # def setUpClass(self):
    #     log.denglu()

#流程记录管理模块
    def test_8(self):
        jlgl.flow_xz()
        a = log.driver.find_element_by_css_selector("html body.has-js div#layui-layer1.layui-layer.layui-layer-dialog.layui-layer-border.layui-layer-msg")
        self.assertTrue(a,msg="新增失败")
    #
    def test_9(self):
        jlgl.flow_xzn()

    def test_10(self):
        jlgl.flow_ss()
        a = log.driver.find_element_by_xpath(
            "/html/body/section/section/section/form/div/div/section/table/tbody/tr/td[3]").text
        b = "取消装箱"
        self.assertEqual(a,b,msg="搜索不匹配")

    unittest.skip('跳过')
    def test_11(self):
        jlgl.flow_ssn()

    def test_12(self):
        jlgl.flow_bj()
        a = log.driver.find_element_by_css_selector(".layui-layer-ico")
        self.assertTrue(a, msg="修改失败")
    #
    def test_13(self):
        jlgl.flow_sc()

    def test_14(self):
        jlgl.flow_plsc()

    def test_15(self):
        jlgl.flow_lcjl()

    def test_16(self):
        jlgl.flow_lcjln()
        a=log.driver.find_element_by_css_selector(".layui-layer-content")
        self.assertTrue(a, msg="不规范录入失败")

    def test_17(self):
        jlgl.flow_jlgl()

    def test_18(self):
        jlgl.flow_jlgln()

    def test_19(self):
        jlgl.flow_jlbj()
        a = log.driver.find_element_by_xpath("/html/body/div[3]/div")
        self.assertTrue(a, msg="修改失败")

    def test_20(self):
        jlgl.flow_dtsc()
        a = log.driver.find_element_by_xpath("/html/body/div[3]/div")
        self.assertTrue(a, msg="删除失败")

    def test_21(self):
        jlgl.flow_jlglsc()
        a = log.driver.find_element_by_xpath("/html/body/div[3]/div")
        self.assertTrue(a, msg="批量删除失败")



# # 溯源实例管理模块
# class test_sl_02(unittest.TestCase):
#     @classmethod
#     def setUpClass(self):
#         log.denglu()
#
#     @classmethod
#     def tearDownClass(self):
#         log.driver.quit()

    # def test_15(self):
    #     sysl.sysl_xz()
    #
    # def test_16(self):
    #     sysl.sysl_slgl()
    #
    # def test_17(self):
    #     sysl.sysl_slgln()
    #
    # def test_18(self):
    #     sysl.sysl_bj()
    #
    # def test_19(self):
    #     sysl.sysl_scyg()
    #
    # def test_20(self):
    #     sysl.sysl_ck()
    #
    # def test_21(self):
    #     sysl.sysl_plsc()
    # def test_22(self):
    #     sysl.sysl_pl_wlm()
    # def test_23(self):
    #     sysl.sysl_pl_wlmn()
    #
    # def test_24(self):
    #     sysl.sysl_fwm()
    #
    # def test_25(self):
    #     sysl.sysl_fwmn()
    #
    # def test_26(self):
    #     sysl.sysl_fw()
    #
    # def test_27(self):
    #     sysl.sysl_cpm()
    #
    # def test_28(self):
    #     sysl.sysl_rq()
    #
    # def test_29(self):
    #     sysl.sysl_czjl()
    #
    # def test_30(self):
    #     sysl.sysl_czjln()
    #
    # def test_31(self):
    #     sysl.sysl_dtsc()
    #
    # def test_32(self):
    #     sysl.sysl_plsc2()

# # 防伪码管理模块
# class test_fwm_03(unittest.TestCase):
#     @classmethod
#     def setUpClass(self):
#         log.denglu()
#
#     @classmethod
#     def tearDownClass(self):
#         log.driver.quit()

    # def test_33(self):
    #     fwgl.fwmgl_plsc()
    #
    # def test_34(self):
    #     fwgl.fwmgl_dg()
    #
    # def test_35(self):
    #     fwgl.fwmgl_plxg_wm()
    #
    # def test_36(self):
    #     fwgl.fwmgl_plxg_id()
    #
    # def test_37(self):
    #     fwgl.fwmgl_plxg_pc()
    #
    # def test_38(self):
    #     fwgl.fwmgl_cpm()
    #
    # def test_39(self):
    #     fwgl.fwmgl_rq()















#
# if __name__ == '__main__':
#     unittest.main()
    # suite=unittest.TestSuite
    # suite.addTests(test_size("test_01_lcxz"))
    # test_dir='./'
    # discover=unittest.defaultTestLoader.discover(test_dir,pattern='test_*.py')
    # Runner=unittest.TextTestRunner()
    # Runner.run(discover)
