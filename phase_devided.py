import cv2
import time
import os

# Подготовка толчка ногой - птн
# Толчковое движение ногой - тдн
# Окончание толчка ногой - отн

queue=['птн','тдн','отн']
# тупой cv2 не может в рускоязычную папку сохранять поэтому нужно это
english=['ptn','tdn','otn']
def read_timecodes(file_txt:str,video: str,save_dir:str):

    # создание папок для сохранения
    if not(os.path.exists(save_dir)):
        os.mkdir(save_dir)
    for p in english:
        path=os.path.join(save_dir,p)
        if not (os.path.exists(path)):
            os.mkdir(path)

    # олучение характерисик видео
    cap = cv2.VideoCapture(video)
    (major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')

    # With webcam get(CV_CAP_PROP_FPS) does not work.
    # Let's see for ourselves.

    if int(major_ver) < 3:
        fps = cap.get(cv2.cv.CV_CAP_PROP_FPS)
        fps = round(fps)
        print("Frames per second using video.get(cv2.cv.CV_CAP_PROP_FPS): {0}".format(fps))
    else:
        fps = cap.get(cv2.CAP_PROP_FPS)
        fps = round(fps)
        print("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))

    # чтение разметки видео по фазам
    with open(file_txt, encoding = 'utf-8') as f:
        data=f.readlines()

    # находим первую записанную позу
    start=data[0]
    for i in range(3):
        if queue[i] in start:
            start_pose=queue[i]
            start_index=i
            start_frame=int(float(start.split('-')[0])*fps)
            print(start_frame)
            break
    #Индекс строки в которой написана следующая фаза т.е. когда нам надо остановиться
    txt_next_index=1
    stop_frame = int(float(data[txt_next_index].split('-')[0]) * fps)
    #Проход по всем кадрам видео
    num=0
    save_dir_pose=os.path.join(save_dir,start_pose)
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            break
        if num>=start_frame:
            # Идет позиция start_pose. Она обновляемая
            # image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            name=os.path.join(save_dir_pose,os.path.basename(video).split('.')[0]+'frame_'+str(num)+'.jpg')

            cv2.imwrite(name,image)

            if num>=stop_frame:
                print(start_pose,stop_frame)
                start_index=(start_index+1)%3
                start_pose=queue[start_index]
                txt_next_index+=1
                try:
                    stop_frame=int(float(data[txt_next_index].split('-')[0])*fps)
                except IndexError:
                    stop_frame=1e10
                english_pose=english[start_index]
                save_dir_pose = os.path.join(save_dir, english_pose)
        num+=1
    print('end function work')

read_timecodes(r"D:\hockey\phase_1909.txt",r"D:\hockey\IMG_1909.MOV",r"D:\hockey\pose")