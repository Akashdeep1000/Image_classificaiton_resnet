import cv2
import numpy as np
import os


in_dir = '/datasets/HFD2/data/'
out_dir ='./data/'

#/datasets/HFD2/data/1June2021/20C/MWIR


first_sub = os.listdir(in_dir)
cnt = 0
for i in range(len(first_sub)):
	print('i: ',i)
	print(f"{i}/{len(first_sub)}")
	if first_sub[i] in ('DRS Daily Log','DRSVideos'):
		continue
	first_sub_path = os.listdir(in_dir+first_sub[i]+'/')
	for j in range(len(first_sub_path)):
		print('j: ',j)
		if first_sub_path[j] in ('A010'):
			continue
		second_sub_path = os.listdir(in_dir+first_sub[i]+'/'+first_sub_path[j]+'/MWIR/')
		for k in range(len(second_sub_path)):
			raw_file_path = str(in_dir+first_sub[i]+'/'+first_sub_path[j]+'/MWIR/'+second_sub_path[k])
			print('raw_file_path: ',raw_file_path)

			cnt+=1
			
			frame = np.fromfile(raw_file_path, dtype=np.uint16)
			frame = np.reshape(frame, (514, 640))
			frame = np.flip(frame)
			frame = np.array(frame)
			dim = (128, 128)
			resized = cv2.resize(frame, dim)
			out_path = '/home/achakraborty/DRS_Project_Event_based_vision/Data_resized_hfd2_MWIR/'+first_sub[i]+'/'+first_sub_path[j]+'/MWIR/'
			if not os.path.exists(out_path):
				os.makedirs(out_path)
			
			print('png file path: ',out_path + second_sub_path[k][:-4]+'.png')
			print('\n')
			cv2.imwrite(out_path + second_sub_path[k][:-4]+'.png', resized)	
			
print(cnt)
		

		
			
	

