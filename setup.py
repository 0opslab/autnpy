#! /usr/bin/python
# coding=UTF-8
# version:python3.x

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
"""
这里这么写的目的是防止setup导入出错，安装出现异常。但一般不会出错
"""


setup(
    name='Autnpy',
    version='0.2.2',#该信息是必不可少的
    author='0opslab',
    author_email='909070781@qq.com',
    platforms='any',
    description='Autnpy universal function',
    license='MIT',
    packages=['',],#需要安装的代码包，也可以用find_packages函数
    # install_requires=['mako>=1.0.3',
    #                   ],#一些第三方账号，需要在这里申明。
    classifiers = [
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        ],#这也需要遵循标准格式
    keywords='Autnpy universal function',
    url='https://github.com/0opslab',
    zip_safe=True,#设为True，以zip的方式进行传输
    include_package_data=True,#字面意思就可理解
    
)