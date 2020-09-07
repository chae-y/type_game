import random
import time
import hgtk
import os

WORD_LIST = [
    "고마운 마음이 자꾸 많이 남아서",
    "내게 해줬던 그 말이 귓가에 맴돌아서",
    "오늘도 전혀 안 추워 따뜻한 이 겨울엔",
    "내 곁엔 항상 너 항상 너 곁에 있으니",
]

random.shuffle(WORD_LIST)
list_len = len(WORD_LIST)
current_count = 0

while current_count < list_len:
    os.system("cls")
    q = WORD_LIST[current_count]
    current_count += 1

    start_time = time.time()
    user_input = input(q+ '\n')
    end_time = time.time() - start_time

    src = hgtk.text.decompose(q).replace("ᴥ","")
    tar = hgtk.text.decompose(user_input).replace("ᴥ","")

    correct=0
    for i, c in enumerate(src, start=0):
        try:
            if tar[i]==c:
                correct += 1
        except:
            pass
    src_len = len(src)
    c = correct/src_len*100 #정확도
    e=(src_len-correct)/src_len*100 #오타율
    speed = float(correct/end_time)*60
    print("속도: {:0.2f} 정확도: {:0.2f}% 오타율: {:0.2f}%".format(speed,c,e))
    os.system("pause")
