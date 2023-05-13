import os
from matplotlib import pyplot as plt
import tensorflow as tf 
import tensorflow_io as tfio

# Import the model for training
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, Dense, Flatten

# Catch the path of the direcotries of the data
DIR_CAPUCHIN = os.path.join('data', 'Parsed_Capuchinbird_Clips')
DIR_NO_CAPUCHIN = os.path.join('data', 'Parsed_Not_Capuchinbird_Clips')


# load_wav_16k_mono: To pass from 44100Hz to 16000hz audio signal
def load_wav_16k_mono(filename):
    file_contents = tf.io.read_file(filename)
    wav, sample_rate = tf.audio.decode_wav(file_contents, desired_channels=1)
    wav = tf.squeeze(wav, axis=-1)
    sample_rate = tf.cast(sample_rate, dtype=tf.int64)
    wav = tfio.audio.resample(wav, rate_in=sample_rate, rate_out=16000)
    return wav

# preprocess: To preprocess and gets the spectrogram of each audio file
def preprocess(file_path, label): 
    wav = load_wav_16k_mono(file_path)
    wav = wav[:48000]
    zero_padding = tf.zeros([48000] - tf.shape(wav), dtype=tf.float32)
    wav = tf.concat([zero_padding, wav],0)
    spectrogram = tf.signal.stft(wav, frame_length=320, frame_step=32)
    spectrogram = tf.abs(spectrogram)
    spectrogram = tf.expand_dims(spectrogram, axis=2)
    return spectrogram, label

# To plot the efficiency of the model
def plot_the_efficiency_model():
    pass


def main():
    # Create the dataframes
    ds_capuchin = tf.data.Dataset.list_files(DIR_CAPUCHIN + '/*.wav')
    ds_no_capuchin = tf.data.Dataset.list_files(DIR_NO_CAPUCHIN + '/*.wav')

    # Add the labels
    positives = tf.data.Dataset.zip((ds_capuchin, tf.data.Dataset.from_tensor_slices(tf.ones(len(ds_capuchin)))))
    negatives = tf.data.Dataset.zip((ds_no_capuchin, tf.data.Dataset.from_tensor_slices(tf.zeros(len(ds_no_capuchin)))))

    # Combine the data for the training
    ds = positives.concatenate(negatives)

    # print(positives.as_numpy_iterator().next())
    
    # Create Training and Testing Partitions

    # Map the preprocess function to have the label
    ds = ds.map(preprocess)
    ds = ds.cache()
    ds = ds.shuffle(buffer_size = 1000)  # Shuffle  the data
    ds = ds.batch(16)           # Train each 16 samples
    ds = ds.prefetch(8)         # Overlaps the preprocessing and model execution of a training step

    # Split into testing and training partions
    train = ds.take(36)       # for training
    test = ds.skip(36).take(15) # for testing the model

    # Create the AI model 
    model = Sequential()
    model.add(Conv2D(16, (3, 3), activation = 'relu', input_shape = (1491, 257, 1)))  #  Add the first layer
    model.add(Conv2D(16, (3, 3), activation = 'relu'))  # Add the second layer
    model.add(Flatten())                                # Add the flatter layer to be one dimension
    model.add(Dense(128, activation = 'relu'))          # Add fourth layer with an output of 128 units
    model.add(Dense(1, activation = 'sigmoid'))         # Add the last layer with the binary output

    # Compile the model using the Adam optimizer
    model.compile('Adam', loss = 'BinaryCrossentropy',
                  metrics = [tf.keras.metrics.Recall(), tf.keras.metrics.Precision()])

    # fetch some data of the model 
    model.summary()

    # Train the model
    histogram = model.fit(train, epochs = 4, validation_data = test)

    

    
    

    
    





if __name__ == "__main__":
    main()
