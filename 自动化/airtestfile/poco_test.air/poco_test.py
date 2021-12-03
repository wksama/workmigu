# -*- encoding=utf8 -*-
__author__ = "86245"

from airtest.core.api import *

auto_setup(__file__)

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

# 获取当前设备的分辨率
width, height = device().get_current_resolution()
print(width, height)
# poco(text="咪咕音乐")
#poco("com.mumu.launcher:id/workspace").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.widget.TextView")[4]

poco.click((0.325,0.385))


poco(text="曾经我也想过一了百了（《披荆斩棘的哥哥》第9期）")
poco("android.widget.LinearLayout").offspring("android:id/content").offspring("cmccwm.mobilemusic:id/fl_fragment_container").offspring("cmccwm.mobilemusic.lib_music:id/song_fresh_recyclerView").child("cmccwm.mobilemusic.lib_music:id/rootview")[0].offspring("cmccwm.mobilemusic:id/songName")

poco("android.widget.LinearLayout").offspring("android:id/content").offspring("cmccwm.mobilemusic:id/fl_fragment_container").offspring("cmccwm.mobilemusic.lib_music:id/song_fresh_recyclerView").child("cmccwm.mobilemusic.lib_music:id/rootview")[1].offspring("cmccwm.mobilemusic:id/songName")

