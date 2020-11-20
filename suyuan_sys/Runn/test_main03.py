import unittest
from common import Login_sz
from Testcase import test_3

log = Login_sz.Log_test()
sysl=test_3.Sysl_test()
class test_size(unittest.TestCase):

    # @classmethod
    # def setUpClass(self):
    #     log.denglu()
    #
    @classmethod
    def tearDownClass(self):
        log.driver.quit()

    def test_22(self):
        sysl.sysl_xz()
    #
    def test_23(self):
        sysl.sysl_slgl()

    def test_24(self):
        sysl.sysl_slgln()

    def test_25(self):
        sysl.sysl_bj()

    def test_26(self):
        sysl.sysl_scyg()

    def test_27(self):
        sysl.sysl_ck()

    def test_28(self):
        sysl.sysl_plsc()

    def test_29(self):
        sysl.sysl_pl_wlm()

    def test_30(self):
        sysl.sysl_pl_wlmn()

    def test_31(self):
        sysl.sysl_fwm()

    def test_32(self):
        sysl.sysl_fwmn()

    def test_33(self):
        sysl.sysl_fw()

    def test_34(self):
        sysl.sysl_cpm()

    def test_35(self):
        sysl.sysl_rq()

    def test_36(self):
        sysl.sysl_czjl()

    def test_37(self):
        sysl.sysl_czjln()

    def test_38(self):
        sysl.sysl_dtsc()

    def test_39(self):
        sysl.sysl_plsc2()
