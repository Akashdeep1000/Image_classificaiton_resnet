#!/usr/bin/env python
import os
import numpy as np

in_dir = '/home/achakraborty/DRS_Project_Event_based_vision/resized_hfd2/'



first_sub = os.listdir(in_dir)

for i in range(len(first_sub)):
	#print('i: ',i)
	if first_sub[i] in ('resize.py'):
		continue
	first_sub_path = os.listdir(in_dir+first_sub[i]+'/')
	for j in range(len(first_sub_path)):
		#print('j: ',j)
		if first_sub_path[j] in ('A010'):
			continue
		second_sub_path = in_dir+first_sub[i]+'/'+first_sub_path[j]+'/MWIR/'
		
		
		out_path = second_sub_path.replace('/resized_hfd2', '/Generate_Events/Generate_Events_Resized_Data/Non_Flash_Events')
		#print(second_sub_path)
		#print(out_path)

		
		os.system('python v2e.py -i ' + second_sub_path +' --overwrite --disable_slomo --input_frame_rate=360 --timestamp_resolution=.003 --auto_timestamp_resolution=False --dvs_exposure duration 0.005 --output_folder='+ out_path +' --overwrite --pos_thres=.15 --neg_thres=.15 --sigma_thres=0.03 --dvs_aedat2 tennis.aedat --output_width=128 --output_height=128 --cutoff_hz=15 --ignore-gooey --no_preview')

'''
a=np.load('matlab_matrix_paths.npy')
total = int(len(a))
for i in range(0,len(a),2):
	clip_path = a[i]
	#print(clip_path)
	
	newton_input_path = '/home/shassan/DRS_Project_Event_based_vision/Generate_Events/Flash_on_Slomo_data' + clip_path.split('ips/cropped')[1]
	#print('---', newton_input_path)
	out_path1 = newton_input_path.split('Flash_on_Slomo_data/')
	out_path = out_path1[0] + 'Generate_events_flash_data_128x128/Flash_Events/' + out_path1[1]
	#print('***',out_path)
	#print('python v2e.py -i ' + newton_input_path +' --overwrite --disable_slomo --input_frame_rate=360 --timestamp_resolution=.003 --auto_timestamp_resolution=False --dvs_exposure duration 0.005 --output_folder='+ out_path +' --overwrite --pos_thres=.15 --neg_thres=.15 --sigma_thres=0.03 --dvs_aedat2 tennis.aedat --output_width=128 --output_height=128 --cutoff_hz=15 --ignore-gooey --no_preview')
	os.system('python v2e.py -i ' + newton_input_path +' --overwrite --disable_slomo --input_frame_rate=360 --timestamp_resolution=.003 --auto_timestamp_resolution=False --dvs_exposure duration 0.005 --output_folder='+ out_path +' --overwrite --pos_thres=.15 --neg_thres=.15 --sigma_thres=0.03 --dvs_aedat2 tennis.aedat --output_width=128 --output_height=128 --cutoff_hz=15 --ignore-gooey --no_preview')
	#break
'''

#python v2e.py -i /home/shassan/DRS_Project_Event_based_vision/Generate_Events/Generate_Events_Resized_Data/test_slomo/MWIR/ --overwrite --disable_slomo --input_frame_rate=60 --timestamp_resolution=.003 --auto_timestamp_resolution=False --dvs_exposure duration 0.005 --output_folder=/home/shassan/DRS_Project_Event_based_vision/Generate_Events/Generate_Events_Resized_Data/test_slomo/MWIR_Slomo/ --overwrite --pos_thres=.15 --neg_thres=.15 --sigma_thres=0.03 --dvs_aedat2 tennis.aedat --output_width=128 --output_height=128 --cutoff_hz=15 --ignore-gooey --no_preview
