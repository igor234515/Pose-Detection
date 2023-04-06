import points_analysis.side_camera as side
import cv2
import os
from show_points import on_image
import json_to_points

colors_file=r'other/colors.json'
# igor's points

# points=['nose', 'right_eye', 'left_eye', 'right_ear',
#           'left_ear', 'right_shoulder', 'left_shoulder',
#           'right_elbow', 'left_elbow', 'right_brush',
#           'left_brush', 'right_hip', 'left_hip', 'right_knee',
#           'left_knee', 'right_ankle', 'left_ankle', 'breast',
#           'top', 'right_big_toe', 'right_small_toe', 'right_knee',
#           'left_big_toe', 'left_small_toe', 'left_heel']

# robert's points
points=['chin',"breast",'left_shoulder','left_elbow','left_brush','right_shoulder','right_elbow','right_brush',
            'groin','left_hip','left_knee','left_ankle','right_hip','right_knee','right_ankle','left_eye','right_eye',
            'left_ear','right_ear','right_foot_mid','right_foot_front',
           'right_foot_back','left_foot_mid','left_foot_front','left_foot_back']
def main():
    path_image = r'D:\hockey\pose\tdn'
    path_dict = r'D:\hockey\json_1909\json_1909'
    for n in os.listdir(path_image):
        name=os.path.join(path_image,n)
        image=cv2.imread(name)
        # номер кадра
        #TODO( сделать реализацию получше)
        num_frame=n.split('.')[0].split('_')[-1]
        file_list=os.listdir(path_dict)
        # shablon='IMG_1909_000000000000_keypoints.json'
        # print(file_list[0].split['_'])
        file_num_rand=file_list[0].split('_')[-2]
        file_num_=file_num_rand[:-len(num_frame)]+num_frame
        file_point_old=file_list[0].replace(file_num_rand,file_num_)
        file_point_old=os.path.join(path_dict,file_point_old)
        dict_points = json_to_points.json_to_points(file_point_old)
        new_image = on_image(dict_points, image, points=points)
        new_image=side.angles(new_image,file_point_old)
        new_image=cv2.resize(new_image,dsize=(int(image.shape[1]*0.8),int(image.shape[0]*0.8)))
        cv2.imshow('show', new_image)
        cv2.waitKey()

main()

# print(points[8])