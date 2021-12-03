# -*- encoding=utf8 -*-
__author__ = "SMZ"

from airtest.core.api import *

auto_setup(__file__)

'''搜索结果页操作'''
try:
    # 获取当前设备的分辨率
    width, height = device().get_current_resolution()
    print('width:%s; height:%s' % (str(width), str(height)))
    
    '''最佳显示位校验'''
    # 歌手最佳显示位校验
    try:
        # 点击&键入搜索词
        touch((0.1*width, 0.05*height))
        text("林俊杰")
        sleep(3)
    
        assert_exists(Template(r"tpl1634886441990.png", record_pos=(-0.394, -0.619), resolution=(1080, 1920)), "校验你可能感兴趣")
        assert_exists(Template(r"tpl1634886802628.png", record_pos=(-0.231, -0.546), resolution=(1080, 1920)), "校验歌手")
        sleep()
        touch(exists(Template(r"tpl1634796109904.png", threshold=0.8, record_pos=(0.447, -0.794), resolution=(1080, 1920))))
        sleep()
    except:
        print("%s%s%s"  % ('-'*15, '校验歌手最佳显示位失败', '-'*15))

    # 专辑最佳显示位校验
    try:
        # 点击&键入搜索词
        touch((0.1*width, 0.05*height))
        text("泡沫之夏")
        sleep(3)
    
        assert_exists(Template(r"tpl1634886441990.png", record_pos=(-0.394, -0.619), resolution=(1080, 1920)), "校验你可能感兴趣")
        assert_exists(Template(r"tpl1634888009053.png", record_pos=(-0.188, -0.532), resolution=(1080, 1920)), "校验专辑")
        sleep()
        touch(exists(Template(r"tpl1634796109904.png", threshold=0.8, record_pos=(0.447, -0.794), resolution=(1080, 1920))))
        sleep()
    except:
        print("%s%s%s"  % ('-'*15, '校验专辑最佳显示位失败', '-'*15))
    
    # 视频最佳显示位校验
    try:
        # 点击&键入搜索词
        touch((0.1*width, 0.05*height))
        text("交换余生")
        sleep(3)
    
        assert_exists(Template(r"tpl1634886441990.png", record_pos=(-0.394, -0.619), resolution=(1080, 1920)), "校验你可能感兴趣")
        assert_exists(Template(r"tpl1637315222560.png", record_pos=(-0.133, -0.32), resolution=(1080, 1920)), "校验视频")
        sleep()
        touch(exists(Template(r"tpl1634796109904.png", threshold=0.8, record_pos=(0.447, -0.794), resolution=(1080, 1920))))
        sleep()
    except:
        print("%s%s%s"  % ('-'*15, '校验视频最佳显示位失败', '-'*15))

    # 歌单最佳显示位校验
    try:
        # 点击&键入搜索词
        touch((0.1*width, 0.05*height))
        text("金海心")
        sleep(3)
    
        assert_exists(Template(r"tpl1634886441990.png", record_pos=(-0.394, -0.619), resolution=(1080, 1920)), "校验你可能感兴趣")
        assert_exists(Template(r"tpl1634888969291.png", record_pos=(-0.194, -0.177), resolution=(1080, 1920)), "校验歌单")
        sleep()
        
        touch(exists(Template(r"tpl1634796109904.png", threshold=0.8, record_pos=(0.447, -0.794), resolution=(1080, 1920))))
        sleep()
    except:
        print("%s%s%s"  % ('-'*15, '校验歌单最佳显示位失败', '-'*15))

    # 视频彩铃最佳显示位校验
    try:
        # 点击&键入搜索词
        touch((0.1*width, 0.05*height))
        text("想象之中")
        sleep(3)
    
        assert_exists(Template(r"tpl1634886441990.png", record_pos=(-0.394, -0.619), resolution=(1080, 1920)), "校验你可能感兴趣")
        assert_exists(Template(r"tpl1634889375755.png", record_pos=(-0.388, -0.177), resolution=(1080, 1920)), "校验视频彩铃")
        sleep()
        touch(exists(Template(r"tpl1634796109904.png", threshold=0.8, record_pos=(0.447, -0.794), resolution=(1080, 1920))))
        sleep()
    except:
        print("%s%s%s"  % ('-'*15, '校验视频彩铃最佳显示位失败', '-'*15))

    # 演唱会最佳显示位校验
    try:
        # 点击&键入搜索词
        touch((0.1*width, 0.05*height))
        text("百花奖")
        sleep(3)
    
        assert_exists(Template(r"tpl1634886441990.png", record_pos=(-0.394, -0.619), resolution=(1080, 1920)), "校验你可能感兴趣")
        assert_exists(Template(r"tpl1634890148126.png", record_pos=(-0.185, -0.553), resolution=(1080, 1920)), "校验演唱会")
        sleep()
        
        touch(exists(Template(r"tpl1634796109904.png", threshold=0.8, record_pos=(0.447, -0.794), resolution=(1080, 1920))))
        sleep()
    except:
        print("%s%s%s"  % ('-'*15, '校验演唱会最佳显示位失败', '-'*15))

    # 彩铃专区最佳显示位校验
    try:
        # 点击&键入搜索词
        touch((0.1*width, 0.05*height))
        text("视频彩铃")
        sleep(3)
    
        assert_exists(Template(r"tpl1634886441990.png", record_pos=(-0.394, -0.619), resolution=(1080, 1920)), "校验你可能感兴趣")
        assert_exists(Template(r"tpl1634890855329.png", record_pos=(-0.36, -0.511), resolution=(1080, 1920)), "校验彩铃专区")
        sleep()
        touch(exists(Template(r"tpl1634796109904.png", threshold=0.8, record_pos=(0.447, -0.794), resolution=(1080, 1920))))
        sleep()
    except:
        print("%s%s%s"  % ('-'*15, '校验彩铃专区最佳显示位失败', '-'*15))

    # 电台最佳显示位校验
    try:
        # 点击&键入搜索词
        touch((0.1*width, 0.05*height))
        text("晴天")
        sleep(3)
    
        assert_exists(Template(r"tpl1634886441990.png", record_pos=(-0.394, -0.619), resolution=(1080, 1920)), "校验你可能感兴趣")
        assert_exists(Template(r"tpl1634891177025.png", record_pos=(-0.191, -0.176), resolution=(1080, 1920)), "校验电台")
        sleep()
        
        touch(exists(Template(r"tpl1634796109904.png", threshold=0.8, record_pos=(0.447, -0.794), resolution=(1080, 1920))))
        sleep()
    except:
        print("%s%s%s"  % ('-'*15, '校验视频彩铃最佳显示位失败', '-'*15))

    # B区最佳显示位校验
    try:
        # 点击&键入搜索词
        touch((0.1*width, 0.05*height))
        text("迪克牛仔")
        sleep(3)
    
        assert_exists(Template(r"tpl1634886441990.png", record_pos=(-0.394, -0.619), resolution=(1080, 1920)), "校验你可能感兴趣")
        
        assert_exists(Template(r"tpl1634891615840.png", record_pos=(-0.441, -0.182), resolution=(1080, 1920)), "校验有专辑")
        sleep()
        swipe((0.7*width, 0.31*height), (0.35*width, 0.31*height))
        sleep()
        assert_not_exists(Template(r"tpl1634892596383.png", threshold=0.88, record_pos=(-0.373, -0.155), resolution=(1080, 1920)), "滑动后专辑被隐藏，故应校验不到")
        sleep(2)
        touch(exists(Template(r"tpl1634796109904.png", threshold=0.8, record_pos=(0.447, -0.794), resolution=(1080, 1920))))
        sleep()
    except:
        print("%s%s%s"  % ('-'*15, '校验B区滑动最佳显示位失败', '-'*15))
except:
    print("%s%s%s"  % ('-'*15, '最佳显示位操作失败', '-'*15))

'''单曲tab校验'''
try:
    '''单曲结果&滑动等'''
    try:
        # 获取当前界面的横纵分辨率
        width, height = device().get_current_resolution()
        print('width:%s; height:%s' % (str(width), str(height)))
        # 点击&键入搜索词
        touch((0.1*width, 0.05*height))
        text("七里香")
        sleep(3)
    
        assert_exists(Template(r"tpl1634894656872.png", record_pos=(-0.422, -0.053), resolution=(1080, 1920)), "校验歌曲名称")
        sleep()
        assert_exists(Template(r"tpl1634894716979.png", record_pos=(-0.275, -0.01), resolution=(1080, 1920)), "校验歌手")
        sleep()
        assert_exists(Template(r"tpl1634894787804.png", record_pos=(0.002, 0.733), resolution=(1080, 1920)), "校验进入歌手详情页")
        sleep()
        
        assert_exists(Template(r"tpl1634895106351.png", record_pos=(-0.411, 0.091), resolution=(1080, 1920)), "校验抽屉结果")
        sleep()
        touch(Template(r"tpl1634895222046.png", record_pos=(-0.408, 0.094), resolution=(1080, 1920)))
        sleep(2)
        assert_exists(Template(r"tpl1634895272884.png", record_pos=(-0.381, 0.23), resolution=(1080, 1920)), "校验关闭抽屉")
        sleep()
        assert_exists(Template(r"tpl1634895756154.png", record_pos=(-0.387, 0.04), resolution=(1080, 1920)), "校验榜单")
        
        # 向下滑动并截图留痕
        for _ in range(2):
            swipe((0.5*width, 0.75*height), (0.5*width, 0.35*height))
            sleep()
        snapshot(msg="歌曲详情页下滑留痕")

        touch(exists(Template(r"tpl1634796109904.png", threshold=0.8, record_pos=(0.447, -0.794), resolution=(1080, 1920))))
        sleep()    
    except:
        print("%s%s%s"  % ('-'*15, '校验单曲结果滑动等失败', '-'*15))
        
    
except:
    print("%s%s%s"  % ('-'*15, '校验单曲tab失败', '-'*15))


'''专辑tab校验'''
try:
    # 获取当前界面的横纵分辨率
    width, height = device().get_current_resolution()
    print('width:%s; height:%s' % (str(width), str(height)))
    # 点击&键入搜索词
    touch((0.1*width, 0.05*height))
    text("七里香")
    sleep(3)
    if exists(Template(r"tpl1634953850985.png", threshold=0.85, rgb=False, record_pos=(-0.411, -0.702), resolution=(1080, 1920))) is not False:
        swipe((0.75*width, 0.5*height), (0.05*width, 0.5*height))  # 滑入专辑tab页
        sleep(5)
    else:
        print("%s%s%s"  % ('-'*15, '未在单曲页', '-'*15))
    assert_exists(Template(r"tpl1634954071740.png", threshold=0.85, record_pos=(-0.231, -0.703), resolution=(1080, 1920)), "tab页校验")
    sleep()
    assert_exists(Template(r"tpl1634954579743.png", record_pos=(-0.191, -0.585), resolution=(1080, 1920)), "校验专辑名")
    sleep()
    assert_exists(Template(r"tpl1634954624559.png", record_pos=(-0.113, -0.426), resolution=(1080, 1920)), "校验包含歌曲专辑")
    sleep()
    for _ in range(2):
        swipe((0.5*width, 0.75*height), (0.5*width, 0.35*height))  # 向下滑动
        sleep()
    snapshot(msg="专辑tab下滑留痕")
    sleep()
    touch(exists(Template(r"tpl1634796109904.png", threshold=0.8, record_pos=(0.447, -0.794), resolution=(1080, 1920))))
    sleep()
except:
    print("%s%s%s"  % ('-'*15, '校验专辑tab失败', '-'*15))

'''视频tab校验'''
try:
    # 获取当前界面的横纵分辨率
    width, height = device().get_current_resolution()
    print('width:%s; height:%s' % (str(width), str(height)))
    # 点击&键入搜索词
    touch((0.1*width, 0.05*height))
    text("周杰伦")
    sleep(3)
    if exists(Template(r"tpl1634955767720.png", threshold=0.8, rgb=True, record_pos=(-0.232, -0.701), resolution=(1080, 1920))) is not False:
        swipe((0.75*width, 0.5*height), (0.05*width, 0.5*height))  # 滑入视频tab页
        sleep(5)
    else:
        print("%s%s%s"  % ('-'*15, '已在视频页', '-'*15))
    assert_exists(Template(r"tpl1634955896620.png", threshold=0.8, rgb=True, record_pos=(-0.057, -0.703), resolution=(1080, 1920)), "视频tab页校验")
    sleep()
    snapshot(msg="视频tab截图留痕")
    sleep()
    

    assert_exists(Template(r"tpl1634955977359.png", record_pos=(-0.4, -0.631), resolution=(1080, 1920)), "校验视频更多删选")
    sleep()
    try:
        touch(Template(r"tpl1634956260304.png", record_pos=(-0.396, -0.632), resolution=(1080, 1920)))
        sleep()
        touch(exists(Template(r"tpl1634956304212.png", record_pos=(-0.249, -0.564), resolution=(1080, 1920))))
        sleep(3)
        snapshot(msg="视频时间排序留痕")
        touch(exists(Template(r"tpl1634956367726.png", record_pos=(-0.098, -0.563), resolution=(1080, 1920))))
        sleep(3)
        snapshot(msg="视频热度排序留痕")
    except:
        print("%s%s%s"  % ('-'*15, '校验视频筛选失败', '-'*15))
    for _ in range(2):
        swipe((0.5*width, 0.75*height), (0.5*width, 0.35*height))  # 向下滑动
        sleep()
    snapshot(msg="视频tab下滑留痕")
    sleep()
    touch(exists(Template(r"tpl1634796109904.png", threshold=0.8, record_pos=(0.447, -0.794), resolution=(1080, 1920))))
    sleep()
except:
    print("%s%s%s"  % ('-'*15, '校验专辑tab失败', '-'*15))

'''歌单tab校验'''
try:
    # 获取当前界面的横纵分辨率
    width, height = device().get_current_resolution()
    print('width:%s; height:%s' % (str(width), str(height)))
    # 点击&键入搜索词
    touch((0.1*width, 0.05*height))
    text("如果当时")
    sleep(5)
    if  exists(Template(r"tpl1634957258835.png", threshold=0.8, rgb=True, record_pos=(-0.056, -0.704), resolution=(1080, 1920))) is not False:
        swipe((0.75*width, 0.5*height), (0.05*width, 0.5*height))  # 滑入歌单tab页
        sleep(5)
    else:
        print("%s%s%s"  % ('-'*15, '已在歌单页', '-'*15))
    assert_exists(Template(r"tpl1634957518249.png", threshold=0.8, rgb=True, record_pos=(-0.001, -0.705), resolution=(1080, 1920)), "歌单tab页校验")
    sleep()
    snapshot(msg="歌单tab截图留痕")
    sleep()

    assert_exists(Template(r"tpl1634955977359.png", record_pos=(-0.4, -0.631), resolution=(1080, 1920)), "校验视频更多删选")
    sleep()
    try:
        touch(Template(r"tpl1634956260304.png", record_pos=(-0.396, -0.632), resolution=(1080, 1920)))
        sleep()
        touch(exists(Template(r"tpl1634956304212.png", record_pos=(-0.249, -0.564), resolution=(1080, 1920))))
        sleep(3)
        snapshot(msg="歌单时间排序留痕")
        touch(exists(Template(r"tpl1634956367726.png", record_pos=(-0.098, -0.563), resolution=(1080, 1920))))
        sleep(3)
        snapshot(msg="歌单热度排序留痕")
    except:
        print("%s%s%s"  % ('-'*15, '校验歌单筛选失败', '-'*15))
    for _ in range(2):
        swipe((0.5*width, 0.75*height), (0.5*width, 0.35*height))  # 向下滑动
        sleep()
    snapshot(msg="歌单tab下滑留痕")
    sleep()
    touch(exists(Template(r"tpl1634796109904.png", threshold=0.8, record_pos=(0.447, -0.794), resolution=(1080, 1920))))
    sleep()
except:
    print("%s%s%s"  % ('-'*15, '校验歌单tab失败', '-'*15))

'''歌词tab校验'''
try:
    # 获取当前界面的横纵分辨率
    width, height = device().get_current_resolution()
    print('width:%s; height:%s' % (str(width), str(height)))
    # 点击&键入搜索词
    touch((0.1*width, 0.05*height))
    text("我们一起")
    sleep(5)
    if exists(Template(r"tpl1634957059405.png", threshold=0.8, rgb=False, record_pos=(-0.002, -0.704), resolution=(1080, 1920))) is not False:
        swipe((0.75*width, 0.5*height), (0.05*width, 0.5*height))  # 滑入歌词tab页
        sleep(5)

    else:
        print("%s%s%s"  % ('-'*15, '已在歌词页', '-'*15))
    wait(Template(r"tpl1634958974174.png", record_pos=(-0.404, -0.386), resolution=(1080, 1920)))

    assert_exists(Template(r"tpl1634958494815.png", threshold=0.8, rgb=True, record_pos=(0.001, -0.701), resolution=(1080, 1920)), "歌词tab页校验")
    sleep()
    snapshot(msg="歌词tab截图留痕")
    sleep()
    
    try:
        touch(exists(Template(r"tpl1634958601045.png", record_pos=(-0.407, -0.386), resolution=(1080, 1920))))
        sleep()
        snapshot(msg="歌词展开留痕")
    except:
        print("%s%s%s"  % ('-'*15, '歌词展开失败', '-'*15))
    for _ in range(2):
        swipe((0.5*width, 0.75*height), (0.5*width, 0.35*height))  # 向下滑动
        sleep()
    snapshot(msg="歌词tab下滑留痕")
    sleep()
    touch(exists(Template(r"tpl1634796109904.png", threshold=0.8, record_pos=(0.447, -0.794), resolution=(1080, 1920))))
    sleep()
except:
    print("%s%s%s"  % ('-'*15, '校验歌词tab失败', '-'*15))

'''歌手tab校验'''
try:
    # 获取当前界面的横纵分辨率
    width, height = device().get_current_resolution()
    print('width:%s; height:%s' % (str(width), str(height)))
    # 点击&键入搜索词
    touch((0.1*width, 0.05*height))
    text("许嵩")
    sleep(3)
    if exists(Template(r"tpl1634958449683.png", threshold=0.7, rgb=False, record_pos=(-0.001, -0.703), resolution=(1080, 1920))) is not False:
        swipe((0.75*width, 0.5*height), (0.05*width, 0.5*height))  # 滑入歌手tab页
        sleep(5)
    else:
        print("%s%s%s"  % ('-'*15, '已在歌手页', '-'*15))

    assert_exists(Template(r"tpl1634959244492.png", threshold=0.8, rgb=True, record_pos=(0.054, -0.704), resolution=(1080, 1920)), "歌手tab页校验")
    sleep()
    snapshot(msg="歌手tab截图留痕")
    sleep()
    for _ in range(2):
        swipe((0.5*width, 0.75*height), (0.5*width, 0.35*height))  # 向下滑动
        sleep()
    snapshot(msg="歌手tab下滑留痕")
    sleep()
    touch(exists(Template(r"tpl1634796109904.png", threshold=0.8, record_pos=(0.447, -0.794), resolution=(1080, 1920))))
    sleep()
except:
    print("%s%s%s"  % ('-'*15, '校验歌手tab失败', '-'*15))

'''演唱会tab校验'''
try:
    # 获取当前界面的横纵分辨率
    width, height = device().get_current_resolution()
    print('width:%s; height:%s' % (str(width), str(height)))
    # 点击&键入搜索词
    touch((0.1*width, 0.05*height))
    text("周杰伦")
    sleep(3)
    if exists(Template(r"tpl1634959196054.png", threshold=0.8, rgb=False, record_pos=(0.055, -0.705), resolution=(1080, 1920))) is not False:
        swipe((0.75*width, 0.5*height), (0.05*width, 0.5*height))  # 滑入演唱会tab页
        sleep(5)
    else:
        print("%s%s%s"  % ('-'*15, '已在演唱会页', '-'*15))

    assert_exists(Template(r"tpl1634959960182.png", threshold=0.8, rgb=True, record_pos=(0.231, -0.7), resolution=(1080, 1920)), "演唱会tab页校验")
    sleep()
    snapshot(msg="演唱会tab截图留痕")
    sleep()
    
    for _ in range(2):
        swipe((0.5*width, 0.75*height), (0.5*width, 0.35*height))  # 向下滑动
        sleep()
    snapshot(msg="演唱会tab下滑留痕")
    sleep()
    touch(exists(Template(r"tpl1634796109904.png", threshold=0.8, record_pos=(0.447, -0.794), resolution=(1080, 1920))))
    sleep()
except:
    print("%s%s%s"  % ('-'*15, '校验演唱会tab失败', '-'*15))

'''票务tab校验'''
try:
    # 获取当前界面的横纵分辨率
    width, height = device().get_current_resolution()
    print('width:%s; height:%s' % (str(width), str(height)))
    # 点击&键入搜索词
    touch((0.1*width, 0.05*height))
    text("周杰伦")
    sleep(3)
    if exists(Template(r"tpl1634959905377.png", threshold=0.85, rgb=False, record_pos=(0.232, -0.702), resolution=(1080, 1920))) is not False:
        swipe((0.75*width, 0.5*height), (0.05*width, 0.5*height))  # 滑入票务tab页
        sleep(5)
    else:
        print("%s%s%s"  % ('-'*15, '已在票务页', '-'*15))

    assert_exists(Template(r"tpl1634960722347.png", threshold=0.85, record_pos=(0.41, -0.702), resolution=(1080, 1920)), "演唱会tab页校验")
    sleep()
    snapshot(msg="票务tab截图留痕")
    sleep()
    for _ in range(2):
        swipe((0.5*width, 0.75*height), (0.5*width, 0.35*height))  # 向下滑动
        sleep()
    snapshot(msg="票务tab下滑留痕")
    sleep()
    touch(exists(Template(r"tpl1634796109904.png", threshold=0.8, record_pos=(0.447, -0.794), resolution=(1080, 1920))))
    sleep()
except:
    print("%s%s%s"  % ('-'*15, '校验票务tab失败', '-'*15))

'''无结果推荐校验'''
try:
    # 获取当前界面的横纵分辨率
    width, height = device().get_current_resolution()
    print('width:%s; height:%s' % (str(width), str(height)))
    tab_list= ['单曲','专辑','视频','歌单','歌词','歌手','演唱会','票务']
    # 点击&键入搜索词
    touch((0.1*width, 0.05*height))
    text("。。。。。")
    sleep(3)
    if exists(Template(r"tpl1634961888576.png", threshold=0.85, rgb=True, record_pos=(-0.411, -0.706), resolution=(1080, 1920))) is not False:
        try:
            assert_exists(Template(r"tpl1634965207219.png", record_pos=(-0.179, -0.628), resolution=(1080, 1920)), "请填写测试点")

        except:
            print('无结果单曲没匹配')
        for index,name in enumerate(tab_list):
            print(index, name)
            snapshot(msg="截图留痕")
            sleep()
            swipe((0.75*width, 0.5*height), (0.05*width, 0.5*height))  # 右滑
            sleep(10)
            if exists(Template(r"tpl1634960658645.png", threshold=0.85, rgb=True, record_pos=(0.413, -0.701), resolution=(1080, 1920))) is not False:
                snapshot(msg="票务截图留痕")
                sleep()
                break
    elif exists(Template(r"tpl1634960658645.png", threshold=0.8, rgb=False, record_pos=(0.413, -0.701), resolution=(1080, 1920))) is not False:
        for index,name in enumerate(tab_list[::-1]):
            print(index, name)
            snapshot(msg="截图留痕")
            sleep()
            swipe((0.2*width, 0.5*height), (0.95*width, 0.5*height))  # 左滑
            sleep(10)
            if exists(Template(r"tpl1634961888576.png", threshold=0.85, rgb=True, record_pos=(-0.411, -0.706), resolution=(1080, 1920))) is not False:
                try:
                    assert_exists(Template(r"tpl1634965207219.png", record_pos=(-0.179, -0.628), resolution=(1080, 1920)), "无结果单曲页校验")

                except:
                    print('无结果单曲没匹配')
                snapshot(msg="单曲页截图留痕")
                sleep()
                break
    else:
        print("%s%s%s"  % ('-'*15, 'GG', '-'*15))
    touch(exists(Template(r"tpl1634796109904.png", threshold=0.8, record_pos=(0.447, -0.794), resolution=(1080, 1920))))
    sleep()
except:
    print("%s%s%s"  % ('-'*15, '校验无结果 推荐失败', '-'*15))



