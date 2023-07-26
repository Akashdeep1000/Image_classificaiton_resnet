import os
import numpy as np
from tqdm import tqdm
import cv2

in_dir = "C://Users//adcha//Desktop//output//DRS_Project_Event_based_vision//Generate_Events//Generate_Events_Resized_Data//Non_Flash_Events//"
# in_dir = "C:/Users/adcha/Desktop/work/RA/Data_resized_hfd2_MWIR_subclips/"

first_sub = os.listdir(in_dir)
#print(first_sub)

positive_events = []
negative_events = []

count = 0

for x1 in tqdm(first_sub):
    first_sub_path = os.listdir(in_dir+ x1 +'//')
    #print(first_sub_path)
    for x2 in first_sub_path:
        second_sub_path = os.listdir(in_dir+ x1 +'//'+ x2)

        for x3 in second_sub_path:

            third_sub_path = os.listdir(in_dir+x1+"//"+x2+"//"+x3+"//MWIR")

            for x4 in third_sub_path:

                final_path = in_dir+x1+"//"+x2+"//"+x3+"//MWIR"+"//"+x4+"//"
                # print(os.listdir(final_path))

                clip = final_path
                vid = cv2.VideoCapture(clip + 'dvs-video.avi')
                if not os.path.exists(clip + 'dvs-video.avi'):
                    continue
                frame_num = 0
                while(True):
                    frame_num += 1
                    ret, frame = vid.read()

                    # Display the resulting frame
                    try:
                        frames_path = clip.replace(
                            x1, x1+"_Flash_Noise_Events_Frames")
                        if frame_num == 1:
                            if x1=="Positives":
                                positive_events.append(frames_path)
                            else:
                                negative_events.append(frames_path)
                        if not os.path.exists(frames_path):
                            os.makedirs(frames_path)

                        cv2.imwrite(frames_path + str(frame_num) + '.png', frame)
                        print(frames_path + str(frame_num) + '.png')
                    except:
                        #print('except')
                        break
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
                vid.release()
                cv2.destroyAllWindows()



               

print(count)
# np.save('C:/Users/adcha/Desktop/output/DRS_Project_Event_based_vision/Generate_Events/Generate_Events_Resized_Data/Non_Flash_Events/positive_events.npy', np.array(positive_events))
# np.save('C:/Users/adcha/Desktop/output/DRS_Project_Event_based_vision/Generate_Events/Generate_Events_Resized_Data/Non_Flash_Events/negative_events.npy', np.array(negative_events))
print(positive_events[:50])
print(negative_events[:50])
print(len(positive_events))
print(len(negative_events))