#! /usr/bin/python
# coding=UTF-8
# version:python3.x

import unittest

from Autnpy import Autnpy


class TEST_Autnpy(unittest.TestCase):
    def test_zip(self):
        # Autnpy.zip_dir("c:/tools", "c:/tools.zip")
        # Autnpy.unzip_file( "c:/tools.zip","c:/toolsback")
        pass

    def test_path(self):
        print(Autnpy.base_path())
        print(Autnpy.trim_path("c:\\files\\\\file2//files"))
        print(Autnpy.base_path("c:\\files\\\\file2//files"))
        print(Autnpy.base_path("/str/test.txt"))

    def test_time(self):
        print("=>time:",Autnpy.date_now())

    def test_listfile(self):
        # Autnpy.list_file('c:/workspace/', print)
        pass

    def test_string(self):
        text = """导语：沙,[}皇【是俄罗斯人最早}《用来称拜帝国皇帝的名号’””：“”""".strip().replace("\s+", "")
        test = Autnpy.remove_punctuation(text)
        self.assertEqual(22, len(test))

        print(Autnpy.random_string(10))
        self.assertEqual(len(Autnpy.random_string(10)), 10)

        self.assertEqual(Autnpy.md5str("123456"), "e10adc3949ba59abbe56e057f20f883e")
    
    def test_web(self):
        self.assertEqual(Autnpy.is_valid_link('https://jingyan.baidu.com/'),True)



    def test_date(self):
        print(Autnpy.date_now())
        print(Autnpy.date_str2date('2020-08-03 19:53:21'))
        print(Autnpy.date_nginxTime2date('21/Dec/2019:21:45:31 +0800'))
if __name__ == '__main__':
    print("==============>start test")
    log = Autnpy.logger(__name__,"c:/run.log")
    log.info("info")
    log.debug("debug")
    log.error("error")
    #log = monsoon.logger(__name__, "c:/run.log")
    unittest.main()


