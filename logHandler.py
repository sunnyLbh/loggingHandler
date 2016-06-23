# -*- coding: utf-8 -*-
"""
__author__ = 'Sunny'
__mtime__ = '6/18/2016'

                ┏┓     ┏┓
              ┏┛┻━━━┛┻┓
             ┃     ☃     ┃
             ┃ ┳┛  ┗┳  ┃
            ┃     ┻     ┃
            ┗━┓     ┏━┛
               ┃     ┗━━━┓
              ┃  神兽保佑   ┣┓
             ┃　永无BUG！  ┏┛
            ┗┓┓┏━┳┓┏┛
             ┃┫┫  ┃┫┫
            ┗┻┛  ┗┻┛
"""
import logging
class loggingHandler:
    def __init__(self,level=logging.DEBUG,filemode='a'):
        # %(name)s            Logger的名字
        # %(levelno)s         数字形式的日志级别
        # %(levelname)s       文本形式的日志级别
        # %(pathname)s        调用日志输出函数的模块的完整路径名，可能没有
        # %(filename)s        调用日志输出函数的模块的文件名
        # %(module)s          调用日志输出函数的模块名
        # %(funcName)s        调用日志输出函数的函数名
        # %(lineno)d          调用日志输出函数的语句所在的代码行
        # %(created)f         当前时间，用UNIX标准的表示时间的浮 点数表示
        # %(relativeCreated)d    输出日志信息时的，自Logger创建以 来的毫秒数
        # %(asctime)s         字符串形式的当前时间。默认格式是 “2003-07-08 16:49:45,896”。逗号后面的是毫秒
        # %(thread)d          线程ID。可能没有
        # %(threadName)s      线程名。可能没有
        # %(process)d         进程ID。可能没有
        # %(message)s         用户输出的消息
        format = '%(asctime)s--%(filename)s[line:%(lineno)d]--%(levelname)s  %(message)s'
        filename = 'F:/Users/python/workspace/Test_Books/loggingHandler/tmp/test.log'
        logging.basicConfig(level=level,format=format,filename=filename,filemode=filemode)

    def Debug(self,message):
        logging.debug(message)

    def info(self,message):
        logging.info(message)

    def warning(self,message):
        logging.warning(message)

    def error(self,message):
        logging.error(message)

    def critical(self,message):
        logging.critical(message)

