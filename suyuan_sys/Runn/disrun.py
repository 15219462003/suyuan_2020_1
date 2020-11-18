import unittest
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