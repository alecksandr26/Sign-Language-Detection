import pickle

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np

from . import DEFAULT_MODEL_FILE, DEFAULT_DATASET_FILE

import pdb                      # For debuggin

class Model:
    def __init__(self, dataset : str = DEFAULT_DATASET_FILE, modelfile = DEFAULT_MODEL_FILE):
        data_dict = pickle.load(open(dataset, 'rb'))
        self.modelfile = modelfile
        self.model = RandomForestClassifier(verbose = 1)
        
        # pdb.set_trace()

        # Labeling the data
        self.data = np.asarray(data_dict['data'])
        self.labels = np.asarray(data_dict['labels'])

    def train(self):
        # Slipt the data data into the tranning data and the testing data
        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(self.data, self.labels,
                                                                                test_size = 0.2,
                                                                                shuffle = True,
                                                                                stratify = self.labels)
        self.model.fit(self.x_train, self.y_train)

    def test(self):
        # Test the model
        y_predict = self.model.predict(self.x_test)
        score = accuracy_score(y_predict, self.y_test)
        
        print('{}% of samples were classified correctly !'.format(score * 100))


    def save(self):
        # Dump the model
        f = open(self.modelfile, "wb")
        pickle.dump({'model': self.model}, f)
        f.close()


# load the model
def load_model(modelfile : str = DEFAULT_MODEL_FILE) -> RandomForestClassifier:
    model_dict = pickle.load(open(modelfile, "rb"))
    return model_dict['model']  # Load the modelxo
    
