import cv2
from moviepy.editor import *
import time
import numpy as np

#video = cv2.VideoCapture("dramaresult.avi")

def writeVideo():
    # 비디오 처리
    video = cv2.VideoCapture("resultOserver.mp4")

    # 프레임의 width와 height가져와서 size로 저장
    fps = video.get(cv2.CAP_PROP_FPS ) #fps는 그대로 가져온다
    vid_size = (round(video.get(cv2.CAP_PROP_FRAME_WIDTH)), round(video.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    fcc = cv2.VideoWriter_fourcc('D', 'I', 'V', 'X')

    #fcc = cv2.VideoWriter_fourcc(*'mp4v')  # mp4v 코덱

    out = cv2.VideoWriter('out.avi', fcc, fps, vid_size)
    #out = cv2.VideoWriter('out.mp4', fcc, fps, vid_size)

    # prevTime = 0

    while (True):
        ret, frame = video.read()
        #curTime = time.time()
        #sec = curTime - prevTime
        #prevTime = curTime
        #fps = 1 / (sec)

        str = "Currently, harmful language has been detected and muted."
        # "현재 유해언어가 감지되어 음소거 처리되었습니다."
        cv2.rectangle(frame, (120, 400), (730, 450), (105, 105, 105), -1)
        cv2.putText(frame, str, (170, 430), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255))
        cv2.imshow('Result', cv2.resize(frame, (1300, 800)))
        out.write(frame)

        # start = time.time()
        # length = start + (int(video.get(cv2.CAP_PROP_FRAME_COUNT)) / fps)

        # time.sleep(length)

        # video.release()
        # out.release()
      
        # exit()

        if cv2.waitKey(1) & 0xFF == ord('q'): # q를 꼭 눌러줘야한다고 안내문 띄우기 (엔터나 다른 걸로)
            video.release()
            out.release()
            cv2.destroyWindow('Result')
            videoclip = VideoFileClip("out.avi")  # 자막 처리된 걸 비디오 클립
            audioclip = AudioFileClip("resultOserver.mp4")  # 음성 파일은 무음 처리된 음성용

            videoclip.audio = audioclip  # 자막 처리된 영상에 무음 덮어씌우는거
            videoclip.write_videofile("new.mp4")  # 새로운 파일로 만드는 거
            break

writeVideo()
