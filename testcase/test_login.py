import pytest


# 读取数据
def read_yaml():
    return ['java', 'python', 'pytest']


class TestLogin:
    def test_login(self):
        print("-------登录接口-------")

    def test_register(self):
        print("-------注册接口-------")

    def test_test(self):
        print("-------测试接口-------")
