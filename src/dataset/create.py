import os
import pickle                   # To put the data into a file

import cv2
import matplotlib.pyplot as plt

# For the progress bar
from tqdm import tqdm

from . import *

class DataSetCreate:
    def __init__(self, directory : str = DEFAULT_DATA_DIR, filename : str = DEFAULT_DATASET_FILE):
        self.directory = directory
        self.filename = filename
        self.data = []
        self.labels = []

    def _process(self, results, data_aux : [int]):
        x_aux = []
        y_aux = []
        j = 0                   # A simple iterator
        
        # Process the results of the hand
        for hand_landmarks in results.multi_hand_landmarks:
            landmark = hand_landmarks.landmark  # Get the list of landmarks
            
            # Dump the landmarks to the  data_aux
            for i in range(len(landmark)):
                # Catch just the x and y coordinates
                x = landmark[i].x
                y = landmark[i].y
                
                x_aux.append(x)
                y_aux.append(y)

            x_m = min(x_aux)
            y_m = min(y_aux)

            for i in range(len(landmark)):
                x = landmark[i].x
                y = landmark[i].y

                data_aux[j] = x - x_m
                j += 1
                data_aux[j] = y - y_m
                j += 1
                
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
                    data_aux = [0.0] * DEFAULT_ARRAY_SIZE  # Create the array with the specific size
                    self._process(results, data_aux)
                    
                    self.data.append(data_aux)  # Catch all the cordinates
                    self.labels.append(d)  # Catch directory
                    
            

        
