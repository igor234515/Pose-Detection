import cv2
import numpy as np
import json_to_points
import math
import show_points
import os
# os.chdir("..")

def angle_of_vectors(a, b, c, d):
    dotProduct = a * c + b * d
    # for three dimensional simply add dotProduct = a*c + b*d  + e*f
    modOfVector1 = math.sqrt(a * a + b * b) * math.sqrt(c * c + d * d)
    # for three dimensional simply add modOfVector = math.sqrt( a*a + b*b + e*e)*math.sqrt(c*c + d*d +f*f)
    angle = dotProduct / modOfVector1
    angleInDegree = math.degrees(math.acos(angle))
    return angleInDegree


# TODO( в один файл закинуть этот список иоттуда читать. Во всех файлах он вначале)
points=['chin',"breast",'left_shoulder','left_elbow','left_brush','right_shoulder','right_elbow','right_brush',
            'groin','left_hip','left_knee','left_ankle','right_hip','right_knee','right_ankle','left_eye','right_eye',
            'left_ear','right_ear','right_foot_mid','right_foot_front',
           'right_foot_back','left_foot_mid','left_foot_front','left_foot_back']
def angles(image,file_point_old):
    global points
    # получение точек and отрисовка их
    dict_points = json_to_points.json_to_points(file_point_old)
    # image=show_points.on_image(dict_points, image, points=points)
    # отрисовка вертикали

    # TODO(разобраться с точками и вставить нормалльное обозначение)
    hip1_x,hip1_y,hip1_p=dict_points[points[11]]
    hip2_x, hip2_y, hip2_p = dict_points[points[12]]
    groin_x, groin_y= int((hip1_x+hip2_x)/2),int((hip1_y+hip2_y)/2)

    sh1_x, sh1_y, sh1_p = dict_points[points[6]]
    sh2_x, sh2_y, sh2_p = dict_points[points[5]]

    br_x, br_y = int((sh1_x + sh2_x) / 2), int((sh1_y + sh2_y) / 2)
    image=cv2.line(image, (groin_x,groin_y), (groin_x,0), (0, 255, 0), thickness=2)
    image=cv2.line(image, (groin_x,groin_y), (br_x, br_y), (0, 255, 0), thickness=2)
    # TODO( нормальную функцию написать: угол между двумя прямыми с координатами 2х точек на каждой прямой)
    gr_vec=np.array([groin_x,0])-np.array([groin_x,groin_y])
    br_vec=np.array([br_x,br_y])-np.array([groin_x,groin_y])
    angle_body=angle_of_vectors(br_vec[0],br_vec[1],gr_vec[0],gr_vec[1])
    print('angle angle_body:',angle_body)
    return image

# for
# image=cv2.imread(r"D:\hockey\pose\tdn\IMG_1909frame_277.jpg")
# file_point_old=r"D:\hockey\json_1909\json_1909\IMG_1909_000000000277_keypoints.json"
# image=angles(image,file_point_old)
# cv2.imshow('show', image)
# cv2.waitKey()

