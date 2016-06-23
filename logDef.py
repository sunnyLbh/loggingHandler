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
from functools import wraps
from loggingHandler.MyExecption import ApiException
format = '%(asctime)s--%(filename)s[line:%(lineno)d]--%(levelname)s: %(message)s'
filename = 'F:/Users/python/workspace/Test_Books/loggingHandler/tmp/test.log'
logging.basicConfig(format=format,filename=filename)

def logged(level):
    def decorate(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            try:
                result = func(*args,**kwargs)
                return result
            except ApiException as e:
                logging.log(level,e.error_result['msg'])
                raise

        return wrapper
    return decorate

