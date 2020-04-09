import pytest
import requests
from common.func import *
import logging
logger = logging.getLogger('test')
logger.setLevel(logging.DEBUG)  # 输出所有大于DEBUG级别的log
# 设置日志输出格式
fmt = logging.Formatter('%(filename)-6s: %(levelname)-6s %(asctime)s: %(message)s')
stream_hdl = logging.StreamHandler()
stream_hdl.setFormatter(fmt)
stream_hdl.setLevel(logging.DEBUG)
logger.addHandler(stream_hdl)



class TestVip1(object):
    data=read_yaml()
    url = data["api_url"]["test_api"]
    def test_token(self):
        method = "get"
        params = {"corpid": "ww697527423c75e5e0",
                  "corpsecret": "JsDsbtVAFRDaGWsBN_RVze1e-F6Uzmhk-WvBMxfbCNg"}
        r = requests.request(method, self.url + "/gettoken", params=params).json()
        ##print(r["access_token"])
        access_token = r["access_token"]
        logger.debug("获取token")
        return access_token

    def test_creat_depament(self):
        print(self.test_token())
        access_token=self.test_token()
        method = "post"
        params = {"access_token": access_token}
        json={"name":"中软测试",
              "parentid":1}
        r=requests.request(method,self.url+"/department/create",params=params,json=json).json()
        print(r)
    def test_list_depament(self):
        access_token = self.test_token()
        method = "get"
        params = {"access_token": access_token}
        r= requests.request(method,self.url+"/department/list",params=params).json()
        print(r)
