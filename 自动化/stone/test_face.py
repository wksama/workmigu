#!/usr/bin/env python
# -*- coding:utf8 -*-

import os
import sys
import json
import requests
import argparse
import hashlib
import base64
import time

import pdb
import random


def encrypt_base64(content, encode_type='utf-8'):
    return base64.b64encode(content.encode(encode_type)).decode(encode_type)


# url = 'http://127.0.0.1:28240/face_recognition/v1/register'
# url = 'http://10.194.33.4:9050/face_recognition/v1/register'
url = 'http://10.194.32.19:9050/face_recognition/v1/register'
# url='http://221.178.45.217:8082/face_recognition/v1/request'
app_id = 'humanrec'
api_key = '2607deabbae1cc4c57c868774e4bb03e'
capabilityname = 'face_recognition00000000'
# url = 'http://10.194.33.4:9050/2d_humanpose/v1/request'
uuid = random.randint(00000000000000000000000000000000, 99999999999999999999999999999999)
# csid = app_id + capabilityname + str(uuid)
csid = app_id + capabilityname + str(uuid)
xsvr_par_dict = {"appid": app_id, "csid": csid}
# print(xsvr_par_dict)
xsvr_par_json = json.dumps(xsvr_par_dict)
xsvr_par_encode = encrypt_base64(xsvr_par_json)
print('xsvr_par_encode:::', xsvr_par_encode)
x_time = str(int(time.time()))
print('x_time:::', x_time)
hash = hashlib.md5()
hash.update((api_key + x_time + xsvr_par_encode).encode("utf8"))
x_chksum = hash.hexdigest()
print('x_chksum:::', x_chksum)

header = {
    # "Content-Type": "application/x-www-form-urlencoded;charset=utf-8",
    "X-Server-Param": xsvr_par_encode,
    "X-CurTime": x_time,
    "X-CheckSum": x_chksum
}


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--image_path', type=str, default="data/normal/real_face")
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = get_args()
    # image_path = args.image_path
    # image_path = 'D:\PycharmProjects\code\img'
    image_path = 'E:\abcd'
    inputs = []

    if os.path.isdir(image_path):  # 读取目录
        img_paths = os.listdir(image_path)
        for img_path in img_paths:
            img_path = os.path.join(image_path, img_path)
            with open(img_path, 'rb') as  f:
                image_data = base64.b64encode(f.read())
            inputs.append(image_data)
    elif os.path.isfile(image_path):  # 读单张图片
        with open(image_path, 'rb') as  f:
            image_data = base64.b64encode(f.read())
        inputs.append(image_data)
    else:
        print("inputs error!")
        sys.exit(-1)

    for image_data in inputs:
        md5hash = hashlib.md5(image_data)
        image_id = md5hash.hexdigest()


        # header = {}
        data = {
            "data": image_data.decode(),
            "image_id": image_id,
        }
        # response = requests.post(url=url, headers=header)
        response = requests.post(url=url, headers=header, data=data)
        print('header',header)
        print("response.headers::::", response.headers)
        print("response.text::::::", response.text)
        # response = requests.post(url=url, headers=header)
        output_json = json.loads(response.text)
        print("output_json:::::", output_json)
        data = output_json['data']
        results = base64.b64decode(data).decode()
        print("results:::::", results)
        print('---------------------------------')
