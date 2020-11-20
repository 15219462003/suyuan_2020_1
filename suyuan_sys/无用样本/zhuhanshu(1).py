'''
项目名称:产品溯源系统
所属模块:登录
日期:2020/11/04
作者:毛展
版本:version:1.0
'''

import unittest
from 产品溯源系统.testcase import test_01
from 产品溯源系统.public import login1

xzlb = test_01.XZCP()
denglu=login1.Test_Denglu()

class Test_size(unittest.TestCase):
    @classmethod
    def setUpClass(self):

        denglu.Denglu()

    def test_xzlb_01(self):

        xzlb.xzlcleb()

    def test_xzlb_02(self):

        xzlb.xzlcl_FAN()

    @classmethod
    def tearDownClass(cls):
        denglu.driver.quit()


if __name__ == '__main__':
    unittest.main()

# if __name__ == '__main__':
#     # unittest.main()
#     suite=unittest.TestSuite()
#     suite.addTest(Test_size("test_size1"))
#     # runner = unittest.TextTestRunner()
#     # runner.run(suite)
#     path1='C:\\Users\\Administrator\\PycharmProjects\\产品溯源系统\\report\\login_01.html'
#     f=open(path1,'wb')
#     runner=HTMLTestRunner(stream=f,title="public",description="测试登录描述",tester="毛展")
#     runner.run(suite)
