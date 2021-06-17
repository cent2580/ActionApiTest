import json
import os
import time
from functools import wraps

import allure
import requests
from aliyun_api_gateway_sign_py3.com.aliyun.api.gateway.sdk import client
from aliyun_api_gateway_sign_py3.com.aliyun.api.gateway.sdk.common import \
    constant
from aliyun_api_gateway_sign_py3.com.aliyun.api.gateway.sdk.http import request
from common.utils import file_binary

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def func_timer(function):
    @wraps(function)
    def function_timer(*args, **kwargs):
        start = time.time()
        result = function(*args, **kwargs)
        finished = time.time()
        result['response_time'] = float('%.2f' % (finished - start))
        allure.attach('Response: %s' % result, name='返回结果')
        return result

    return function_timer


config = {
    # 线上环境
    # 'appkey': '203901115',
    # 'secret': 'mDSXHrRsd4lGRsKe51uQgfnoD88pzvEG',
    'host': 'https://sig-server-api.firerock.tech:17001'

    # 线下环境
    # 'appkey': '203890949',
    # 'secret': 'Bv2LSuYJy5orvAoKk7Ze5LM1oOr7pOkL',
    # 'host': 'https://yh.firerock.tech:17001'
}


class Req:
    @classmethod
    @func_timer
    def base_req(cls, **kwargs):

        if 'host' in kwargs:
            host = kwargs['host']
            del kwargs['host']
        else:
            host = config['host']

        url = kwargs['url']
        method = kwargs['method']
        data = kwargs['data']

        try:
            filepath = os.path.join(BASE_DIR, kwargs['files'])
            kwargs['files'] = file_binary(filepath)
        except Exception:
            pass
        allure.attach('Request: %s' % kwargs, name='请求参数')

        api_gateway = None
        try:
            appkey = config['appkey']
            secret = config['secret']
            api_gateway = True
        except:
            api_gateway = False

        if api_gateway:
            if method == 'GET':
                url = url + '?' + '&'.join(
                    ['{}={}'.format(k, v) for k, v in data.items()])
                req = request.Request(host=host,
                                      method='GET',
                                      url=url,
                                      time_out=3000)
            elif method == 'POST':
                req = request.Request(host=host,
                                      method='POST',
                                      url=url,
                                      time_out=3000)
                req.set_body(data)
                req.set_content_type(constant.CONTENT_TYPE_FORM)
            else:
                allure.attach('请求方式错误...')

            cli = client.DefaultClient(appkey, secret)
            res = cli.execute(req)
            res_code = res[0]
            res_headers = res[1]
            res_body = res[2]
            if res_code >= 400:
                allure.attach("网关请求失败：%s" % str(res))
                return
            else:
                res_body_obj = json.loads(res_body)
                if res_body_obj['code'] >= 400:
                    allure.attach("请求失败: %s" % str(res_body))
                    return
                else:
                    return res_body_obj
        else:
            kwargs['url'] = host + url
            try:
                res = requests.request(**kwargs)
                res.raise_for_status()  # 如果响应状态码不是 200，则主动抛出异常
            except requests.RequestException as e:
                allure.attach('Error: %s' % str(e), name='请求错误')
            else:
                return res.json()
