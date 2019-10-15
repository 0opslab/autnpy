#! /usr/bin/python
# coding=UTF-8
# version:python3.x
import datetime
import logging
import os
import shutil
import fnmatch

"""封装一些常用的方法，方便操作
@author 0opslab
@url https://github.com/0opslab
"""

# 常用的一些爬虫user-agent
WEBUTIL_SPIDER = ['spider', 'Baiduspider', 'Googlebot', '360Spider', 'bingbot', 'Yahoo', 'iaskspider', 'YodaoBot',
                  'msnbot', 'libcurl-agent', 'CFNetwork', 'okhttp', 'urllib', 'Python-urllib', 'HttpClient',
                  'Go-http-client', 'AHC', 'masscan']


def trim_path(file_name):
    """返回标准的路径"""
    return os.path.normpath(file_name).replace("\\", "/")


def base_path(file=''):
    """获取当前路径下的开始文件的全路径"""
    return trim_path(os.getcwd().replace("\\", "/").split("src/")[0] + file)


def md5str(*args):
    """获取字符串的md5"""
    import hashlib
    datastr = ""
    for x in args:
        datastr = datastr + str(x)
    m = hashlib.md5(datastr.encode(encoding='utf-8'))
    return m.hexdigest()


def logger(modeule_name, log_file="run.log"):
    """Initialize logging module."""
    log = logging.getLogger(modeule_name)
    formatter = logging.Formatter('%(asctime)s-(%(name)s)-[%(levelname)s] %(message)s')
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


def date_now(formats='%Y-%m-%d %H:%M:%S'):
    """获取当前时间"""
    return datetime.datetime.now().strftime(formats)


def load_keyvalue(host, user, password, database, key, charset="utf8"):
    """从数据库中获取配置
      CREATE TABLE `t_sys_keyvalue` (
      `buskey` varchar(10) NOT NULL COMMENT '业务主键',
      `busName` varchar(60) NOT NULL COMMENT '业务名称',
      `used` char(1) DEFAULT '1',
      `busValue` varchar(4000) NOT NULL COMMENT 'value值-建议配置JSON串',
      `createtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
      `REMARK` char(100) DEFAULT NULL COMMENT '备注信息',
      PRIMARY KEY (`buskey`),
      UNIQUE KEY `T_SYS_KEYVALUE_buskey_uindex` (`buskey`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='keyvalue配置表';
    """
    import pymysql
    try:
        sql = "SELECT busValue FROM t_sys_keyvalue t where t.buskey='%s'"
        conn = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            charset=charset,
        )

        csor = conn.cursor()
        csor.execute(sql % key)
        results = csor.fetchall()
        for row in results:
            return row[0]

        csor.close()
        conn.close()
    except Exception as es:
        print(es)

    return None


def hash_file(fine_name, hashtype="sha256", block_size=64 * 1024):
    """ Support md5(), sha1(), sha224(), sha256(), sha384(), sha512(),
    blake2b(), blake2s(),sha3_224, sha3_256, sha3_384, sha3_512,
    shake_128, and shake_256
    """
    import hashlib
    with open(fine_name, 'rb') as file:
        fhash = hashlib.new(hashtype, b"")
        while True:
            data = file.read(block_size)
            if not data:
                break
            fhash.update(data)
        return fhash.hexdigest()


def zip_dir(dirname, zipfilename):
    """
    @函数目的: 压缩指定目录为zip文件
    @参数说明：dirname为指定的目录，zipfilename为压缩后的zip文件路径
    """
    import zipfile
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


def unzip_file(zipfilename, unziptodir):
    """
    | ##@函数目的: 解压zip文件到指定目录
    | ##@参数说明：zipfilename为zip文件路径，unziptodir为解压文件后的文件目录
    | ##@返回值：无
    | ##@函数逻辑：
    """
    import zipfile
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


def read_file_prefix(file, lens):
    """读取文件的前lens个字节"""
    with open(file, "rb") as temp:
        prefix = ''.join(['%02x' % b for b in bytes(temp.read(lens))])
        return prefix


def del_path(path):
    """删除目录"""
    ls = os.listdir(path)
    for i in ls:
        c_path = os.path.join(path, i)
        if os.path.isdir(c_path):
            del_path(c_path)
        else:
            os.remove(c_path)
    os.rmdir(path)


def dedupe(items, key=None):
    """字典列表去重"""
    """
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


def list_file(path, fun, suffix='*'):
    """罗列从某个文件夹下的某一类文件，可以使用通配符
        path：路径
        fun：处理函数
        suffix：匹配指定规则的文件
    """
    for root, dirs, files in os.walk(path):
        for file in files:
            if fnmatch.fnmatch(file, suffix):
                fun(os.path.join(root, file))
