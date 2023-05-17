import pickle

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Include the nerual net
import tensorflow as tf
from tensorflow.keras import datasets, layers, models

import numpy as np

from . import DEFAULT_MODEL_FILE, DEFAULT_DATASET_FILE
from collections import Counter

import pdb                      # For debuggin

# Maps each label to a single number with this we can perfeclty map outputs
def build_map_label(lst):
    dic = {}
    index_number = 0
    for item in lst:
        if item not in dic:
            dic[item] = index_number
            index_number += 1
    return dic



class Model:
    def __init__(self, dataset : str = DEFAULT_DATASET_FILE, modelfile = DEFAULT_MODEL_FILE):
        data_dict = pickle.load(open(dataset, 'rb'))
        self.modelfile = modelfile
        
        # pdb.set_trace()
        
        # Get the amount of neuros that should have the output layer
        labels = np.asarray(data_dict['labels'])
        self.labels_map = build_map_label(labels)
        n_output_neurons = len(self.labels_map)

        # Build the output data
        labels_output = []
        for label in labels:
            labels_output.append(self.labels_map[label])
            
        # Reshape data to have the input shape (84, 1)
        self.data = np.asarray(data_dict['data']).reshape(-1, 84, 1)
        self.data_output = np.asarray(labels_output)

        # Create the CNN model
        self.model = models.Sequential()
        self.model.add(layers.Flatten(input_shape = (84, 1))) # Input layer
        
        self.model.add(layers.Dense(84, activation = 'relu'))  
        self.model.add(layers.Dense(n_output_neurons * 3, activation = "relu"))
        self.model.add(layers.Dense(n_output_neurons * 2, activation = "relu"))
        
        self.model.add(layers.Dense(n_output_neurons, activation = "softmax"))  # Output layer

        # The model should return [1.0, 0.0, ..., 0.0]  depending on the label

    def train(self):
        # Optimze with adam and loss sparce categorlical crossentropy
        self.model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
        self.model.summary()    # Print the model summary

        self.x_train, self.x_test, self.y_train, self.y_test = \
            train_test_split(self.data, self.data_output, shuffle = True, test_size = 0.3)

        self.model.fit(self.x_train, self.y_train, epochs = 20, batch_size = 32)

    def test(self):
        # pdb.set_trace()
        y_predict = np.argmax(self.model.predict(self.x_test), axis = 1)
        score = accuracy_score(y_predict, self.y_test)
        
        print('{}% of samples were classified correctly !'.format(score * 100))


    def save(self):
        # Dump the model
        f = open(self.modelfile, "wb")
        pickle.dump({'model': self.model}, f)
        f.close()


# load the model
def load_model(modelfile : str = DEFAULT_MODEL_FILE):
    model_dict = pickle.load(open(modelfile, "rb"))
    return model_dict['model']  # Load the modelxo
    
