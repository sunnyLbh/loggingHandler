# -*- coding: utf-8 -*-
"""
__author__ = 'Sunny'
__mtime__ = '6/23/2016'

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
from loggingHandler.logDef import logged
import logging
from loggingHandler.StaticFunc import ErrorCode,Set_return_dicts
from loggingHandler.MyExecption import ApiException

@logged(logging.ERROR)
def test():
    try:
        print ('in the function')
        raise ApiException(ErrorCode.JsonError)
    except ApiException as e:
        return Set_return_dicts(forWorker=e.error_result['forWorker'],
                                code=e.error_result['errorCode'],
                                forUser=e.error_result['forUser'])

a = test()
print (a)
