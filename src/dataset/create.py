import os
import pickle                   # To put the data into a file

import mediapipe as mp          # Extract the landmarks 
import cv2
import matplotlib.pyplot as plt

from . import *


class DataSet:
    def __init__(self, directory : str = DEFAULT_DATA_DIR, filename : str = DEFAULT_DATASET_FILE):
        self.directory = directory
        self.filename = filename
        self.data = []
        self.labels = []

    def _process(self, results, data_aux : [int]):
        x_aux = []
        y_aux = []
        
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
                    
                data_aux.append(x - x_m)
                data_aux.append(y - y_m)
                
    def _dump(self):
        dataset_file = open(self.filename, "wb")
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
            for img_path in os.listdir(os.path.join(self.directory, d)):
                img = cv2.imread(os.path.join(self.directory, d, img_path))
                img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Converts the image into rgb
        
                results = HANDS.process(img_rgb)  # process and create the finded landmarks

                if results.multi_hand_landmarks:  # Check if a hand is detected
                    data_aux = []
                    self._process(results, data_aux)
                    
                    self.data.append(data_aux)  # Catch all the cordinates
                    self.labels.append(d)  # Catch directory
        self._dump()
                    
            

        
