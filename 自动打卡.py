#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/5/25 11:45
# @Author  : chy
# @Site    : 
# @File    : 自动打卡.py
# @Software: PyCharm
import requests
import time
import base64
import json

headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.62 XWEB/2693 MMWEBSDK/201001 Mobile Safari/537.36 MMWEBID/7311 MicroMessenger/7.0.20.1781(0x27001439) Process/appbrand2 WeChat/arm64 NetType/4G Language/zh_CN ABI/arm64",
    "Referer": "https://servicewechat.com/wx8227f55dc4490f45/76/page-frame.html"
}
key = {
    'xh': 'S211231006',
    'timestamp': time.time(),
}
print(key['timestamp'])
key_base64 = base64.b64encode(json.dumps(key).encode('utf-8'))
key = {
    'key': key_base64
}

r = requests.post('https://we.cqupt.edu.cn/api/yjs_mrdk/get_yjs_mrdk_flag.php', data=key)
r_dict = json.loads(r.text)
if r_dict["data"]["count"] == "1":
    print("打了")
else:
    params = {
        'address': '重庆市南岸区江南水岸二组团七栋',
        'key': "PULBZ-BSEWU-MAEVV-2IAJR-ZCAS3-53F4O"
    }
    r = requests.get("https://apis.map.qq.com/ws/geocoder/v1/", params=params)
    print(r.text)
    r_dict = json.loads(r.text)
    print(r_dict)
    mrdk_dit = {
        'openid': '',
        'timestamp': time.time(),
        'xh': 'S211231006',
        'name': '陈泓宇',
        'xb': '男',
        'szdq': r_dict["result"]["address_components"]["province"] + r_dict["result"]["address_components"]["city"] +
                r_dict["result"]["address_components"]["district"],
        'xxdz': '重庆市南岸区江南水岸二组团七栋',
        'locationBig': '中国' + r_dict["result"]["address_components"]["province"] +
                       r_dict["result"]["address_components"][
                           "city"] + r_dict["result"]["address_components"]["district"],
        'locationSmall': r_dict["result"]["address_components"]["city"] + r_dict["result"]["address_components"][
            "district"] + r_dict['result']["title"],
        'latitude': r_dict["result"]["location"]["lng"],
        'longitude': r_dict["result"]["location"]["lat"],

        'ywjcqzbl': '低风险',
        'ywjchblj': '无',
        'xjzdywqzbl': '无',
        'twsfzc': '是',
        'ywytdzz': '无',
        'jkmresult': '绿色',
        'beizhu': '无'
    }
    print(mrdk_dit)
    mrdk_base64 = base64.b64encode(json.dumps(mrdk_dit).encode('utf-8'))
    data = {
        'key': mrdk_base64
    }
    r = requests.post("https://we.cqupt.edu.cn/api/yjs_mrdk/post_yjs_mrdk_info.php", headers=headers, data=data)
    print(r.text)
