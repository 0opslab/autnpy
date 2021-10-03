#! /usr/bin/python
# coding=UTF-8
# version:python3.x
import os
import random
import string
import hashlib
import logging
import datetime
import zipfile
import shutil,zipfile
import re
from urllib.parse import urlparse

"""封装一些常用的方法，方便操作
@author 0opslab
@url https://github.com/0opslab
"""

class Autnpy:
    @staticmethod
    def logger(modeule_name, log_file="run.log"):
        """Initialize logging module."""
        log = logging.getLogger(modeule_name)
        formatter = logging.Formatter(
            '%(asctime)s-(%(name)s)-[%(levelname)s] %(message)s')
        log.setLevel(logging.DEBUG)

        # Create a file handler to store error messages
        fhdr = logging.FileHandler(log_file, mode='w')
        fhdr.setLevel(logging.ERROR)
        fhdr.setFormatter(formatter)

        # Create a stream handler to print all messages to console
        chdr = logging.StreamHandler()
        chdr.setFormatter(formatter)

        log.addHandler(fhdr)
        log.addHandler(chdr)
        return log

    ###################################################################
    # 常用方法封装
    @staticmethod
    def dedupe(items, key=None):
        """字典列表去重
        :param items:字典列表
        :param key:为一个偏函数
        :return:
        """
        seen = set()
        for item in items:
            val = item if key is None else key(item)
            if val not in seen:
                yield item
                seen.add(val)


    ####################################################################
    # 文件相关的操作封装
    @staticmethod
    def trim_path(file_name):
        """返回标准的路径"""
        return os.path.normpath(file_name).replace("\\", "/")

    @staticmethod
    def base_path(file=''):
        """获取当前路径下的开始文件的全路径"""
        return Autnpy.trim_path(os.getcwd().replace("\\", "/").split("src/")[0] + file)



    @staticmethod
    def hash_file(fine_name, hashtype="sha256", block_size=64 * 1024):
        """ Support md5(), sha1(), sha224(), sha256(), sha384(), sha512(),
        blake2b(), blake2s(),sha3_224, sha3_256, sha3_384, sha3_512,
        shake_128, and shake_256
        """
        
        with open(fine_name, 'rb') as file:
            fhash = hashlib.new(hashtype, b"")
            while True:
                data = file.read(block_size)
                if not data:
                    break
                fhash.update(data)
            return fhash.hexdigest()

    @staticmethod
    def zip_dir(dirname, zipfilename):
        """
        @函数目的: 压缩指定目录为zip文件
        @参数说明：dirname为指定的目录，zipfilename为压缩后的zip文件路径
        """
        
        filelist = []
        if os.path.isfile(dirname):
            filelist.append(dirname)
        else:
            for root, dirs, files in os.walk(dirname):
                for name in files:
                    filelist.append(os.path.join(root, name))

        zf = zipfile.ZipFile(zipfilename, "w", zipfile.zlib.DEFLATED)

        for tar in filelist:
            arcname = tar[len(dirname):]
            # print arcname
            zf.write(tar, arcname)

        zf.close()

    @staticmethod
    def unzip_file(zipfilename, unziptodir):
        """
        | ##@函数目的: 解压zip文件到指定目录
        | ##@参数说明：zipfilename为zip文件路径，unziptodir为解压文件后的文件目录
        | ##@返回值：无
        | ##@函数逻辑：
        """
        if not os.path.exists(unziptodir):
            os.mkdir(unziptodir)
        zfobj = zipfile.ZipFile(zipfilename)
        for name in zfobj.namelist():
            name = name.replace('\\', '/')

            if name.endswith('/'):
                p = os.path.join(unziptodir, name[:-1])
                if os.path.exists(p):
                    # 如果文件夹存在，就删除之：避免有新更新无法复制
                    shutil.rmtree(p)
                os.mkdir(p)
            else:
                ext_filename = os.path.join(unziptodir, name)
                ext_dir = os.path.dirname(ext_filename)
                if not os.path.exists(ext_dir):
                    os.mkdir(ext_dir)
                outfile = open(ext_filename, 'wb')
                outfile.write(zfobj.read(name))
                outfile.close()

    @staticmethod
    def read_file_prefix(file, lens):
        """读取文件的前lens个字节"""
        with open(file, "rb") as temp:
            prefix = ''.join(['%02x' % b for b in bytes(temp.read(lens))])
            return prefix

    @staticmethod
    def read_fileContent(file, encoding="utf-8"):
        """读取文件内容"""
        with open(file, "r", encoding) as ff:
            return ff.read()

    @staticmethod
    def del_path(path):
        """删除目录"""
        ls = os.listdir(path)
        for i in ls:
            c_path = os.path.join(path, i)
            if os.path.isdir(c_path):
                Autnpy.del_path(c_path)
            else:
                os.remove(c_path)
        os.rmdir(path)
    





    @staticmethod
    def list_file(path, fun):
        """罗列从某个文件夹下的某一类文件，可以使用通配符
            path：路径
            fun：处理函数
            suffix：匹配指定规则的文件
        """
        if not callable(fun):
            raise Exception("Argument fun must be a function type")

        for root, dirs, files in os.walk(path):
            for file in files:
                fun(os.path.join(root, file))

    @staticmethod
    def list_file_suffix(dir, filetypes):
        """在目录dir中根据文件后缀查找文件"""
        lst = []
        for root, dirs, files in os.walk(dir):
            for file in files:
                suffix = os.path.splitext(file)[1]
                if suffix in filetypes:
                    filepath = os.path.join(root, file)
                    lst.append(filepath)

    @staticmethod
    def file_lines(ff, fun, encoding="utf-8"):
        """按行读入文件并通过函数fun处理"""
        with open(ff, encoding) as ff:
            for line in ff:
                fun(line)

    #####################################################################
    # 字符串相关的操作
    @staticmethod
    def random_string(lens):
        """返回指定长度(任意长度)随机字符串"""
        # 利用ascii随机
        # num_set = [chr(i) for i in range(48,58)]
        # char_set = [chr(i) for i in range(97,123)]
        # char_sset = [chr(i) for i in range(65,91)]
        # 从a-zA-Z0-9生成指定数量的随机字符(总共62个字符)
        total_set = string.ascii_letters + string.digits
        if lens <= 62:
            return "".join(random.sample(total_set, lens))
        else:
            cs = lens//62
            ys = lens % 62
            rs = ""
            for i in range(cs):
                rs += "".join(random.sample(total_set, 62))
            rs += "".join(random.sample(total_set, ys))
            return rs
    @staticmethod
    def str_Q2B(ustring):
        """把字符串全角转半角"""
        ss = []
        for s in ustring:
            rstring = ""
            for uchar in s:
                inside_code = ord(uchar)
                # 全角空格直接转换
                if inside_code == 12288:
                    inside_code = 32
                # 全角字符（除空格）根据关系转化
                elif (inside_code >= 65281 and inside_code <= 65374):
                    inside_code -= 65248
                rstring += chr(inside_code)
            ss.append(rstring)
        return ''.join(ss)

    @staticmethod
    def str_B2Q(ustring):
        """把字符串全角转半角"""
        ss = []
        for s in ustring:
            rstring = ""
            for uchar in s:
                inside_code = ord(uchar)
                # 全角空格直接转换
                if inside_code == 32:
                    inside_code = 12288
                # 全角字符（除空格）根据关系转化
                elif (inside_code >= 33 and inside_code <= 126):
                    inside_code += 65248
                rstring += chr(inside_code)
            ss.append(rstring)
        return ''.join(ss)

    @staticmethod
    def remove_punctuation(line, strip_all=True):
        """删除所有的标点符号"""
        
        if strip_all:
            rule = re.compile("[^a-zA-Z0-9\u4e00-\u9fa5]")
            line = rule.sub('', line)
        else:
            punctuation = """！？｡＂＃＄％＆＇（）＊＋－／：；＜＝＞＠［＼］＾＿｀｛｜｝～｟｠｢｣､、〃》「」『』【】〔〕〖〗〘〙〚〛〜〝〞〟〰〾〿–—‘'‛“”„‟…‧﹏"""
            re_punctuation = "[{}]+".format(punctuation)
            line = re.sub(re_punctuation, "", line)
        return line.strip()

    @staticmethod
    def replace_punctuation(line, target=' ', strip_all=True):
        """将所有的标点符号统一替换位target字符串"""
        if strip_all:
            rule = re.compile("[^a-zA-Z0-9\u4e00-\u9fa5]")
            line = rule.sub(target, line)
        else:
            punctuation = """！？｡＂＃＄％＆＇（）＊＋－／：；＜＝＞＠［＼］＾＿｀｛｜｝～｟｠｢｣､、〃》「」『』【】〔〕〖〗〘〙〚〛〜〝〞〟〰〾〿–—‘'‛“”„‟…‧﹏"""
            re_punctuation = "[{}]+".format(punctuation)
            line = re.sub(re_punctuation, target, line)
        return line.strip()

    @staticmethod
    def md5str(*args):
        """获取字符串的md5"""
        datastr = ""
        for x in args:
            datastr = datastr + str(x)
        m = hashlib.md5(datastr.encode(encoding='utf-8'))
        return m.hexdigest()



    @staticmethod
    def try_decode(res):
        """尝试使用常见的几种中文编码进行解码"""
        try:
            text = res.decode('utf-8')
            return text
        except UnicodeDecodeError:
            pass
        try:
            text = res.decode('gb2312')
            return text
        except UnicodeDecodeError:
            pass
        try:
            text = res.decode('gbk')
            return text
        except UnicodeDecodeError:
            pass
        #logger.error('[UnicodeDecodeError]')
        return None
    
    ################################################################
    # web相关常用的方法参数
    @staticmethod
    def is_valid_link(link):
        """
        检测有效链接
        嵌入的 data:image 图片不作为新链接
        os.path.relpath 返回值最前面多一个 . 需要删掉
        """
        regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

        # print() # True
        # print(re.match(regex, "example.com") is not None)            # False
        return re.match(regex, link) is not None

    @staticmethod
    def get_abs_filepath(home_dir, link):
        """把链接转换为本地网站文件夹的绝对路径"""
        rel_url = link.split('/',1)[1][1:].split('/',1)[1]	
        abs_filepath = os.path.join(home_dir, rel_url).replace("\\",'/')
        if abs_filepath.find('..') > 0:
            parts = abs_filepath.split('..')
            abs_filepath = '/'.join(parts[0].split('/')[0:-2]) + parts[1]
        if os.path.isdir(abs_filepath):
            #logger.warning('[isdir]\t{0}\t{1}'.format(link, abs_filepath))
            abs_filepath = os.path.join(abs_filepath, 'index.html')
        return abs_filepath

    ####################################################################
    # 时间相关的操作
    @staticmethod
    def date_now(formats='%Y-%m-%d %H:%M:%S'):
        """获取当前时间"""
        # 当前时间多加一天
        #(datetime.datetime.now()+datetime.timedelta(days=1))
        #.strftime("%Y-%m-%d %H:%M:%S")

        # 当前时间多减一天
        #(datetime.datetime.now()+datetime.timedelta(days=1))
        #.strftime("%Y-%m-%d %H:%M:%S")

        # 多加一分钟
        #(datetime.datetime.now()+datetime.timedelta(minutes=1))
        # #时间加0.5天
        # offset = datetime.timedelta(days=0.5)
        # #时间加0.5小时
        # offset = datetime.timedelta(hours=0.5)
        # #时间加1分钟
        # offset = datetime.timedelta(minutes=1)
        # #时间加1秒钟
        # offset = datetime.timedelta(seconds=1)
        return datetime.datetime.now().strftime(formats)

    @staticmethod
    def date_str2date(str,formats="%Y-%m-%d %H:%M:%S"):
        """字符串转时间"""
        return datetime.datetime.strptime(str,formats)

    @staticmethod
    def  date_nginxTime2date(time,formats='%d/%b/%Y:%H:%M:%S'):
        """nginx 时间格式解析"""
        time = time.replace(" +0800", "") 
        return datetime.datetime.strptime(time, formats)
        