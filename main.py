import points_analysis.side_camera as side
import cv2
import os
from show_points import on_image
import json_to_points
import points_analysis.front_camera as front
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
def main(path_image,path_dict,camera):
    if camera=='side':
        support_leg=180
        phases=side.define_opr_leg(path_image,path_dict)
        ind_phases=0

        list_image=[]
        list_points=[]
        last_num_image=0
        for n in os.listdir(path_image ):
            name=os.path.join(path_image,n)
            image=cv2.imread(name)
            # номер кадра
            #TODO( сделать реализацию получше)
            num_frame=n.split('.')[0].split('_')[-1]
            file_list=os.listdir(path_dict)
            file_num_rand=file_list[0].split('_')[-2]
            file_num_=file_num_rand[:-len(num_frame)]+num_frame
            file_point_old=file_list[0].replace(file_num_rand,file_num_)
            file_point_old=os.path.join(path_dict,file_point_old)
            dict_points = json_to_points.json_to_points(file_point_old)
            new_image = on_image(dict_points, image, points=points)
            # for opr leg
            num=int(name.split('.')[-2].split('_')[-1])
            print(num)
            if num-last_num_image>1:
                ind_phases+=1
                string='angle support: ' + str(support_leg)+'. NEED 180'
                ord_y = new_image.shape[0] - 400
                ord_x = new_image.shape[1] - 550
                new_image = cv2.putText(new_image , string, (ord_x, ord_y), cv2.FONT_HERSHEY_SIMPLEX,
                                    0.5, (0, 0,255), 1, cv2.LINE_AA)
            else:
                ph=phases[ind_phases]
                new_image = side.write_opr_leg(new_image, dict_points,ph)
                new_image,support_leg = side.angles(new_image, dict_points,ph, True)
            last_num_image=num

            new_image=cv2.resize(new_image,dsize=(int(image.shape[1]*0.8),int(image.shape[0]*0.8)))
            cv2.imshow('show', new_image)
            cv2.waitKey()
    else:
        ind_phases = 0
        last_num_image = 0
        for n in os.listdir(path_image):
            name = os.path.join(path_image, n)
            image = cv2.imread(name)
            # номер кадра
            # TODO( сделать реализацию получше)
            num_frame = n.split('.')[0].split('_')[-1]
            file_list = os.listdir(path_dict)
            file_num_rand = file_list[0].split('_')[-2]
            file_num_ = file_num_rand[:-len(num_frame)] + num_frame
            file_point_old = file_list[0].replace(file_num_rand, file_num_)
            file_point_old = os.path.join(path_dict, file_point_old)
            dict_points = json_to_points.json_to_points(file_point_old)
            new_image = on_image(dict_points, image, points=points)
            new_image = front.angles(new_image, dict_points)
            new_image = front.leg(new_image, dict_points)
            new_image = front.elbow(new_image, dict_points)
            # for opr leg

            # num = int(name.split('.')[-2].split('_')[-1])
            # print(num)
            # if num - last_num_image > 1:
            #     ind_phases += 1
            # else:
            #     ph = phases[ind_phases]
            #     new_image = side.write_opr_leg(new_image, dict_points, ph)
            # last_num_image = num
            # print(image)
            new_image = cv2.resize(new_image, dsize=(int(image.shape[1] * 0.8), int(image.shape[0] * 0.8)))
            cv2.imshow('show', new_image)
            cv2.waitKey()




i=0
camers=['side','front']
if i==0:
    path_image = r'D:\hockey\pose\tdn'
    path_dict = r'D:\hockey\json_1909\json_1909'
else:

    path_image = r'D:\hockey\front_all\ptn l'
    path_dict = r'D:\hockey\json_1904\json_1904'

main(path_image,path_dict,camers[i])