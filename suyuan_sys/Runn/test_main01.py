import unittest
from common import Login_sz
from Testcase import test_1

fwgl=test_1.Fwmgl_test()

class test_size(unittest.TestCase):
    log = Login_sz.Log_test()
    @classmethod
    def setUpClass(self):
        self.log.denglu()


    # @classmethod
    # def tearDownClass(self):
    #     log.driver.quit()

    def test_1(self):
        fwgl.fwmgl_plsc()

    def test_2(self):
        fwgl.fwmgl_dg()

    def test_3(self):
        fwgl.fwmgl_plxg_wm()

    def test_4(self):
        fwgl.fwmgl_plxg_id()

    def test_5(self):
        fwgl.fwmgl_plxg_pc()

    def test_6(self):
        fwgl.fwmgl_cpm()

    def test_7(self):
        fwgl.fwmgl_rq()
