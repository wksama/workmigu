from pydub import AudioSegment

'''# 音频的原始文件record.wav
filename = 'record'
# 
wav = AudioSegment.from_wav(filename + '.wav')
# 读取前45分钟的音频并保存在record_cut1.wav中
wav[:45 * 60 * 1000].export(filename + '_cut1.wav', format="wav")
# 读取45分钟以后的音频并保存在record_cut2.wav中
wav[45 * 60 * 1000:].export(filename + '_cut2.wav', format="wav")
'''

wav_name = '111.wav'
wav_path = 'E:\\download\\'
save_path = 'E:\\download\\smz\\'
# 读取音频文件
wav = AudioSegment.from_wav(wav_path + wav_name)
# 获取音频时长
wav_time = wav.duration_seconds
print('wav_time:', wav_time)
# 时长比20倍数和余数
beishu = int(wav_time // 20)
yushu = wav_time % 20
print('beishu:', beishu)
print('yushu:', yushu)
# 20s节点获取排列
time_list = [i * 20 for i in range(beishu + 1)]
# print(time_list)
time_list.append(time_list[-1] + yushu)
print('time_list:', time_list)
for index, data in enumerate(time_list):
    if index == len(time_list) - 1:
        break
    wav[time_list[index] * 1000:time_list[index + 1] * 1000].export(save_path + '%s_cut.wav' % (index + 1),
                                                                    format="wav")
