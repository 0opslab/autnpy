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
    name='autnpy',
    version='0.2.4',
    author='0opslab',
    author_email='909070781@qq.com',
    platforms='any',
    description='Autnpy universal function',
    license='MIT',
    packages=['autnpy'],
    # install_requires=['mako>=1.0.3',               ],
    classifiers = [
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        ],
    keywords='Autnpy universal function',
    url='https://github.com/0opslab',
    zip_safe=True,
    include_package_data=True,
    
)