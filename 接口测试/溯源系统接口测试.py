
import requests
from requests_toolbelt.multipart import MultipartEncoder
import unittest
# url="https://v0.yiketianqi.com/api"
# data={'appid':'78778619','appsecret':'y3UvmynJ','version':'v61'}
# r=requests.post(url,)
# print(r.json())

class Suyuan_automate(unittest.TestCase):
    def setUp(self):
        url = "http://123.57.140.190/manage/index.php?act=adminlogin"
        data = {"Username": "admin", "Password": "admin999", "Submit": "管理登录"}
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        r = requests.post(url, data=data, headers=headers)
        print(r.text)
        cookie = "PHPSESSID" + "=" + r.cookies["PHPSESSID"]
        return cookie

    def test_zdd(self):
        a = self.setUp()
        url1 = "http://123.57.140.190/manage/add_cp.php?act=save_cp"
        data = MultipartEncoder({'pro_name':'拉链8',
                                'cpbh':'4654689',
                                'cptxm':'4164351',
                                'cpms':'降记号三年级'})
        headers1 = {"Content-Type": data.content_type,
                    "Cookie": a}
        r1 = requests.post(url=url1, data=data, headers=headers1)
        print(r1.text)

    def test_fwm_tianjia(self):
        a = self.setUp()
        url="http://123.57.140.190/manage/add_fwm.php?act=save_code"
        data3={'riqi':'132315456',
               'code_length':'8',
               'code_pre':'kk',
               'code_type':'2',
               'txm_type':'4',
               'txm_num':'10',
               'code_count':'10',
               'product':'350',
               'zd1': '31',
               'qiyong': 'yes'}
        header3={'Content-Type':'application/x-www-form-urlencoded',
                 'Cookie':a}
        r=requests.post(url,data=data3,headers=header3)
        print(r.text)

    def test_pici_shanchu(self):
        a = self.setUp()
        url="http://123.57.140.190/manage/del_fwm_all.php?act=pici"
        data4=MultipartEncoder({'riqi':'13213213653515'})
        header4={'Content-Type':data4.content_type,
                 'Cookie':a}
        r=requests.post(url,data=data4,headers=header4)
        print(r.text)

    def test_name_bianji(self):
        url="http://123.57.140.190/manage/edit_cp.php?act=save_edit_pro"
        data5=MultipartEncoder({'id':'395',
                                'pro_name':'飞来峰',
                                'cpbh':'888666',
                                'cptxm':'666888',
                                'cpms':'此山非彼山'})
        headers5={'Content-Type':data5.content_type,
                 'Cookie':self.setUp()}
        r=requests.post(url,data=data5,headers=headers5)
        print(r.text)




if __name__ == '__main__':
    unittest.main()
