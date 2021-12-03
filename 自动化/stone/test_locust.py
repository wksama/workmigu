from locust import HttpUser, task, between, events
from locust.runners import MasterRunner, WorkerRunner

import os
import sys
import json
import requests
import argparse
import hashlib
import base64
import time
import uuid

import pdb
import random


def encrypt_base64(content, encode_type='utf-8'):
    return base64.b64encode(content.encode(encode_type)).decode(encode_type)


app_id = 'humanrec'
api_key = '30f2d2f55015074b4d584ad1d1813096'
capabilityname = 'face_recognition00000000'

uuid = uuid.uuid4().hex
csid = app_id + capabilityname + str(uuid)
xsvr_par_dict = {"appid": app_id, "csid": csid}
# print(xsvr_par_dict)
xsvr_par_json = json.dumps(xsvr_par_dict)
xsvr_par_encode = encrypt_base64(xsvr_par_json)
x_time = str(int(time.time()))
hash = hashlib.md5()
hash.update((api_key + x_time + xsvr_par_encode).encode("utf8"))
x_chksum = hash.hexdigest()
header = {
    # "Content-Type": "application/x-www-form-urlencoded;charset=utf-8",
    "X-Server-Param": xsvr_par_encode,
    "X-CurTime": x_time,
    "X-CheckSum": x_chksum}



class QuickstartUser(HttpUser):
    wait_time = between(0, 1)
    weight = 10

    def on_start(self):
        pass

    @task
    def task1(self):

        image_path = 'D:\img'
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

            data = {
                "data": image_data.decode(),
                "image_id": image_id,
            }

            self.client.post("/face_recognition/v1/register", headers=header, data=data)
