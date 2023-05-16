import os
import pickle                   # To put the data into a file

import cv2
import matplotlib.pyplot as plt

# For the progress bar
from tqdm import tqdm

from . import *
from .process import process_img

class DataSetCreate:
    def __init__(self, directory : str = DEFAULT_DATA_DIR, filename : str = DEFAULT_DATASET_FILE):
        self.directory = directory
        self.filename = filename
        self.data = []
        self.labels = []

                
    def save(self, savefilename : str = ""):
        if savefilename == "":
            savefilename = self.filename
        
        dataset_file = open(savefilename, "wb")
        pickle.dump(
            {
                "data" : self.data,
                "labels" : self.labels
            },
            dataset_file
        )

        dataset_file.close()

    def build(self):
        # Iterate each image from each directory
        for d in os.listdir(self.directory):
            for img_path in tqdm(os.listdir(os.path.join(self.directory, d)),
                                 desc = f"Processing images for {d}"):
                img = cv2.imread(os.path.join(self.directory, d, img_path))
                img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Converts the image into rgb
        
                results = HANDS.process(img_rgb)  # process and create the finded landmarks

                if results.multi_hand_landmarks:  # Check if a hand is detected
                    data_tuple = process_img(results)  # Process the image
                    
                    self.data.append(data_tuple[0])  # Catch all the cordinates
                    self.labels.append(d)  # Catch directory
                    
            

        
