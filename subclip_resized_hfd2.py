import cv2
import os


import os
import numpy as np

in_dir = '/home/shassan/DRS_Project_Event_based_vision/Data_resized_hfd2_MWIR/'


pos_ann = []
neg_ann = []

first_sub = os.listdir(in_dir)
count = 0
for i in range(0, len(first_sub)):
    if first_sub[i] in ['subclip_resized_hfd2.py' ,  'resize.py']:
        continue
    first_sub_path = os.listdir(in_dir+first_sub[i]+'/')
    for j in range(len(first_sub_path)):
        print('i: ',i, ' j: ',j)
        print(count)
        if first_sub_path[j] in ('A010'):
            continue
        second_sub_path = in_dir+first_sub[i]+'/'+first_sub_path[j]+'/MWIR/'
        print(second_sub_path)
        
        imgs = sorted(os.listdir(second_sub_path))
	
        frame_num = 0
        fold_num = 0
        for k in range(0,len(imgs)):
            #print('frame_num: ',frame_num)
            #print('fold_num: ',fold_num)
            frame_num += 1
            frame = cv2.imread(second_sub_path+imgs[k])

            # Display the resulting frame
            if 1:
                if count%2 == 0:
                    frames_path = second_sub_path.replace(
                    'Data_resized_hfd2_MWIR', 'Data_resized_hfd2_MWIR_subclips/Positives')
                else:
                    frames_path = second_sub_path.replace(
                    'Data_resized_hfd2_MWIR', 'Data_resized_hfd2_MWIR_subclips/Negatives')
                if not os.path.exists(frames_path+str(fold_num)):
                    os.makedirs(frames_path+str(fold_num))
                    
                #print(frames_path + str(fold_num) + '/' +str(frame_num) + '_frame.png')
                    
                cv2.imwrite(frames_path + str(fold_num) + '/' +str(frame_num) + '_frame.png', frame)
                if frame_num % 16 == 0:
                    if count%2 ==0:
                    	pos_ann.append(frames_path+str(fold_num))
                    else:
                    	neg_ann.append(frames_path+str(fold_num))
                    count += 1
                    #print(count)
                    fold_num += 1
                    frame_num = 0

print(count)
np.save('pos_ann.npy' , np.array(pos_ann))
np.save('neg_ann.npy' , np.array(neg_ann))
print(pos_ann[:10])
print(neg_ann[:10])
print(len(pos_ann))
print(len(neg_ann))


