# -*- encoding=utf8 -*-
__author__ = "SMZ"

from airtest.core.api import *

auto_setup(__file__)

# 获取当前设备的分辨率
width, height = device().get_current_resolution()
print(width, height)

touch(Template(r"tpl1634698338443.png", record_pos=(-0.18, -0.207), resolution=(1080, 1920)))

sleep(15)
'''用户协议操作'''
try:
    if exists(Template(r"tpl1634698545241.png", record_pos=(0.225, 0.784), resolution=(1080, 1920))) is not False:
        touch(Template(r"tpl1634698588108.png", record_pos=(0.228, 0.787), resolution=(1080, 1920)))
    else:
        print("%s%s%s"  % ('-'*10, '非首次打开，已点击过', '-'*10))
except:
    print("%s%s%s"  % ('-'*10, '用户协议点击出现问题', '-'*10))

sleep(3)
'''开启界面操作'''
try:
    # 界面滑动
    if exists(Template(r"tpl1634717435742.png", threshold=0.8, rgb=True, record_pos=(0.001, 0.836), resolution=(1080, 1920))) is not False:
        for _ in range(10):
            swipe((0.8*width, 0.5*height), (0.01*width, 0.5*height))
            if exists(Template(r"tpl1634717861932.png", record_pos=(0.004, 0.718), resolution=(1080, 1920))) is not False:
                break
        sleep(1)
        touch(Template(r"tpl1634717980478.png", record_pos=(0.003, 0.715), resolution=(1080, 1920)))
    else:
        print("%s%s%s"  % ('-'*10, '开启界面，已点击过', '-'*10))
except:
    print("%s%s%s"  % ('-'*10, '开启界面出现问题', '-'*10))

sleep(5)
'''未成年协议操作'''
try:
    if exists(Template(r"tpl1634718493086.png", threshold=0.7, rgb=False, record_pos=(0.002, 0.263), resolution=(1080, 1920))) is not False:
        touch(Template(r"tpl1634724621582.png", record_pos=(0.002, 0.264), resolution=(1080, 1920)))
    else:
        print("%s%s%s"  % ('-'*10, '未成年协议，已点击过', '-'*10))
except:
    print("%s%s%s"  % ('-'*10, '未成年协议出现问题', '-'*10))

sleep(2)
'''登录操作'''
try:
    # 操作我的页
    if exists(Template(r"tpl1634719512909.png", rgb=True, record_pos=(-0.375, 0.833), resolution=(1080, 1920))) is not False:
        touch(Template(r"tpl1634778244629.png", record_pos=(-0.373, 0.835), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1634719202375.png", rgb=True, record_pos=(-0.378, 0.836), resolution=(1080, 1920))) is not False:
        touch(Template(r"tpl1634719102262.png", rgb=True, record_pos=(-0.378, 0.833), resolution=(1080, 1920)))
    else:
        print("%s%s%s"  % ('-'*10, '未找到我的tab', '-'*10))
    sleep(2)
    # 操作点击登录
    if exists(Template(r"tpl1634719343582.png", record_pos=(-0.283, -0.676), resolution=(1080, 1920))) is not False:
        touch(Template(r"tpl1634719369574.png", record_pos=(-0.281, -0.671), resolution=(1080, 1920)))
    else:
        print("%s%s%s"  % ('-'*10, '未找到点击登录', '-'*10))
    sleep(2)  
    # 操作密码登录

    if exists(Template(r"tpl1634722626865.png", threshold=0.85, record_pos=(-0.206, -0.643), resolution=(1080, 1920))) is not False:
        touch(Template(r"tpl1634722087118.png", record_pos=(-0.394, -0.2), resolution=(1080, 1920)))
        # 键入登录账号密码
        sleep(2)
        touch((0.1*width, 0.185*height))
        text("18814523086")
        sleep(1)
        touch((0.1*width, 0.25*height))
        text("Z862456169")
        sleep(1)
        touch(Template(r"tpl1634723413489.png", record_pos=(0.005, -0.279), resolution=(1080, 1920)))
        sleep(3) # 登录联网耗时
        
        if exists(Template(r"tpl1634720655710.png", record_pos=(0.235, 0.335), resolution=(1080, 1920))) is not False:
            touch(Template(r"tpl1634720682743.png", record_pos=(0.229, 0.334), resolution=(1080, 1920)))
        if exists(Template(r"tpl1634720755276.png", record_pos=(-0.1, -0.031), resolution=(1080, 1920))) is not False:
            print("账号或密码错误")
        
        if exists(Template(r"tpl1634721110510.png", record_pos=(-0.136, -0.153), resolution=(1080, 1920))) is not False:
            touch(Template(r"tpl1634721126111.png", record_pos=(0.151, 0.218), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1634722447311.png", threshold=0.85, record_pos=(-0.369, -0.73), resolution=(1080, 1920))) is not False:
        # 键入登录账号密码
        sleep(2)
        touch((0.1*width, 0.185*height))
        text("18814523086")
        sleep(1)
        touch((0.1*width, 0.25*height))
        text("Z862456169")
        sleep(1)
        touch(Template(r"tpl1634723382928.png", record_pos=(0.003, -0.278), resolution=(1080, 1920)))
        sleep(3) # 登录联网耗时
        if exists(Template(r"tpl1634720655710.png", record_pos=(0.235, 0.335), resolution=(1080, 1920))) is not False:
            touch(Template(r"tpl1634720682743.png", record_pos=(0.229, 0.334), resolution=(1080, 1920)))
        if exists(Template(r"tpl1634720755276.png", record_pos=(-0.1, -0.031), resolution=(1080, 1920))) is not False:
            print("账号或密码错误")
        
        if exists(Template(r"tpl1634721110510.png", record_pos=(-0.136, -0.153), resolution=(1080, 1920))) is not False:
            touch(Template(r"tpl1634721126111.png", record_pos=(0.151, 0.218), resolution=(1080, 1920)))
    else:
        print("%s%s%s"  % ('-'*10, '未找到密码登录', '-'*10))
    
    if exists(Template(r"tpl1634721325288.png", rgb=True, record_pos=(-0.381, 0.835), resolution=(1080, 1920))) is not False:
        touch(Template(r"tpl1634777912863.png", record_pos=(-0.379, 0.833), resolution=(1080, 1920)))
        sleep(1)

        if exists(Template(r"tpl1634721370078.png", record_pos=(-0.282, -0.676), resolution=(1080, 1920))) is False:
            print("%s%s%s"  % ('-'*10, '账号登录成功', '-'*10))
    elif exists(Template(r"tpl1634721449301.png", rgb=True, record_pos=(-0.375, 0.836), resolution=(1080, 1920))) is not False:
        touch(Template(r"tpl1634721488771.png", record_pos=(-0.378, 0.833), resolution=(1080, 1920)))
        sleep(1)
        if exists(Template(r"tpl1634721518690.png", record_pos=(-0.282, -0.671), resolution=(1080, 1920))) is False:
            print("%s%s%s"  % ('-'*10, '账号登录成功', '-'*10))
except:
    print("%s%s%s"  % ('-'*10, '登录界面出现问题', '-'*10))
        

