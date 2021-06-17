import json
import os
from re import X
from string import Template

import allure
import pytest
from requests import api
import yaml
from jsonpath import jsonpath
from common.utils import read_yaml

from base import Req

APIDIR = os.path.join(os.path.dirname(__file__), 'api')


def pytest_collect_file(parent, path):
    '''收集用例'''
    if path.ext == ".yaml" and path.basename.startswith("test"):
        return YamlFile.from_parent(parent, fspath=path)


def pytest_collection_modifyitems(items):
    items.sort(key=lambda x: x.spec['tcid'])  # 根据tcid排序


class YamlFile(pytest.File):
    def collect(self):
        raw = yaml.safe_load(self.fspath.open(encoding='utf8'))
        for spec in raw:
            name = spec['tcname']
            yield YamlItem.from_parent(self, name=name, spec=spec)


class YamlItem(pytest.Item):
    def __init__(self, name, parent, spec):
        super().__init__(name, parent)
        self.g = globals()
        self.spec = spec
        self.tc = self.spec['tc']

    def setup(self):
        '''
        Item 对象的初始化步骤, 同样还有teardown方法, 这里省略
        :return:
        '''
        if 'setup' in self.spec:
            with allure.step('前置'):
                self.runner(self.spec['setup'])

    def teardown(self):
        if 'teardown' in self.spec:
            with allure.step('后置'):
                self.runner(self.spec['teardown'])

    def runtest(self):
        '''运行用例'''
        self.runner(self.tc)

    def runner(self, data):
        for item in data:
            if item.get('action'):
                action = item['action']
                action_type = action[0]
                api_path = os.path.join(APIDIR, action[1])
                api_name = action[2]
                response = self.operate(action_type, api_path, api_name)
            if item.get('extract'):
                extract = item['extract']
                for key, value in extract.items():
                    self.g[key] = jsonpath(response, value)[0]
            if item.get('validate'):
                validate = self.values_render_variable(item['validate'])
                self.assert_response(response, validate)

    def operate(self, action_type, api_path, api_name):
        '''执行action'''
        if action_type == 'req':
            with allure.step(api_name):
                api_data = read_yaml(api_path)[api_name]
                response = self.req(**api_data['request'])
                if api_data.get('validate'):
                    validate = self.values_render_variable(
                        api_data['validate'])
                    self.assert_response(response, validate)
                return response

    def req(self, **kwargs):
        '''请求接口'''
        new_request_data = self.values_render_variable(kwargs)
        # print(new_request_data)
        response = Req.base_req(**new_request_data)
        # print(response)
        return response

    def values_render_variable(self, template):
        '''替换变量'''
        try:
            template_values = Template(json.dumps(template)).safe_substitute(
                self.g)
            values = yaml.safe_load(template_values)
            return values
        except Exception as e:
            allure.attach(e)

    def assert_response(self, response, validate):
        '''设置断言'''
        with allure.step('校验'):
            for v in validate:
                if v.get('eq'):
                    expr = v.get("eq")[1]
                    actual_result = jsonpath(response, expr)
                    print(actual_result)
                    expect_result = v.get("eq")[2]
                    if v.get("eq")[0] == "==":
                        assert actual_result[0] == expect_result
                        allure.attach("实际结果：%s，期望等于：%s" %
                                      (actual_result[0], expect_result),
                                      name="%s的断言" % expr)
                    elif v.get("eq")[0] == "!=":
                        assert expect_result != actual_result[0]
                        allure.attach("实际结果：%s，期望不等于：%s" %
                                      (actual_result[0], expect_result),
                                      name="%s的断言" % expr)
                    elif v.get("eq")[0] == "num":
                        assert len(actual_result[0]) == expect_result
                        allure.attach("实际结果：%s，期望数量：%s" %
                                      (actual_result[0], expect_result),
                                      name="%s的断言" % expr)
                    elif v.get("eq")[0] == "<":
                        assert actual_result[0] < expect_result
                        allure.attach("实际结果：%s，期望小于：%s" %
                                      (actual_result[0], expect_result),
                                      name="%s的断言" % expr)
                    elif v.get("eq")[0] == "contains":
                        assert expect_result in actual_result
                        allure.attach("实际结果：%s，期望包含：%s" %
                                      (actual_result[0], expect_result),
                                      name="%s的断言" % expr)
                    elif v.get("eq")[0] == "nocontains":
                        assert expect_result not in actual_result
                        allure.attach("实际结果：%s，期望包含：%s" %
                                      (actual_result[0], expect_result),
                                      name="%s的断言" % expr)

    def reportinfo(self):
        return self.fspath, 0, f"usecase: {self.name}"

    def repr_failure(self, excinfo):
        """Called when self.runtest() raises an exception."""
        if isinstance(excinfo.value, YamlException):
            error_info = "\n".join([
                "usecase execution failed",
                "   spec failed: {1!r}: {2!r}".format(*excinfo.value.args),
                "   no further details known at this point.",
            ])
            allure.attach('%s：%s' % (self.parent, error_info))
            return error_info


class YamlException(Exception):
    pass
    """Custom exception for error reporting."""
