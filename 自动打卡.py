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
import os

openid = os.environ['openid']
xh = os.environ['xh']
server = os.environ['server']
headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.62 XWEB/2693 MMWEBSDK/201001 Mobile Safari/537.36 MMWEBID/7311 MicroMessenger/7.0.20.1781(0x27001439) Process/appbrand2 WeChat/arm64 NetType/4G Language/zh_CN ABI/arm64",
    "Referer": "https://servicewechat.com/wx8227f55dc4490f45/76/page-frame.html"
}

key = {
    'xh': 'S211231006',
    'timestamp': time.time()
}


def encode(key):
    encoded_key = base64.b64encode(json.dumps(key).encode('utf-8'))
    return {
        'key': encoded_key
    }


def mrdk_status(key):
    i = 0
    while i < 3:
        try:
            r = requests.post('https://we.cqupt.edu.cn/api/yjs_mrdk/get_yjs_mrdk_flag.php', data=encode(key),
                              timeout=5)
            r_dict = json.loads(r.text)
            return r_dict['data']['count']
        except requests.exceptions.RequestException as e:
            print(e.strerror)
            i += 1


def sendToWechat(param):
    i = 0
    while i < 3:
        try:
            r = requests.post(f'https://sctapi.ftqq.com/{server}.send', data=param, timeout=5)
            return
        except requests.exceptions.RequestException as e:
            i += 1
            print(e.re)


def getposition(param):
    i = 0
    while i < 3:
        try:
            r = requests.get("https://apis.map.qq.com/ws/geocoder/v1/", params=params)
            r_dict = json.loads(r.text)
            return r_dict
        except requests.exceptions.RequestException as e:
            i += 1
            print(e.re)


def dk(param):
    i = 0
    while i < 3:
        try:
            r = requests.post("https://we.cqupt.edu.cn/api/yjs_mrdk/post_yjs_mrdk_info.php", headers=headers,
                              data=encode(mrdk_dict))
            if r.status_code == 200:
                param_server = {
                    'title': '打卡结果',
                    'desp': '已成功打卡'
                }
                sendToWechat(param_server)
                return
            else:
                param_server = {
                    'title': '打卡结果',
                    'desp': '打卡失败'
                }
                sendToWechat(param_server)
                return
        except requests.exceptions.RequestException as e:
            i += 1
            print(e.re)


# if mrdk_status(key) != "0":
    params = {
        'address': '重庆市南岸区江南水岸二组团七栋',
        'key': "PULBZ-BSEWU-MAEVV-2IAJR-ZCAS3-53F4O"
    }

    r_dict = getposition(params)
    mrdk_dict = {
        'openid': openid,
        'timestamp': time.time(),
        'xh': xh,
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
    dk(mrdk_dict)

# else:
    print("打了")
    param_server = {
        'title': '每日打卡',
        'desp': '今日已打卡'
    }
    sendToWechat(param_server)
