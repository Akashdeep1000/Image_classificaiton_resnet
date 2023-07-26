import os
import numpy as np
from tqdm import tqdm

in_dir = "C:/Users/adcha/Desktop/output/DRS_Project_Event_based_vision/Data_resized_hfd2_MWIR_subclips/"
# in_dir = "C:/Users/adcha/Desktop/work/RA/Data_resized_hfd2_MWIR_subclips/"

first_sub = os.listdir(in_dir)
#print(first_sub)

for x1 in tqdm(first_sub):
    first_sub_path = os.listdir(in_dir+ x1 +'/')
    #print(first_sub_path)
    for x2 in first_sub_path:
        second_sub_path = os.listdir(in_dir+ x1 +'/'+ x2)

        for x3 in second_sub_path:

            third_sub_path = os.listdir(in_dir+x1+"/"+x2+"/"+x3+"/MWIR")

            for x4 in third_sub_path:

                final_path = in_dir+x1+"/"+x2+"/"+x3+"/MWIR"+"/"+x4

                out_path = final_path.replace('/Data_resized_hfd2_MWIR_subclips', '/Generate_Events/Generate_Events_Resized_Data/Non_Flash_Events')

                os.system('python v2e.py -i ' + final_path +' --overwrite --slomo_model SuperSloMo39.ckpt --input_frame_rate=60 --timestamp_resolution=.003 --auto_timestamp_resolution=False --dvs_exposure duration 0.005 --output_folder='+ out_path +' --overwrite --pos_thres=.15 --neg_thres=.15 --sigma_thres=0.03 --dvs_aedat2 tennis.aedat --output_width=346 --output_height=260 --cutoff_hz=15 --ignore-gooey --no_preview')
                # print('python v2e.py -i ' + final_path +' --overwrite --slomo_model SuperSloMo39.ckpt --input_frame_rate=60 --timestamp_resolution=.003 --auto_timestamp_resolution=False --dvs_exposure duration 0.005 --output_folder='+ out_path +' --overwrite --pos_thres=.15 --neg_thres=.15 --sigma_thres=0.03 --dvs_aedat2 tennis.aedat --output_width=346 --output_height=260 --cutoff_hz=15 --ignore-gooey --no_preview')
                # exit()
                # print('python v2e.py -i ' + final_path +' --overwrite --disable_slomo --input_frame_rate=360 --timestamp_resolution=.003 --auto_timestamp_resolution=False --dvs_exposure duration 0.005 --output_folder='+ out_path +' --overwrite --pos_thres=.15 --neg_thres=.15 --sigma_thres=0.03 --dvs_aedat2 tennis.aedat --output_width=128 --output_height=128 --cutoff_hz=15 --ignore-gooey --no_preview')


#C:\Users\adcha\Desktop\output\DRS_Project_Event_based_vision\Data_resized_hfd2_MWIR_subclips