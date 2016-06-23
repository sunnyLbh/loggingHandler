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

class ErrorCode():
    QueryLangFormatError = 1000   #接口查询语言语法出错
    NoneData = 1002                  # 没有数据
    DataUnSave = 1003                # 数据无法保存
    JsonError = 1004                 #接收的JSON格式出错
    TokenSessionError = 1005         #TokenSession失效
    MethodError = 1006               #错误的请求方式

    ParameterError = 1100            #参数错误
    ParameterMiss = 1101             #参数缺失
    ErrorRequest = 1102              #错误的请求

    ErrorFindCode = 2000             #未识别错误码

    ERROR_MESSAGE = {
        QueryLangFormatError: {'forWorker':u"查询语言语法出错,请检查语法",
                                      'forUser':u"查询语言语法出错,请检查语法"},
        NoneData: {'forWorker':u"没有数据",
                   'forUser':u"没有数据"},
        DataUnSave: {'forWorker':u"数据无法保存",
                     'forUser':u"数据无法保存"},
        JsonError : {'forWorker':u"接收的JSON格式出错",
                     'forUser':u"请求错误"},
        TokenSessionError : {'forWorker':u"TokenSession失效",
                             'forUser':u"请求错误"},
        MethodError : {'forWorker':u"请求方式出错",
                             'forUser':u"请求错误"},

        ParameterError: {'forWorker':u"不合法的参数",
                         'forUser':u"请求错误"},
        ParameterMiss: {'forWorker':u"参数缺失",
                        'forUser':u"请求错误"},
        ErrorRequest : {'forWorker':u"请求错误",
                        'forUser':u"请求错误"},

        ErrorFindCode : {'forWorker':u"未识别错误码",
                          'forUser':u"请求错误"}
    }

#设置返回值
#forUser是显示给用户看的文字，forWorker是显示提供给后台程序员看的字段
#ret代表成功或者失败，data代表返回值，result代表错误代码
def Set_return_dicts(data=None,forUser='',code=200,ret='success',forWorker=''):
    import json
    if data == None:
       ret = 'failure'

    return_dicts = {
        'data' : data,
        'forUser' : forUser,
        'code' : code,
        'ret' : ret,
        'version' : '1.0',
        'forWorker' : forWorker
    }
    return return_dicts