import cv2
import os
from scipy.io import loadmat
import numpy as np

main_dir = '/home/shassan/DRS_Project_Event_based_vision/Data_resized_hfd2_MWIR_subclips/Positives_Flash_Noise_Events'

positive_events = []

annots = loadmat('positive_list.mat')
annots = annots['a']

first_sub = os.listdir(main_dir)
count = 0
for i in range(len(annots)):
    tmp = annots[i].strip()
    tmp = main_dir+tmp[(tmp.find('positive')+8):]
    clip = tmp
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
                'Positives_Flash_Noise_Events', 'Positives_Flash_Noise_Events_Frames')
            if frame_num == 1:
                positive_events.append(frames_path)
            if not os.path.exists(frames_path):
                os.makedirs(frames_path)

            cv2.imwrite(frames_path + str(frame_num) + '.png', frame)
        except:
            #print('except')
            break
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    vid.release()
    cv2.destroyAllWindows()

print(count)
np.save('positive_events.npy', np.array(positive_events))
print(positive_events[:50])
print(len(positive_events))
