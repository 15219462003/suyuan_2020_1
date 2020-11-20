import unittest
from requests_toolbelt.multipart import MultipartEncoder
import requests


class Sy_2():

    def denglu(self):
        url = "http://123.57.140.190/manage/index.php?act=adminlogin"
        data1 = {'Username': 'admin', 'Password': 'admin999', 'Submit': '管理登录'}
        header = {'Content-Type': 'application/x-www-form-urlencoded'}
        r = requests.post(url, data=data1, headers=header)
        print(r.text)
        cookie = "PHPSESSID" + "=" + r.cookies["PHPSESSID"]
        return cookie

    def xinzeng(self):
        a = self.denglu()
        url1 = "http://123.57.140.190/manage/add_cp.php?act=save_cp"
        data2 = MultipartEncoder({'pro_name': '拉链10',
                                  'cpbh': '465468985',
                                  'cptxm': '412164351',
                                  'cpms': '倚天屠龙记'})
        head2 = {'Content-Type': data2.content_type,
                 'Cookie': a}
        r2 = requests.post(url1, data=data2, headers=head2)
        print(r2.text)

    def fwm_tianjia(self):
        a = self.denglu()
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


if __name__ == '__main__':
    s = Sy_2()
    s.denglu()
    s.xinzeng()
    s.fwm_tianjia()
