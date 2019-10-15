#! /usr/bin/python
# coding=UTF-8
# version:python3.x

import unittest
import monsoon as  Mon



class TEST_MONSOON(unittest.TestCase):

    # def test_zip_dir(self):
    #     Mon.zip_dir("c:/tools", "c:/tools.zip")
    #
    # def test_unzip_file(self):
    #     Mon.unzip_file( "c:/tools.zip","c:/toolsback")


    def test_path(self):
        print(Mon.trim_path("c:\\files\\\\file2//files"))
        print(Mon.base_path("c:\\files\\\\file2//files"))
    def test_common(self):
        print(Mon.base_path())
        print(Mon.base_path("/str/test.txt"))
        # print(date_time_str())
        print(Mon.date_now())
        print(Mon.load_keyvalue("127.0.0.1", "root", "123456", "datas", "WEIBOLOGIN"))


    def test_listfile(self):
        Mon.list_file('c:/workspace/', print, '*.java')

if __name__ == '__main__':
    print("==============>start test")
    log = Mon.logger(__name__,"c:/run.log")
    log.info("info")
    log.debug("debug")
    log.error("error")
    unittest.main()
