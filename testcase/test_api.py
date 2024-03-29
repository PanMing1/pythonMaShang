import time

import pytest

from common.send_request import SendRequest
from common.yaml_util import write_yaml, read_yaml, read_test_yaml


class TestApi:

    # 测试get使用
    # def test_get_token(self):
    #     print("测试1")
    #     url = "http://192.168.100.35:81/formmodel/formInfo/list"
    #     dates = {
    #         "t": int(time.time() * 1000),
    #         "formName": "ZH-RE-TSD-000034"
    #     }
    #     headers = {
    #         "token": "7b93dc6488284c7d4191dcd703acc952",
    #         "Content-Type": "application/json"
    #     }
    #     res = SendRequest().all_send_request(method="get", url=url, params=dates, headers=headers)
    #     # res = requests.get(url=url, params=dates, headers=headers)
    #     print(res.json())

    # 登录，获取token  接口（系统登录）
    @pytest.mark.parametrize("caseinfo", read_test_yaml("/testcase/get_token.yaml"))
    def test_post_token(self, caseinfo):
        url = 'http://192.168.100.35:81/security/sys/login'
        json = {"t": int(time.time() * 1000), "username": "admin", "password": "zhre2021!@#$"}
        res = SendRequest().all_send_request(method=caseinfo["request"]["method"],
                                             url=caseinfo["request"]["url"],
                                             json=caseinfo["request"]["json"])

        result = res.json()
        TestApi.access_token = result["token"]
        write_yaml({"token": result["token"]})
        print(result)

    # 使用token，给自己获得权限  接口（工作量统计列表查询）
    def test_edit_flag(self):
        url = "http://192.168.100.35:81/logistics/order/job/statistics/list"
        json = {"t": int(time.time() * 1000), "page": 1, "limit": 10, "wheelsetCode": "ZQ GBD 00002", "carGroup": "",
                "status": "", "month": "2023-07", "deliverDate": "", "finishedTime": "", "deliverType": ""}
        headers = {
            "token": read_yaml("token")
        }
        res = SendRequest().all_send_request(method="post", url=url, json=json, headers=headers)
        result = res.json()
        print(result)

    # 文件上传
    # def test_file_upload(self):
    #     url = "http://192.168.100.35:81/security/sys/userext/upload"
    #     dates1 = {
    #         "file": open("C:\\Users\\mg_sa\\Desktop\\1\\ZH0160.png", mode='rb')
    #
    #     }
    #
    #     detes2 = {
    #         "staffCode": "adminjx",
    #         # "filename": "ZH0160.png",
    #         "Content-Type": "image/png"
    #     }
    #     res = SendRequest().all_send_request(method="post", url=url, files=dates1, data=detes2)
    #     # res = requests.post(url=url, files=dates1, data=detes2)
    #     result = res.json()
    #     print(result)
