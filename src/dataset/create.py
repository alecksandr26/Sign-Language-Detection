import os
import pickle                   # To put the data into a file

import mediapipe as mp          # Extract the landmarks 
import cv2
import matplotlib.pyplot as plt


# Objects to draw the landmarks over the images
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

hands = mp_hands.Hands(static_image_mode = True, min_detection_confidence = 0.3)
DATA_DIR = './data'

data = []
labels = []
for dir_ in os.listdir(DATA_DIR):  # List the images directories
    # For each image
    for img_path in os.listdir(os.path.join(DATA_DIR, dir_)):  # List the images from the directories
    #for img_path in os.listdir(os.path.join(DATA_DIR, dir_))[:1]:  # List the images from the directories
        data_aux = []
        x_ = []
        y_ = []

        img = cv2.imread(os.path.join(DATA_DIR, dir_, img_path))
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Converts the image into rgb
        
        results = hands.process(img_rgb)  # process and create the finded landmarks

        if results.multi_hand_landmarks:  # Check if a hand is detected
            for hand_landmarks in results.multi_hand_landmarks:
                
                # Dump the landmarks to the  data_aux
                for i in range(len(hand_landmarks.landmark)):
                    # Catch just the x and y coordinates
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y
                    x_.append(x)
                    y_.append(y)

                for i in range(len(hand_landmarks.landmark)):
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y
                    
                    data_aux.append(x - min(x_))
                    data_aux.append(y - min(y_))
                    
                """
                mp_drawing.draw_landmarks(img_rgb, hand_landmarks, mp_hands.HAND_CONNECTIONS,
                                          mp_drawing_styles.get_default_hand_landmarks_style(),
                                          mp_drawing_styles.get_default_hand_connections_style())
                """
                

            data.append(data_aux)  # Catch all the cordinates
            labels.append(dir_)  # Catch directory
            
            # plt.figure()
            # plt.imshow(img_rgb)
        

f = open('data.pickle', 'wb')   # Dump the data
pickle.dump({'data': data, 'labels': labels}, f)  # Dump all the data inorder to create the dataset
f.close()

# plt.show()
