import pickle

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Include the nerual net
import tensorflow as tf
from tensorflow.keras import datasets, layers, models

import numpy as np

from . import DEFAULT_MODEL_FILE, DEFAULT_DATASET_FILE

import pdb                      # For debuggin

class Model:
    def __init__(self, dataset : str = DEFAULT_DATASET_FILE, modelfile = DEFAULT_MODEL_FILE):
        data_dict = pickle.load(open(dataset, 'rb'))
        self.modelfile = modelfile
        
        # self.model = RandomForestClassifier(verbose = 1)
        # pdb.set_trace()

        # Fetch the indexes 
        self.labels = np.asarray(data_dict['labels'])
        label_mapping = {
            label: index for index, label in enumerate(self.labels)
        }
        self.label_indices = np.asarray(
            [label_mapping[label] for label in self.labels]
        )

        # Reshape data to have the input shape (84, 1)
        self.data = np.asarray(data_dict['data']).reshape(-1, 84, 1)

        # Create the CNN model
        self.model = models.Sequential()
        self.model.add(layers.Conv1D(32, 3, activation='relu', input_shape=(84, 1)))
        self.model.add(layers.Flatten())
        self.model.add(layers.Dense(len(self.labels), activation='softmax'))

    def train(self):
        # Slipt the data data into the tranning data and the testing data
        """
        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(self.data, self.labels,
                                                                                test_size = 0.2,
                                                                                shuffle = True,
                                                                                stratify = self.labels)
        self.model.fit(self.x_train, self.y_train)
        """
        
        self.model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

        self.x_train, self.x_test, self.y_train, self.y_test = \
            train_test_split(
                self.data, self.label_indices, test_size=0.2, shuffle=True,
                stratify = self.label_indices
        )

        self.model.fit(self.x_train, self.y_train, epochs = 10, batch_size = 32)

    def test(self):
        # Test the model
        # y_predict = self.model.predict(self.x_test)
        self.model.summary()
        y_predict = np.argmax(self.model.predict(self.x_test), axis=1)
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
    
