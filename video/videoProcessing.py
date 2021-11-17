import os
import pandas as pd
from pytube import YouTube
from moviepy.editor import *
import librosa
import soundfile as sf
import numpy as np
import shutil

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# 경로 정의
DATA_IN_PATH = 'C:\\Users\\llsa0\\PBL4_speechtext\\PBL4\\video\\data\\'

def main(video, idd=0):
    data_output = DATA_IN_PATH + str(idd) + "\\"
    print(bcolors.OKGREEN + '\nplease wait! \n' + bcolors.ENDC)

    # 파일 복사하기 (사본 생성)
    shutil.copy2(DATA_IN_PATH+video, data_output+"copied_"+video)
    print(bcolors.OKGREEN + '\nMake copy of video ! \n' + bcolors.ENDC)

    videoclip = VideoFileClip(data_output+"copied_"+video)
    audioclip = videoclip.audio
    audioclip.write_audiofile(data_output+"copy.wav") # 음성 wav 추출하기
    print(bcolors.OKGREEN + '\nChage mp4 to wav ! \n' + bcolors.ENDC)

    y =  [0,1,0,0,0,1,0,0,1,0]
    #      0 1 2 3 4 5 6 7 8 9
    # 0 3~4 6~7

    # 0    1    2  3
    # a   1.0  3.0 아메리카노
    make_quiet_wav(data_output+"copy.wav", y, data_output+"{}_result_{}.wav".format(idd, video))
    videoclip = videoclip.set_audio(AudioFileClip(data_output+"{}_result_{}.wav".format(idd, video)))
    videoclip = videoclip.subclip(0,8)
    videoclip.write_videofile(data_output+"{}_result_{}".format(idd,video))

    print(bcolors.OKGREEN + '\nNow you can check!!! ' + bcolors.ENDC)

    # 데이터 길이 10개, 0->1로 바뀌는 구간 총 5번. 실제 묵음 처리 5번
    # 데이터 길이 5개, 0->1로 바뀌는 구간 2번. 실제 묵음 동일.
    # 영상 길이와 데이터 길이에 따라 구간 변경?
    # 영상 길이에 따라 간격은 달라지는 것 같음.
    # 앞 팀에게 데이터 요청시 start time 과 endtime 분배 요청하기

def make_quiet_wav(wav, y, output_name):
    quiet, _ = librosa.load(DATA_IN_PATH+'quiet.wav', sr = 44100)
    data, _ = librosa.load(wav, sr=44100)
    length = len(y)
    for i in range(1, length):
        tmp = int(len(data)*(i)/length)
        t_1 = y[i-1] # 이전 구간
        t = y[i] # 현재구간
        if (t_1 == 0) and (t == 1):
            if tmp > 22000 :
                data[tmp-22000:tmp] = quiet[:22000] * 1.0
            else:
                data[:tmp] = quiet[:tmp] * 1.0  #a[2]-a[1]
    sf.write(output_name, data, 44100)

if __name__ == '__main__':
    video= "4_result_example.mp4"
    idd = int(input('ID: '))
    data_output = DATA_IN_PATH  + str(idd) + "\\"
    try:
        if not os.path.exists(data_output):
            os.makedirs(data_output)
    except OSError:
        print('Error: Creating directory. ' + data_output)
        quit()

    main(video,idd)
    print(bcolors.OKGREEN + '\nDone !!! \n' + bcolors.ENDC)