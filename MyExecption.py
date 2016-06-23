# -*- coding: utf-8 -*-
"""
__author__ = 'Sunny'
__mtime__ = '4/15/2016'

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
from loggingHandler.StaticFunc import ErrorCode

class ApiException(Exception):
    '''全局错误码exception，搭配ErrorCode使用'''
    @staticmethod
    def get_for_worker(errorCode):
        return ErrorCode.ERROR_MESSAGE.get(errorCode, 2000)['forWorker']

    @staticmethod
    def get_for_user(errorCode):
        return ErrorCode.ERROR_MESSAGE.get(errorCode, 2000)['forUser']

    @staticmethod
    def get_error_result(errorCode):
        return {
            "forWorker": ApiException.get_for_worker(errorCode),
            "errorCode": str(errorCode),
            'forUser' : ApiException.get_for_user(errorCode)
        }

    @property
    def error_result(self):
        return self.get_error_result(self.errorCode)

    def __init__(self, errorCode=None):
        self.errorCode = errorCode
        self.message = self.get_for_worker(self.errorCode)
        self.forUser = self.get_for_user(self.errorCode)
