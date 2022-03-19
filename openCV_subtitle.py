import cv2
import time
import numpy as np

#video = cv2.VideoCapture("C:/Users/llsa0/Downloads/dramaresult.avi")

def writeVideo():
    video = cv2.VideoCapture("C:/Users/llsa0/Downloads/text.mp4")

    # 프레임의 width와 height가져와서 size로 저장
    fps = video.get(cv2.CAP_PROP_FPS ) #fps는 그대로 가져온다
    vid_size = (round(video.get(cv2.CAP_PROP_FRAME_WIDTH)), round(video.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    fcc = cv2.VideoWriter_fourcc('D', 'I', 'V', 'X')

    out = cv2.VideoWriter('C:/Users/llsa0/Downloads/out.avi', fcc, fps, vid_size)

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

        # cv2.imshow('Result', cv2.resize(frame, (1300, 800)))
        out.write(frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            video.release()
            out.release()
            cv2.destroyWindow('Result')
            break

writeVideo()