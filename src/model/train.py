import pickle

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np

# Load the data
data_dict = pickle.load(open('./data.pickle', 'rb'))

# Dump the data into arrays
data = np.asarray(data_dict['data'])
labels = np.asarray(data_dict['labels'])

# Slipt the data data into the tranning data and the testing data
x_train, x_test, y_train, y_test = train_test_split(data, labels, test_size = 0.2,
                                                    shuffle = True, stratify = labels)
# Create the model
model = RandomForestClassifier()

# Fit the model
model.fit(x_train, y_train)

# Test the model
y_predict = model.predict(x_test)

score = accuracy_score(y_predict, y_test)

print('{}% of samples were classified correctly !'.format(score * 100))

# Dump the tranined model
f = open('model.p', 'wb')
pickle.dump({'model': model}, f)
f.close()
