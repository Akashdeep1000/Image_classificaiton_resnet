import pandas as pd
import os


positive_folders = []

parent_folder = "C:\\Users\\adcha\\Desktop\\output\\DRS_Project_Event_based_vision\\Generate_Events\\Generate_Events_Resized_Data\\Non_Flash_Events\\Negatives"

for folder1 in os.listdir(parent_folder):

    path_folder1 = os.path.join(parent_folder,folder1)

    for folder2 in os.listdir(path_folder1):

        path_folder2 = os.path.join(path_folder1,folder2)

        for folder3 in os.listdir(path_folder2):

            path_folder3 = os.path.join(path_folder2,folder3)

            for folder4 in os.listdir(path_folder3):

                path_folder4 = os.path.join(path_folder3,folder4)

                positive_folders.append(path_folder4)


df = pd.DataFrame(positive_folders)

df.to_csv("C:\\Users\\adcha\\Desktop\\negative_files.csv")

