# -*- encoding=utf8 -*-
__author__ = "SMZ"

from airtest.core.api import *

auto_setup(__file__)


'''搜索启动页操作'''
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
    # 点击&键入搜索词
    touch((0.1*width, 0.05*height))
    text("周杰伦")
    sleep(2)
    touch(exists(Template(r"tpl1634796109904.png", threshold=0.8, record_pos=(0.447, -0.794), resolution=(1080, 1920))))
    sleep()
    touch((0.525*width, 0.06*height))
    sleep()
    # 点击&键入搜索词
    touch((0.1*width, 0.05*height))
    text("迪克牛仔")
    sleep(2)
    touch(exists(Template(r"tpl1634796109904.png", threshold=0.8, record_pos=(0.447, -0.794), resolution=(1080, 1920))))
    sleep()
    
    # 判定搜索历史&删除单条搜索历史
    if exists(Template(r"tpl1634797695251.png", threshold=0.9, rgb=True, record_pos=(-0.417, -0.697), resolution=(1080, 1920))) is not False:
        swipe(Template(r"tpl1634797743061.png", record_pos=(-0.384, -0.614), resolution=(1080, 1920)), Template(r"tpl1634797743061.png", record_pos=(-0.384, -0.614), resolution=(1080, 1920)), duration=3) # 模拟长按
        sleep()
        if exists(Template(r"tpl1634797948928.png", threshold=0.8, target_pos=3, record_pos=(-0.387, -0.613), resolution=(1080, 1920))) is not False:
            print("%s%s%s"  % ('-'*15, '关闭单条记录', '-'*15))
            touch(Template(r"tpl1634798456186.png", threshold=0.85, target_pos=3, record_pos=(-0.386, -0.613), resolution=(1080, 1920))) # 点击图片3位置，叉掉此搜索记录
            sleep()
            print("%s%s%s"  % ('-'*15, '关闭单条记录成功', '-'*15))
            assert_not_exists(Template(r"tpl1634798055898.png", threshold=0.85, rgb=True, record_pos=(-0.384, -0.612), resolution=(1080, 1920)), "删除后应不存在此搜索记录")
        else:
            print("%s%s%s"  % ('-'*15, '未识别单条记录，关闭失败', '-'*15))
    else:
        print("%s%s%s"  % ('-'*15, '无搜索历史', '-'*15))

    # 删除多条
    if exists(Template(r"tpl1634798875702.png", threshold=0.85, record_pos=(-0.408, -0.695), resolution=(1080, 1920))) is not False:
        touch(Template(r"tpl1634798919303.png", threshold=0.85, record_pos=(0.459, -0.695), resolution=(1080, 1920)))
        sleep(2)
        if exists(Template(r"tpl1634808811343.png", threshold=0.8, record_pos=(0.132, 0.103), resolution=(1080, 1920))) is not False:
            sleep()
            touch(Template(r"tpl1634808907536.png", record_pos=(0.131, 0.105), resolution=(1080, 1920)))
            sleep()
    else:
        print("%s%s%s"  % ('-'*15, '搜索历史多条未删掉', '-'*15))
    
    '''显示搜索发现&不显示搜索历史'''
    try:
        assert_not_exists(Template(r"tpl1634799172686.png", threshold=0.9, record_pos=(-0.412, -0.698), resolution=(1080, 1920)), "无搜索历史")
        sleep()
        assert_exists(Template(r"tpl1634799540477.png", threshold=0.9, rgb=True, record_pos=(-0.411, -0.701), resolution=(1080, 1920)), "显示搜索发现")
        sleep()
    except:
        print("%s%s%s"  % ('-'*15, '搜索发现校验失败', '-'*15))
        
    '''显示各卡片信息'''
    try:
        swipe((0.2*width,0.6*height),(0.6*width,0.6*height))
        sleep()
        assert_exists(Template(r"tpl1634800389899.png", threshold=0.9, rgb=False, record_pos=(-0.382, -0.406), resolution=(1080, 1920)), "搜索飙升存在")
        sleep()
        assert_exists(Template(r"tpl1634800812723.png", threshold=0.9, record_pos=(0.153, -0.316), resolution=(1080, 1920)), "热评歌曲存在")
        sleep()
        for _ in range(2):
            swipe((0.8*width,0.6*height),(0.2*width,0.6*height))
            sleep()
        assert_exists(Template(r"tpl1634801010917.png", threshold=0.9, record_pos=(0.056, -0.32), resolution=(1080, 1920)), "视频热播存在")
        sleep()
        
        # 校验播放
        for _ in range(2):
            swipe((0.2*width,0.6*height),(0.8*width,0.6*height))
            sleep()
        if exists(Template(r"tpl1634801575182.png", threshold=0.9, record_pos=(-0.053, -0.499), resolution=(1080, 1920))) is not False:
            touch(Template(r"tpl1634801609238.png", threshold=0.9, record_pos=(-0.049, -0.499), resolution=(1080, 1920))) # 点击播放
            sleep()
            try:
                if exists(Template(r"tpl1634801765020.png", threshold=0.8, record_pos=(0.344, 0.839), resolution=(1080, 1920))) is not False or exists(Template(r"tpl1634801791477.png", threshold=0.8, record_pos=(0.393, 0.842), resolution=(1080, 1920))) is not False:
                    print("%s%s%s"  % ('-'*15, '卡片歌曲播放成功', '-'*15))
                    sleep(3)
                    touch(Template(r"tpl1634802154301.png", threshold=0.85, record_pos=(0.347, 0.839), resolution=(1080, 1920)))
                    sleep()
                else:
                    print("%s%s%s"  % ('-'*15, '卡片歌曲播放失败', '-'*15))
            except:
                print("%s%s%s"  % ('-'*15, '卡片歌曲播放校验失败', '-'*15))
                
        '''卡片点击跳转'''
        try:
            '''卡片歌曲跳转'''
            for _ in range(2):
                swipe((0.2*width,0.6*height),(0.8*width,0.6*height))
                sleep()
            if exists(Template(r"tpl1634802556508.png", record_pos=(-0.383, -0.319), resolution=(1080, 1920))) is not False:
                touch((0.25*width, 0.75*height)) # 点击歌曲搜索
                sleep(3)
                try:
                    assert_exists(Template(r"tpl1634802824533.png", record_pos=(-0.408, -0.706), resolution=(1080, 1920)), "跳转到搜索结果页")
                    sleep()
                    touch(Template(r"tpl1634804834737.png", threshold=0.85, record_pos=(0.449, -0.794), resolution=(1080, 1920))) # 关闭搜索词
                    sleep(2)
                except:
                    print("%s%s%s"  % ('-'*15, '卡片歌曲跳转失败', '-'*15))
                

            else:
                print("%s%s%s"  % ('-'*15, '卡片歌曲点击失败', '-'*15))

            '''卡片视频跳转'''
            for _ in range(2):
                swipe((0.8*width,0.6*height),(0.2*width,0.6*height))
                sleep()
            if exists(Template(r"tpl1634803320488.png", threshold=0.8, record_pos=(0.059, -0.316), resolution=(1080, 1920))) is not False:
                touch((0.75*width, 0.75*height)) # 点击视频搜索
                sleep(10)
                try:
                    assert_exists(Template(r"tpl1634803494362.png", threshold=0.8, record_pos=(-0.405, -0.097), resolution=(1080, 1920)), "跳转到mv播放页")
                    sleep(2)
                    keyevent("4") # 点击返回
                    sleep(3)
                except:
                    print("%s%s%s"  % ('-'*15, '卡片视频跳转失败', '-'*15))
            else:
                print("%s%s%s"  % ('-'*15, '卡片视频点击失败', '-'*15))
        except:
            print("%s%s%s"  % ('-'*15, '卡片跳转校验失败', '-'*15))
    except:
        print("%s%s%s"  % ('-'*15, '卡片校验失败', '-'*15))
    '''aiui操作'''
    try:
        if exists(Template(r"tpl1634806869231.png", threshold=0.85, record_pos=(0.448, -0.794), resolution=(1080, 1920))) is not False:
            touch(Template(r"tpl1634806903514.png", threshold=0.8, record_pos=(0.446, -0.797), resolution=(1080, 1920)))
            sleep(5)
            if exists(Template(r"tpl1634807420355.png", record_pos=(0.131, 0.248), resolution=(1080, 1920))) is not False or exists(Template(r"tpl1634807566640.png", record_pos=(-0.14, 0.245), resolution=(1080, 1920))) is not False or  exists(Template(r"tpl1634807598075.png", record_pos=(-0.022, -0.176), resolution=(1080, 1920))) is not False:
                touch(Template(r"tpl1634807623596.png", record_pos=(-0.134, 0.244), resolution=(1080, 1920)))
            else:
                print("%s%s%s"  % ('-'*15, 'aiui麦克风已操作', '-'*15))
        else:
            print("%s%s%s"  % ('-'*15, 'aiui未找到', '-'*15))

    except:
        print("%s%s%s"  % ('-'*15, 'aiui操作失败', '-'*15))
    
    '''换肤操作'''
    try:
        for _ in range(2):
            keyevent("4")  # 返回主页面
            sleep(5)
            if exists(Template(r"tpl1634810489480.png", threshold=0.85, record_pos=(0.439, -0.786), resolution=(1080, 1920))) is not False:
                break

        if exists(Template(r"tpl1634808164798.png", threshold=0.85, record_pos=(0.434, -0.788), resolution=(1080, 1920))) is not False:
            touch(Template(r"tpl1634808203496.png", threshold=0.85, record_pos=(0.439, -0.79), resolution=(1080, 1920)))
            sleep(5)
            if exists(Template(r"tpl1634808299984.png", record_pos=(-0.357, -0.633), resolution=(1080, 1920))) is not False:
                touch(Template(r"tpl1634808332172.png", record_pos=(-0.356, -0.634), resolution=(1080, 1920)))
                sleep(5)
            elif exists(Template(r"tpl1634808370757.png", record_pos=(-0.366, -0.633), resolution=(1080, 1920))) is not False:
                touch(Template(r"tpl1634808400880.png", record_pos=(-0.366, -0.631), resolution=(1080, 1920)))
                sleep(5)
            else:
                print("%s%s%s"  % ('-'*15, '主题换肤未找到', '-'*15))
            
            try:
                assert_exists(Template(r"tpl1634808564254.png", record_pos=(-0.302, -0.781), resolution=(1080, 1920)), "主题换肤校验")
            except:
                print("%s%s%s"  % ('-'*15, '换肤操作失败', '-'*15))
    except:
        print("%s%s%s"  % ('-'*15, '换肤操作失败', '-'*15))
    
    # 返回主界面
    for _ in range(2):
        keyevent("4")
        sleep(3)
        if exists(Template(r"tpl1634810489480.png", threshold=0.85, record_pos=(0.439, -0.786), resolution=(1080, 1920))) is not False:
            break   
except:
    print("%s%s%s"  % ('-'*15, '搜索启动页操作失败', '-'*15))

