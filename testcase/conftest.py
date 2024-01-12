'''
@Project ：publicdemo 
@File    ：conftest.py
@Author  ：PanMing
@Date    ：2024/1/9 17:51 
'''
import pytest

from common.yaml_util import clear_yaml


# @pytest.fixture(scope="function", autouse=True, params=read_yaml(), name='ea')
@pytest.fixture(scope="session", autouse=True)
def exe_assert():
    clear_yaml()
