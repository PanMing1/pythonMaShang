import requests


class SendRequest:
    sess = requests.session()

    def all_send_request(self, method, url, **kwargs):
        print("----------开始接口测试----------")
        print("接口请求地址 %s" % url)
        res = SendRequest.sess.request(method, url, **kwargs)
        print("----------结束接口测试----------")
        return res
