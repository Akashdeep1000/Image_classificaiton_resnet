import numpy as np
import random
import cv2
from tqdm import tqdm
import os

in_dir = "C://Users//adcha//Desktop//output//DRS_Project_Event_based_vision//Generate_Events//Generate_Events_Resized_Data//Non_Flash_Events_no_noise//"
out_dir = "C://Users//adcha//Desktop//output//DRS_Project_Event_based_vision//Generate_Events//Generate_Events_Resized_Data//Non_Flash_Events_withnoise_15//"
first_sub = os.listdir(in_dir)
print(first_sub)

max_frames = 1000


def sp_noise(image,prob):
    '''
    Add salt and pepper noise to image
    prob: Probability of the noise
    '''
    output = np.zeros(image.shape,np.uint8)
    thres = 1 - prob 
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]
    return output

for x1 in tqdm(first_sub):
    first_sub_path = os.listdir(in_dir+ x1 +'//')
    os.mkdir(out_dir+ x1 +'//')
    for x2 in first_sub_path:
        second_sub_path = os.listdir(in_dir+ x1 +'//'+ x2)
        os.mkdir(out_dir+ x1 +'//'+x2+"//")

        for x3 in second_sub_path:

            third_sub_path = os.listdir(in_dir+x1+"//"+x2+"//"+x3+"//MWIR//")
            os.mkdir(out_dir+ x1 +'//'+x2+"//"+x3)
            os.mkdir(out_dir+ x1 +'//'+x2+"//"+x3+"//MWIR//")

            for x4 in third_sub_path:

                fourth_sub_path = os.listdir(in_dir+x1+"//"+x2+"//"+x3+"//MWIR"+"//"+x4+"//")
                os.mkdir(out_dir+x1+"//"+x2+"//"+x3+"//MWIR"+"//"+x4+"//")
                
                for x5 in fourth_sub_path:
                    final_path = in_dir+x1+"//"+x2+"//"+x3+"//MWIR"+"//"+x4+"//"+x5
                    final_path_out = out_dir+x1+"//"+x2+"//"+x3+"//MWIR"+"//"+x4+"//"+x5

                    clip = final_path
                    image = cv2.imread(clip , 0)
                    noise_img = sp_noise(image,0.15)#0.004, 0.0065, 0.009, 0.0115
                    cv2.imwrite(final_path_out, noise_img)
   
 