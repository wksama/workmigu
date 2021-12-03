# -*- encoding=utf8 -*-
__author__ = "SMZ"

from airtest.core.api import *

auto_setup(__file__)

'''搜索结果页操作'''
try:
    if exists(Template(r"tpl1634795150417.png", threshold=0.85, rgb=True, record_pos=(-0.13, 0.839), resolution=(1080, 1920))) is not False:
        touch(Template(r"tpl1634795174574.png", threshold=0.85, rgb=True, record_pos=(-0.128, 0.833), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1634795207312.png", threshold=0.8, rgb=False, record_pos=(-0.131, 0.833), resolution=(1080, 1920))) is not False:
        touch(Template(r"tpl1634795298087.png", record_pos=(-0.126, 0.833), resolution=(1080, 1920)))
    else:
        print("%s%s%s"  % ('-'*15, '未找到音乐tab', '-'*15))
        
    sleep()
    # 获取当前设备的分辨率
    width, height = device().get_current_resolution()
    print('width:%s; height:%s' % (str(width), str(height)))
    
    # 点击搜索框
    touch((0.525*width, 0.06*height))
    sleep(10)
    
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
        touch(Template(r"tpl1634886937329.png", record_pos=(-0.231, -0.549), resolution=(1080, 1920)))
        sleep(3)
        assert_exists(Template(r"tpl1634886983013.png", record_pos=(-0.342, -0.158), resolution=(1080, 1920)), "校验进入歌手详情页")
        sleep(2)
        keyevent("4")  # 返回搜索结果页
        sleep(3)
        touch(exists(Template(r"tpl1634796109904.png", threshold=0.8, record_pos=(0.447, -0.794), resolution=(1080, 1920))))
        sleep()
    except:
        print("%s%s%s"  % ('-'*15, '校验歌手最佳显示位失败', '-'*15))
    finally:
        # 循环退出，直至返回至搜索框
        for _ in range(5):
            if exists(Template(r"tpl1638499859633.png", record_pos=(-0.415, -0.525), resolution=(1080, 1920))) is not False:
                break
            else:
                if exists(Template(r"tpl1638500210883.png", threshold=0.8, record_pos=(0.446, -0.796), resolution=(1080, 1920))) is not False:
                    touch(Template(r"tpl1638499578147.png", record_pos=(0.448, -0.795), resolution=(1080, 1920)))
                else:
                    keyevent("4")


    # 专辑最佳显示位校验
    try:
        # 点击&键入搜索词
        touch((0.1*width, 0.05*height))
        text("泡沫之夏")
        sleep(3)
    
        assert_exists(Template(r"tpl1634886441990.png", record_pos=(-0.394, -0.619), resolution=(1080, 1920)), "校验你可能感兴趣")
        assert_exists(Template(r"tpl1634888009053.png", record_pos=(-0.188, -0.532), resolution=(1080, 1920)), "校验专辑")
        sleep()
        touch(Template(r"tpl1634888009053.png", record_pos=(-0.188, -0.532), resolution=(1080, 1920)))

        sleep(3)
        assert_exists(Template(r"tpl1634888112463.png", record_pos=(-0.177, -0.376), resolution=(1080, 1920)), "校验进入专辑详情页")
        sleep(2)
        keyevent("4")  # 返回搜索结果页
        sleep(3)
        touch(exists(Template(r"tpl1634796109904.png", threshold=0.8, record_pos=(0.447, -0.794), resolution=(1080, 1920))))
        sleep()
    except:
        print("%s%s%s"  % ('-'*15, '校验专辑最佳显示位失败', '-'*15))
    finally:
        # 循环退出，直至返回至搜索框
        for _ in range(5):
            if exists(Template(r"tpl1638499859633.png", record_pos=(-0.415, -0.525), resolution=(1080, 1920))) is not False:
                break
            else:
                if exists(Template(r"tpl1638500210883.png", threshold=0.8, record_pos=(0.446, -0.796), resolution=(1080, 1920))) is not False:
                    touch(Template(r"tpl1638499578147.png", record_pos=(0.448, -0.795), resolution=(1080, 1920)))
                else:
                    keyevent("4")
    
    # 视频最佳显示位校验
    try:
        # 点击&键入搜索词
        touch((0.1*width, 0.05*height))
        text("彼得潘")
        sleep(3)
    
        assert_exists(Template(r"tpl1634886441990.png", record_pos=(-0.394, -0.619), resolution=(1080, 1920)), "校验你可能感兴趣")
        assert_exists(Template(r"tpl1634888412905.png", record_pos=(-0.112, -0.531), resolution=(1080, 1920)), "校验视频")
        sleep()
        touch(Template(r"tpl1634888412905.png", record_pos=(-0.112, -0.531), resolution=(1080, 1920)))

        sleep(5)
        assert_exists(Template(r"tpl1634888642141.png", record_pos=(-0.403, -0.097), resolution=(1080, 1920)), "校验进入视频详情页")
        sleep(2)
        keyevent("4")  # 返回搜索结果页
        sleep(3)
        touch(exists(Template(r"tpl1634796109904.png", threshold=0.8, record_pos=(0.447, -0.794), resolution=(1080, 1920))))
        sleep()
    except:
        print("%s%s%s"  % ('-'*15, '校验视频最佳显示位失败', '-'*15))
    finally:
        # 循环退出，直至返回至搜索框
        for _ in range(5):
            if exists(Template(r"tpl1638499859633.png", record_pos=(-0.415, -0.525), resolution=(1080, 1920))) is not False:
                break
            else:
                if exists(Template(r"tpl1638500210883.png", threshold=0.8, record_pos=(0.446, -0.796), resolution=(1080, 1920))) is not False:
                    touch(Template(r"tpl1638499578147.png", record_pos=(0.448, -0.795), resolution=(1080, 1920)))
                else:
                    keyevent("4")

    # 歌单最佳显示位校验
    try:
        # 点击&键入搜索词
        touch((0.1*width, 0.05*height))
        text("林俊杰")
        sleep(3)
    
        assert_exists(Template(r"tpl1634886441990.png", record_pos=(-0.394, -0.619), resolution=(1080, 1920)), "校验你可能感兴趣")
        assert_exists(Template(r"tpl1634888969291.png", record_pos=(-0.194, -0.177), resolution=(1080, 1920)), "校验歌单")
        sleep()
        touch(Template(r"tpl1634888993406.png", record_pos=(-0.194, -0.177), resolution=(1080, 1920)))

        sleep(5)
        assert_exists(Template(r"tpl1634889055143.png", record_pos=(-0.379, -0.784), resolution=(1080, 1920)), "校验进入歌单详情页")
        sleep(2)
        keyevent("4")  # 返回搜索结果页
        sleep(3)
        touch(exists(Template(r"tpl1634796109904.png", threshold=0.8, record_pos=(0.447, -0.794), resolution=(1080, 1920))))
        sleep()
    except:
        print("%s%s%s"  % ('-'*15, '校验歌单最佳显示位失败', '-'*15))
    finally:
        # 循环退出，直至返回至搜索框
        for _ in range(5):
            if exists(Template(r"tpl1638499859633.png", record_pos=(-0.415, -0.525), resolution=(1080, 1920))) is not False:
                break
            else:
                if exists(Template(r"tpl1638500210883.png", threshold=0.8, record_pos=(0.446, -0.796), resolution=(1080, 1920))) is not False:
                    touch(Template(r"tpl1638499578147.png", record_pos=(0.448, -0.795), resolution=(1080, 1920)))
                else:
                    keyevent("4")

    # 视频彩铃最佳显示位校验
    try:
        # 点击&键入搜索词
        touch((0.1*width, 0.05*height))
        text("想象之中")
        sleep(3)
    
        assert_exists(Template(r"tpl1634886441990.png", record_pos=(-0.394, -0.619), resolution=(1080, 1920)), "校验你可能感兴趣")
        assert_exists(Template(r"tpl1634889375755.png", record_pos=(-0.388, -0.177), resolution=(1080, 1920)), "校验视频彩铃")
        sleep()
        touch(Template(r"tpl1634889465664.png", record_pos=(-0.388, -0.177), resolution=(1080, 1920)))

        sleep(5)
        wait(Template(r"tpl1634889664377.png", record_pos=(0.427, 0.728), resolution=(1080, 1920)), timeout=35)  #首次有可能会要现在插件，故作等待

        assert_exists(Template(r"tpl1634889607400.png", record_pos=(0.429, 0.727), resolution=(1080, 1920)), "校验进入视频彩铃详情页")
        sleep(2)
        keyevent("4")  # 返回搜索结果页
        sleep(3)
        touch(exists(Template(r"tpl1634796109904.png", threshold=0.8, record_pos=(0.447, -0.794), resolution=(1080, 1920))))
        sleep()
    except:
        print("%s%s%s"  % ('-'*15, '校验视频彩铃最佳显示位失败', '-'*15))
    finally:
        # 循环退出，直至返回至搜索框
        for _ in range(5):
            if exists(Template(r"tpl1638499859633.png", record_pos=(-0.415, -0.525), resolution=(1080, 1920))) is not False:
                break
            else:
                if exists(Template(r"tpl1638500210883.png", threshold=0.8, record_pos=(0.446, -0.796), resolution=(1080, 1920))) is not False:
                    touch(Template(r"tpl1638499578147.png", record_pos=(0.448, -0.795), resolution=(1080, 1920)))
                else:
                    keyevent("4")

    # 演唱会最佳显示位校验
    try:
        # 点击&键入搜索词
        touch((0.1*width, 0.05*height))
        text("百花奖")
        sleep(3)
    
        assert_exists(Template(r"tpl1634886441990.png", record_pos=(-0.394, -0.619), resolution=(1080, 1920)), "校验你可能感兴趣")
        assert_exists(Template(r"tpl1634890148126.png", record_pos=(-0.185, -0.553), resolution=(1080, 1920)), "校验演唱会")
        sleep()
        touch(Template(r"tpl1634890193865.png", record_pos=(-0.187, -0.555), resolution=(1080, 1920)))

        sleep(5)
        wait(Template(r"tpl1634890242506.png", record_pos=(-0.249, -0.232), resolution=(1080, 1920)), timeout=35)  #首次有可能会要现在插件，故作等待

        assert_exists(Template(r"tpl1634890265789.png", record_pos=(-0.249, -0.228), resolution=(1080, 1920)), "校验进入演唱会详情页")
        sleep(2)
        keyevent("4")  # 返回搜索结果页
        sleep(3)
        touch(exists(Template(r"tpl1634796109904.png", threshold=0.8, record_pos=(0.447, -0.794), resolution=(1080, 1920))))
        sleep()
    except:
        print("%s%s%s"  % ('-'*15, '校验演唱会最佳显示位失败', '-'*15))
    finally:
        # 循环退出，直至返回至搜索框
        for _ in range(5):
            if exists(Template(r"tpl1638499859633.png", record_pos=(-0.415, -0.525), resolution=(1080, 1920))) is not False:
                break
            else:
                if exists(Template(r"tpl1638500210883.png", threshold=0.8, record_pos=(0.446, -0.796), resolution=(1080, 1920))) is not False:
                    touch(Template(r"tpl1638499578147.png", record_pos=(0.448, -0.795), resolution=(1080, 1920)))
                else:
                    keyevent("4")

    # 彩铃专区最佳显示位校验
    try:
        # 点击&键入搜索词
        touch((0.1*width, 0.05*height))
        text("视频彩铃")
        sleep(3)
    
        assert_exists(Template(r"tpl1634886441990.png", record_pos=(-0.394, -0.619), resolution=(1080, 1920)), "校验你可能感兴趣")
        assert_exists(Template(r"tpl1634890855329.png", record_pos=(-0.36, -0.511), resolution=(1080, 1920)), "校验彩铃专区")
        sleep()
        touch(Template(r"tpl1634890908999.png", record_pos=(-0.361, -0.508), resolution=(1080, 1920)))

        sleep(5)
        # wait(Template(r"tpl1634890956305.png", record_pos=(-0.359, 0.839), resolution=(1080, 1920)), timeout=35)  #首次有可能会要现在插件，故作等待

        assert_exists(Template(r"tpl1634890992198.png", record_pos=(-0.359, 0.838), resolution=(1080, 1920)), "校验进入彩铃专区详情页")
        sleep(2)
        keyevent("4")  # 返回搜索结果页
        sleep(3)
        touch(exists(Template(r"tpl1634796109904.png", threshold=0.8, record_pos=(0.447, -0.794), resolution=(1080, 1920))))
        sleep()
    except:
        print("%s%s%s"  % ('-'*15, '校验彩铃专区最佳显示位失败', '-'*15))
    finally:
        # 循环退出，直至返回至搜索框
        for _ in range(5):
            if exists(Template(r"tpl1638499859633.png", record_pos=(-0.415, -0.525), resolution=(1080, 1920))) is not False:
                break
            else:
                if exists(Template(r"tpl1638500210883.png", threshold=0.8, record_pos=(0.446, -0.796), resolution=(1080, 1920))) is not False:
                    touch(Template(r"tpl1638499578147.png", record_pos=(0.448, -0.795), resolution=(1080, 1920)))
                else:
                    keyevent("4")

    # 电台最佳显示位校验
    try:
        # 点击&键入搜索词
        touch((0.1*width, 0.05*height))
        text("晴天")
        sleep(3)
    
        assert_exists(Template(r"tpl1634886441990.png", record_pos=(-0.394, -0.619), resolution=(1080, 1920)), "校验你可能感兴趣")
        assert_exists(Template(r"tpl1634891177025.png", record_pos=(-0.191, -0.176), resolution=(1080, 1920)), "校验电台")
        sleep()
        touch(Template(r"tpl1634891222946.png", record_pos=(-0.194, -0.176), resolution=(1080, 1920)))

        sleep(5)
        # wait(Template(r"tpl1634890956305.png", record_pos=(-0.359, 0.839), resolution=(1080, 1920)), timeout=35)  #首次有可能会要现在插件，故作等待

        assert_exists(Template(r"tpl1634891255195.png", record_pos=(-0.005, 0.775), resolution=(1080, 1920)), "校验进入电台详情页")
        sleep(2)
        touch(exists(Template(r"tpl1634891290673.png", record_pos=(-0.004, 0.774), resolution=(1080, 1920))))
        sleep()
        keyevent("4")  # 返回搜索结果页
        sleep(3)
        touch(exists(Template(r"tpl1634796109904.png", threshold=0.8, record_pos=(0.447, -0.794), resolution=(1080, 1920))))
        sleep()
    except:
        print("%s%s%s"  % ('-'*15, '校验视频彩铃最佳显示位失败', '-'*15))
    finally:
        # 循环退出，直至返回至搜索框
        for _ in range(5):
            if exists(Template(r"tpl1638499859633.png", record_pos=(-0.415, -0.525), resolution=(1080, 1920))) is not False:
                break
            else:
                if exists(Template(r"tpl1638500210883.png", threshold=0.8, record_pos=(0.446, -0.796), resolution=(1080, 1920))) is not False:
                    touch(Template(r"tpl1638499578147.png", record_pos=(0.448, -0.795), resolution=(1080, 1920)))
                else:
                    keyevent("4")

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
    finally:
        # 循环退出，直至返回至搜索框
        for _ in range(5):
            if exists(Template(r"tpl1638499859633.png", record_pos=(-0.415, -0.525), resolution=(1080, 1920))) is not False:
                break
            else:
                if exists(Template(r"tpl1638500210883.png", threshold=0.8, record_pos=(0.446, -0.796), resolution=(1080, 1920))) is not False:
                    touch(Template(r"tpl1638499578147.png", record_pos=(0.448, -0.795), resolution=(1080, 1920)))
                else:
                    keyevent("4")
except:
    print("%s%s%s"  % ('-'*15, '最佳显示位操作失败', '-'*15))
finally:
    # 循环退出，直至返回至搜索框
    for _ in range(5):
        if exists(Template(r"tpl1638499859633.png", record_pos=(-0.415, -0.525), resolution=(1080, 1920))) is not False:
            break
        else:
            if exists(Template(r"tpl1638500210883.png", threshold=0.8, record_pos=(0.446, -0.796), resolution=(1080, 1920))) is not False:
                touch(Template(r"tpl1638499578147.png", record_pos=(0.448, -0.795), resolution=(1080, 1920)))
            else:
                keyevent("4")


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
        assert_exists(Template(r"tpl1638510416925.png", record_pos=(-0.372, -0.169), resolution=(1080, 1920)), "校验榜单")
        if exists(Template(r"tpl1638510436011.png", record_pos=(-0.374, -0.168), resolution=(1080, 1920))) is not False:
            touch(Template(r"tpl1638510457151.png", record_pos=(-0.379, -0.171), resolution=(1080, 1920)))
            sleep(3)
            assert_exists(Template(r"tpl1638510480238.png", record_pos=(-0.216, -0.369), resolution=(1080, 1920)), "校验榜单")
            sleep()
            keyevent("4")
            sleep(2)
        else:
            print("%s%s%s"  % ('-'*15, '未找到尖叫热歌榜', '-'*15))
        # 向下滑动并截图留痕
        for _ in range(2):
            swipe((0.5*width, 0.75*height), (0.5*width, 0.35*height))
            sleep()
        snapshot(msg="歌曲详情页下滑留痕")

        touch(exists(Template(r"tpl1634796109904.png", threshold=0.8, record_pos=(0.447, -0.794), resolution=(1080, 1920))))
        sleep()    
    except:
        print("%s%s%s"  % ('-'*15, '校验单曲结果滑动等失败', '-'*15))
    finally:
        # 循环退出，直至返回至搜索框
        for _ in range(5):
            if exists(Template(r"tpl1638499859633.png", record_pos=(-0.415, -0.525), resolution=(1080, 1920))) is not False:
                break
            else:
                if exists(Template(r"tpl1638500210883.png", threshold=0.8, record_pos=(0.446, -0.796), resolution=(1080, 1920))) is not False:
                    touch(Template(r"tpl1638499578147.png", record_pos=(0.448, -0.795), resolution=(1080, 1920)))
                else:
                    keyevent("4")
        
    '''超多评论等校验'''
    try:
        # 获取当前设备的分辨率
        width, height = device().get_current_resolution()
        print('width:%s; height:%s' % (str(width), str(height)))
        # 点击&键入搜索词
        touch((0.1*width, 0.05*height))
        text("圣诞节")
        sleep(3)
    
        assert_exists(Template(r"tpl1634915800265.png", record_pos=(-0.317, 0.041), resolution=(1080, 1920)), "校验超多评论")
        assert_exists(Template(r"tpl1634915912055.png", record_pos=(0.448, 0.054), resolution=(1080, 1920)), "校验歌曲更多按钮")
        sleep()
        if exists(Template(r"tpl1634915990995.png", record_pos=(0.448, 0.055), resolution=(1080, 1920))) is not False:
            touch(Template(r"tpl1634916071392.png", record_pos=(0.444, 0.053), resolution=(1080, 1920)))  # 点击更多按钮
            sleep()
            assert_exists(Template(r"tpl1634916118414.png", record_pos=(-0.357, 0.476), resolution=(1080, 1920)), "校验收藏按钮")
            sleep()
            assert_exists(Template(r"tpl1634916177262.png", record_pos=(0.119, 0.294), resolution=(1080, 1920)), "校验下载按钮")
            sleep()
            keyevent("4")  # 退出更多
            sleep()
        else:
            print("%s%s%s"  % ('-'*15, '校验歌曲更多失败', '-'*15))
        
        try:
            touch(exists(Template(r"tpl1634917316582.png", record_pos=(-0.355, -0.077), resolution=(1080, 1920))))  # 校验播放全部
            sleep()
            touch(exists(Template(r"tpl1634918863127.png", threshold=0.8, record_pos=(0.441, 0.842), resolution=(1080, 1920))))
            sleep(2)
            snapshot(msg="播放全部页面内容截图留痕")
            sleep()
            keyevent("4")
            sleep()
            touch(exists(Template(r"tpl1634918987295.png", threshold=0.8, record_pos=(0.347, 0.843), resolution=(1080, 1920))))
            sleep()
        except:
            print("%s%s%s"  % ('-'*15, '校验播放全部失败', '-'*15))
        
        # 校验歌曲mv播放
        touch(exists(Template(r"tpl1634917953160.png", record_pos=(0.378, 0.326), resolution=(1080, 1920))))
        wait(Template(r"tpl1634918009159.png", record_pos=(-0.403, -0.093), resolution=(1080, 1920)))
        sleep()
        assert_exists(Template(r"tpl1634918056097.png", record_pos=(-0.405, -0.098), resolution=(1080, 1920)), "校验mv详情页")
        keyevent("4")
        sleep()
        touch(exists(Template(r"tpl1634796109904.png", threshold=0.8, record_pos=(0.447, -0.794), resolution=(1080, 1920))))
        sleep()
    except:
        print("%s%s%s"  % ('-'*15, '校验超多评论失败', '-'*15))
    finally:
        # 循环退出，直至返回至搜索框
        for _ in range(5):
            if exists(Template(r"tpl1638499859633.png", record_pos=(-0.415, -0.525), resolution=(1080, 1920))) is not False:
                break
            else:
                if exists(Template(r"tpl1638500210883.png", threshold=0.8, record_pos=(0.446, -0.796), resolution=(1080, 1920))) is not False:
                    touch(Template(r"tpl1638499578147.png", record_pos=(0.448, -0.795), resolution=(1080, 1920)))
                else:
                    keyevent("4")
    
    '''数字专辑校验'''
    try:
        # 获取当前设备的分辨率
        width, height = device().get_current_resolution()
        print('width:%s; height:%s' % (str(width), str(height)))
        # 点击&键入搜索词
        touch((0.1*width, 0.05*height))
        text("Mojito")
        sleep(3)
        touch(exists(Template(r"tpl1634920562962.png", record_pos=(-0.371, -0.053), resolution=(1080, 1920))))
        sleep(2)
        assert_exists(Template(r"tpl1634920603534.png", record_pos=(-0.444, 0.494), resolution=(1080, 1920)), "校验付费歌曲")
        sleep()
        keyevent("4")
        sleep()
        touch(exists(Template(r"tpl1634796109904.png", threshold=0.8, record_pos=(0.447, -0.794), resolution=(1080, 1920))))
        sleep()
    except:
        print("%s%s%s"  % ('-'*15, '校验数字专辑失败', '-'*15))
    finally:
        # 循环退出，直至返回至搜索框
        for _ in range(5):
            if exists(Template(r"tpl1638499859633.png", record_pos=(-0.415, -0.525), resolution=(1080, 1920))) is not False:
                break
            else:
                if exists(Template(r"tpl1638500210883.png", threshold=0.8, record_pos=(0.446, -0.796), resolution=(1080, 1920))) is not False:
                    touch(Template(r"tpl1638499578147.png", record_pos=(0.448, -0.795), resolution=(1080, 1920)))
                else:
                    keyevent("4")
except:
    print("%s%s%s"  % ('-'*15, '校验单曲tab失败', '-'*15))
finally:
    # 循环退出，直至返回至搜索框
    for _ in range(5):
        if exists(Template(r"tpl1638499859633.png", record_pos=(-0.415, -0.525), resolution=(1080, 1920))) is not False:
            break
        else:
            if exists(Template(r"tpl1638500210883.png", threshold=0.8, record_pos=(0.446, -0.796), resolution=(1080, 1920))) is not False:
                touch(Template(r"tpl1638499578147.png", record_pos=(0.448, -0.795), resolution=(1080, 1920)))
            else:
                keyevent("4")


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
    try:
        touch(Template(r"tpl1634954717297.png", record_pos=(-0.193, -0.583), resolution=(1080, 1920)))
        wait(Template(r"tpl1634954759310.png", record_pos=(-0.381, -0.786), resolution=(1080, 1920)))
        snapshot(msg="专辑详情页截图留痕")
        keyevent("4")
        sleep()
    except:
        print("%s%s%s"  % ('-'*15, '校验专辑详情失败', '-'*15))
    finally:
        # 循环退出，直至返回至搜索框
        for _ in range(5):
            if exists(Template(r"tpl1638499859633.png", record_pos=(-0.415, -0.525), resolution=(1080, 1920))) is not False:
                break
            else:
                if exists(Template(r"tpl1638500210883.png", threshold=0.8, record_pos=(0.446, -0.796), resolution=(1080, 1920))) is not False:
                    touch(Template(r"tpl1638499578147.png", record_pos=(0.448, -0.795), resolution=(1080, 1920)))
                else:
                    keyevent("4")
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
finally:
    # 循环退出，直至返回至搜索框
    for _ in range(5):
        if exists(Template(r"tpl1638499859633.png", record_pos=(-0.415, -0.525), resolution=(1080, 1920))) is not False:
            break
        else:
            if exists(Template(r"tpl1638500210883.png", threshold=0.8, record_pos=(0.446, -0.796), resolution=(1080, 1920))) is not False:
                touch(Template(r"tpl1638499578147.png", record_pos=(0.448, -0.795), resolution=(1080, 1920)))
            else:
                keyevent("4")

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
    try:
        touch(exists(Template(r"tpl1634956072508.png", record_pos=(-0.044, -0.479), resolution=(1080, 1920)))) # 进入视频详情页
        wait(Template(r"tpl1634956120647.png", record_pos=(-0.406, -0.094), resolution=(1080, 1920)))
        sleep()
        assert_exists(Template(r"tpl1634956138792.png", record_pos=(-0.404, -0.094), resolution=(1080, 1920)), "校验视频详情")
        keyevent("4")
        sleep(3)
    except:
        print("%s%s%s"  % ('-'*15, '视频播放详情页失败', '-'*15))
    finally:
        # 循环退出，直至返回至搜索框
        for _ in range(5):
            if exists(Template(r"tpl1638499859633.png", record_pos=(-0.415, -0.525), resolution=(1080, 1920))) is not False:
                break
            else:
                if exists(Template(r"tpl1638500210883.png", threshold=0.8, record_pos=(0.446, -0.796), resolution=(1080, 1920))) is not False:
                    touch(Template(r"tpl1638499578147.png", record_pos=(0.448, -0.795), resolution=(1080, 1920)))
                else:
                    keyevent("4")

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
    finally:
        # 循环退出，直至返回至搜索框
        for _ in range(5):
            if exists(Template(r"tpl1638499859633.png", record_pos=(-0.415, -0.525), resolution=(1080, 1920))) is not False:
                break
            else:
                if exists(Template(r"tpl1638500210883.png", threshold=0.8, record_pos=(0.446, -0.796), resolution=(1080, 1920))) is not False:
                    touch(Template(r"tpl1638499578147.png", record_pos=(0.448, -0.795), resolution=(1080, 1920)))
                else:
                    keyevent("4")
    for _ in range(2):
        swipe((0.5*width, 0.75*height), (0.5*width, 0.35*height))  # 向下滑动
        sleep()
    snapshot(msg="视频tab下滑留痕")
    sleep()
    touch(exists(Template(r"tpl1634796109904.png", threshold=0.8, record_pos=(0.447, -0.794), resolution=(1080, 1920))))
    sleep()
except:
    print("%s%s%s"  % ('-'*15, '校验专辑tab失败', '-'*15))
finally:
    # 循环退出，直至返回至搜索框
    for _ in range(5):
        if exists(Template(r"tpl1638499859633.png", record_pos=(-0.415, -0.525), resolution=(1080, 1920))) is not False:
            break
        else:
            if exists(Template(r"tpl1638500210883.png", threshold=0.8, record_pos=(0.446, -0.796), resolution=(1080, 1920))) is not False:
                touch(Template(r"tpl1638499578147.png", record_pos=(0.448, -0.795), resolution=(1080, 1920)))
            else:
                keyevent("4")

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
    try:
        touch(exists(Template(r"tpl1634957633002.png", record_pos=(-0.162, -0.461), resolution=(1080, 1920)))) # 进入歌单详情页
        wait(Template(r"tpl1634957667728.png", record_pos=(-0.387, -0.784), resolution=(1080, 1920)))
        sleep()
        assert_exists(Template(r"tpl1634957694603.png", record_pos=(-0.381, -0.787), resolution=(1080, 1920)), "校验歌单详情")
        keyevent("4")
        sleep(3)
    except:
        print("%s%s%s"  % ('-'*15, '歌单详情页失败', '-'*15))
    finally:
        # 循环退出，直至返回至搜索框
        for _ in range(5):
            if exists(Template(r"tpl1638499859633.png", record_pos=(-0.415, -0.525), resolution=(1080, 1920))) is not False:
                break
            else:
                if exists(Template(r"tpl1638500210883.png", threshold=0.8, record_pos=(0.446, -0.796), resolution=(1080, 1920))) is not False:
                    touch(Template(r"tpl1638499578147.png", record_pos=(0.448, -0.795), resolution=(1080, 1920)))
                else:
                    keyevent("4")

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
    finally:
        # 循环退出，直至返回至搜索框
        for _ in range(5):
            if exists(Template(r"tpl1638499859633.png", record_pos=(-0.415, -0.525), resolution=(1080, 1920))) is not False:
                break
            else:
                if exists(Template(r"tpl1638500210883.png", threshold=0.8, record_pos=(0.446, -0.796), resolution=(1080, 1920))) is not False:
                    touch(Template(r"tpl1638499578147.png", record_pos=(0.448, -0.795), resolution=(1080, 1920)))
                else:
                    keyevent("4")
    for _ in range(2):
        swipe((0.5*width, 0.75*height), (0.5*width, 0.35*height))  # 向下滑动
        sleep()
    snapshot(msg="歌单tab下滑留痕")
    sleep()
    touch(exists(Template(r"tpl1634796109904.png", threshold=0.8, record_pos=(0.447, -0.794), resolution=(1080, 1920))))
    sleep()
except:
    print("%s%s%s"  % ('-'*15, '校验歌单tab失败', '-'*15))
finally:
    # 循环退出，直至返回至搜索框
    for _ in range(5):
        if exists(Template(r"tpl1638499859633.png", record_pos=(-0.415, -0.525), resolution=(1080, 1920))) is not False:
            break
        else:
            if exists(Template(r"tpl1638500210883.png", threshold=0.8, record_pos=(0.446, -0.796), resolution=(1080, 1920))) is not False:
                touch(Template(r"tpl1638499578147.png", record_pos=(0.448, -0.795), resolution=(1080, 1920)))
            else:
                keyevent("4")

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
        touch(exists(Template(r"tpl1634958794283.png", record_pos=(-0.388, -0.608), resolution=(1080, 1920))))
        sleep(2)
        touch(exists(Template(r"tpl1634958847690.png", record_pos=(0.345, 0.84), resolution=(1080, 1920))))
        sleep()
    except:
        print("%s%s%s"  % ('-'*15, '歌词播放失败', '-'*15))
    finally:
        # 循环退出，直至返回至搜索框
        for _ in range(5):
            if exists(Template(r"tpl1638499859633.png", record_pos=(-0.415, -0.525), resolution=(1080, 1920))) is not False:
                break
            else:
                if exists(Template(r"tpl1638500210883.png", threshold=0.8, record_pos=(0.446, -0.796), resolution=(1080, 1920))) is not False:
                    touch(Template(r"tpl1638499578147.png", record_pos=(0.448, -0.795), resolution=(1080, 1920)))
                else:
                    keyevent("4")
    try:
        touch(exists(Template(r"tpl1634958601045.png", record_pos=(-0.407, -0.386), resolution=(1080, 1920))))
        sleep()
        snapshot(msg="歌词展开留痕")
    except:
        print("%s%s%s"  % ('-'*15, '歌词展开失败', '-'*15))
    finally:
        # 循环退出，直至返回至搜索框
        for _ in range(5):
            if exists(Template(r"tpl1638499859633.png", record_pos=(-0.415, -0.525), resolution=(1080, 1920))) is not False:
                break
            else:
                if exists(Template(r"tpl1638500210883.png", threshold=0.8, record_pos=(0.446, -0.796), resolution=(1080, 1920))) is not False:
                    touch(Template(r"tpl1638499578147.png", record_pos=(0.448, -0.795), resolution=(1080, 1920)))
                else:
                    keyevent("4")
    for _ in range(2):
        swipe((0.5*width, 0.75*height), (0.5*width, 0.35*height))  # 向下滑动
        sleep()
    snapshot(msg="歌词tab下滑留痕")
    sleep()
    touch(exists(Template(r"tpl1634796109904.png", threshold=0.8, record_pos=(0.447, -0.794), resolution=(1080, 1920))))
    sleep()
except:
    print("%s%s%s"  % ('-'*15, '校验歌词tab失败', '-'*15))
finally:
    # 循环退出，直至返回至搜索框
    for _ in range(5):
        if exists(Template(r"tpl1638499859633.png", record_pos=(-0.415, -0.525), resolution=(1080, 1920))) is not False:
            break
        else:
            if exists(Template(r"tpl1638500210883.png", threshold=0.8, record_pos=(0.446, -0.796), resolution=(1080, 1920))) is not False:
                touch(Template(r"tpl1638499578147.png", record_pos=(0.448, -0.795), resolution=(1080, 1920)))
            else:
                keyevent("4")

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
    try:
        touch(exists(Template(r"tpl1634959310967.png", record_pos=(-0.306, -0.608), resolution=(1080, 1920))))
        sleep()
        wait(Template(r"tpl1634959365912.png", record_pos=(-0.374, -0.155), resolution=(1080, 1920)))
        sleep()
        snapshot(msg="歌手详情页留痕")
        keyevent("4")
        sleep(3)
    except:
        print("%s%s%s"  % ('-'*15, '歌手详情失败', '-'*15))
    finally:
        # 循环退出，直至返回至搜索框
        for _ in range(5):
            if exists(Template(r"tpl1638499859633.png", record_pos=(-0.415, -0.525), resolution=(1080, 1920))) is not False:
                break
            else:
                if exists(Template(r"tpl1638500210883.png", threshold=0.8, record_pos=(0.446, -0.796), resolution=(1080, 1920))) is not False:
                    touch(Template(r"tpl1638499578147.png", record_pos=(0.448, -0.795), resolution=(1080, 1920)))
                else:
                    keyevent("4")
    for _ in range(2):
        swipe((0.5*width, 0.75*height), (0.5*width, 0.35*height))  # 向下滑动
        sleep()
    snapshot(msg="歌手tab下滑留痕")
    sleep()
    touch(exists(Template(r"tpl1634796109904.png", threshold=0.8, record_pos=(0.447, -0.794), resolution=(1080, 1920))))
    sleep()
except:
    print("%s%s%s"  % ('-'*15, '校验歌手tab失败', '-'*15))
finally:
    # 循环退出，直至返回至搜索框
    for _ in range(5):
        if exists(Template(r"tpl1638499859633.png", record_pos=(-0.415, -0.525), resolution=(1080, 1920))) is not False:
            break
        else:
            if exists(Template(r"tpl1638500210883.png", threshold=0.8, record_pos=(0.446, -0.796), resolution=(1080, 1920))) is not False:
                touch(Template(r"tpl1638499578147.png", record_pos=(0.448, -0.795), resolution=(1080, 1920)))
            else:
                keyevent("4")

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
    try:
        touch(exists(Template(r"tpl1634960240851.png", record_pos=(-0.413, -0.613), resolution=(1080, 1920))))
        sleep()
        wait(Template(r"tpl1634960367666.png", record_pos=(-0.253, -0.231), resolution=(1080, 1920)))
        sleep(3)
        snapshot(msg="演唱会详情页留痕")
        keyevent("4")
        sleep(3)
    except:
        print("%s%s%s"  % ('-'*15, '演唱会详情失败', '-'*15))
    finally:
        # 循环退出，直至返回至搜索框
        for _ in range(5):
            if exists(Template(r"tpl1638499859633.png", record_pos=(-0.415, -0.525), resolution=(1080, 1920))) is not False:
                break
            else:
                if exists(Template(r"tpl1638500210883.png", threshold=0.8, record_pos=(0.446, -0.796), resolution=(1080, 1920))) is not False:
                    touch(Template(r"tpl1638499578147.png", record_pos=(0.448, -0.795), resolution=(1080, 1920)))
                else:
                    keyevent("4")
    for _ in range(2):
        swipe((0.5*width, 0.75*height), (0.5*width, 0.35*height))  # 向下滑动
        sleep()
    snapshot(msg="演唱会tab下滑留痕")
    sleep()
    touch(exists(Template(r"tpl1634796109904.png", threshold=0.8, record_pos=(0.447, -0.794), resolution=(1080, 1920))))
    sleep()
except:
    print("%s%s%s"  % ('-'*15, '校验演唱会tab失败', '-'*15))
finally:
    # 循环退出，直至返回至搜索框
    for _ in range(5):
        if exists(Template(r"tpl1638499859633.png", record_pos=(-0.415, -0.525), resolution=(1080, 1920))) is not False:
            break
        else:
            if exists(Template(r"tpl1638500210883.png", threshold=0.8, record_pos=(0.446, -0.796), resolution=(1080, 1920))) is not False:
                touch(Template(r"tpl1638499578147.png", record_pos=(0.448, -0.795), resolution=(1080, 1920)))
            else:
                keyevent("4")

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
    try:
        touch((0.15*width, 0.25*height))
        sleep()
        wait(Template(r"tpl1634960841853.png", record_pos=(-0.374, -0.794), resolution=(1080, 1920)))
        sleep(3)
        snapshot(msg="票务详情页留痕")
        keyevent("4")
        sleep(3)
    except:
        print("%s%s%s"  % ('-'*15, '票务详情失败', '-'*15))
    finally:
        # 循环退出，直至返回至搜索框
        for _ in range(5):
            if exists(Template(r"tpl1638499859633.png", record_pos=(-0.415, -0.525), resolution=(1080, 1920))) is not False:
                break
            else:
                if exists(Template(r"tpl1638500210883.png", threshold=0.8, record_pos=(0.446, -0.796), resolution=(1080, 1920))) is not False:
                    touch(Template(r"tpl1638499578147.png", record_pos=(0.448, -0.795), resolution=(1080, 1920)))
                else:
                    keyevent("4")
    for _ in range(2):
        swipe((0.5*width, 0.75*height), (0.5*width, 0.35*height))  # 向下滑动
        sleep()
    snapshot(msg="票务tab下滑留痕")
    sleep()
    touch(exists(Template(r"tpl1634796109904.png", threshold=0.8, record_pos=(0.447, -0.794), resolution=(1080, 1920))))
    sleep()
except:
    print("%s%s%s"  % ('-'*15, '校验票务tab失败', '-'*15))
finally:
    # 循环退出，直至返回至搜索框
    for _ in range(5):
        if exists(Template(r"tpl1638499859633.png", record_pos=(-0.415, -0.525), resolution=(1080, 1920))) is not False:
            break
        else:
            if exists(Template(r"tpl1638500210883.png", threshold=0.8, record_pos=(0.446, -0.796), resolution=(1080, 1920))) is not False:
                touch(Template(r"tpl1638499578147.png", record_pos=(0.448, -0.795), resolution=(1080, 1920)))
            else:
                keyevent("4")

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
finally:
    # 循环退出，直至返回至搜索框
    for _ in range(5):
        if exists(Template(r"tpl1638499859633.png", record_pos=(-0.415, -0.525), resolution=(1080, 1920))) is not False:
            break
        else:
            if exists(Template(r"tpl1638500210883.png", threshold=0.8, record_pos=(0.446, -0.796), resolution=(1080, 1920))) is not False:
                touch(Template(r"tpl1638499578147.png", record_pos=(0.448, -0.795), resolution=(1080, 1920)))
            else:
                keyevent("4")



