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
DATA_IN_PATH = 'C:\\Users\\llsa0\\PBL4_speechtext\\PBL4\\video\\'

def main(video, idd=0):
    # 파일 복사하기 (사본 생성)
    shutil.copy2(DATA_IN_PATH+"example.mp4", DATA_IN_PATH+"copy.mp4")
    print(bcolors.OKGREEN + '\nMake copy of video ! \n' + bcolors.ENDC)

    videoclip = VideoFileClip(DATA_IN_PATH+"copy.mp4")
    audioclip = videoclip.audio
    audioclip.write_audiofile(DATA_IN_PATH+"copy.wav") # 음성 wav 추출하기
    print(bcolors.OKGREEN + '\nChage mp4 to wav ! \n' + bcolors.ENDC)

    y = [0,1,1,0,0,1,0]
    make_quiet_wav(DATA_IN_PATH+"copy.wav", y, DATA_IN_PATH+"demo\\result_{}.wav".format( video))
    videoclip = videoclip.set_audio(AudioFileClip(DATA_IN_PATH+"demo\\result_{}.wav".format(video)))
    videoclip = videoclip.subclip(0, 8)
    videoclip.write_videofile(DATA_IN_PATH+"demo\\result_{}.mp4".format(video))

    videoclip = VideoFileClip(DATA_IN_PATH+"copy.mp4")
    videoclip = videoclip.subclip(28, 34)
    videoclip.write_videofile(DATA_IN_PATH+"demo\\origin_{}.mp4".format(video))
    print(bcolors.OKGREEN + '\nNow you can check!!! ' + bcolors.ENDC)

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
                data[tmp-22000:tmp] =  quiet[:22000]*0.5
            else:
                data[:tmp] =  quiet[:tmp]*0.5
    sf.write(output_name, data, 44100)

if __name__ == '__main__':
    video= "copy.mp4"
    main(video)
    print(bcolors.OKGREEN + '\nDone !!! \n' + bcolors.ENDC)