from rest_framework.views import exception_handler
from django.db import DatabaseError
from rest_framework.response import Response
from rest_framework import status

import logging



def custom_exception_handler(exc, context):
    """
    自定义异常处理类
    :param exc: 发生异常时的异常处理对象
    :param context:  抛出异常的上下文
    :return: Response响应对象
    """
    response = exception_handler(exc, context)
    if response is None:
        print(exc)
        view = context["view"]
        if isinstance(exc, DatabaseError):
            # 数据库异常
            return Response({"message": "数据库异常","code":200}, status=status.HTTP_507_INSUFFICIENT_STORAGE)
        if isinstance(exc, Exception):
            # redis异常
            print(exc)
            return Response({"message": "redis数据库异常","code":200}, status=status.HTTP_507_INSUFFICIENT_STORAGE)
    return Response({"code":500})