import cv2
import os
from scipy.io import loadmat
import numpy as np




main_dir = '/home/shassan/DRS_Project_Event_based_vision/Data_resized_hfd2_MWIR_subclips/Negatives_Noise_Events'

negative_events = []

annots = np.load('negative_list.npy')

first_sub = os.listdir(main_dir)
count = 0
for i in range(len(annots)):
    tmp = annots[i].strip()
    tmp = main_dir+tmp[(tmp.find('Negatives')+9):]
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
                'Negatives_Noise_Events', 'Negatives_Noise_Events_Frames')
            if frame_num == 1:
                negative_events.append(frames_path)
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
np.save('negative_events.npy', np.array(negative_events))
print(negative_events[:50])
print(len(negative_events))
