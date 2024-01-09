'''
@Project ：publicdemo 
@File    ：conftest.py
@Author  ：PanMing
@Date    ：2024/1/9 17:51 
'''
import pytest

from testcase.test_login import read_yaml


# @pytest.fixture(scope="function", autouse=True, params=read_yaml(), name='ea')
@pytest.fixture(scope="function", autouse=True)
def exe_assert():
    print("----------接口开始前----------")
    yield
    print("----------接口结束后----------")
