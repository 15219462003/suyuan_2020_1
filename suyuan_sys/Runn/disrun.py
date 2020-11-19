import unittest
import sys
import 
os
curPath = os.path.abspath(os.path.dirname(r'C:\Users\Administrator\PycharmProjects\autosuyuansys\common\majorfunctionfwm.py'))

rootPath = os.path.split(curPath)[0]

sys.path.append(rootPath)
class runfun():
    def di(self):
        lj = r'./'
        discover = unittest.defaultTestLoader.discover(lj, pattern='test_*.py')
        return discover
if __name__ == '__main__':
    q=runfun()
    l=q.di()
    Runner = unittest.TextTestRunner()
    Runner.run(l)