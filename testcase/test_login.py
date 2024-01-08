import pytest


# 读取数据
def read_yaml():
    return ['java', 'python', 'pytest']


@pytest.fixture(scope="function", autouse=False)
def exe_assert():
    print("----------接口开始前----------")
    yield
    print("----------接口结束后----------")


class TestLogin:

    def test_login(self):
        print("-------登录接口-------")

    def test_register(self, exe_assert):
        print("-------注册接口-------")

    def test_test(self):
        print("-------测试接口-------")
