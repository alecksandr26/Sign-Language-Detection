# Table of Contents
* [Description](https://github.com/RaudelCasas1603/Monky-Detection-#sign-language-detection)
* [How to install it?](https://github.com/RaudelCasas1603/Monky-Detection-#how-to-install-it)
* [How to train it?](https://github.com/RaudelCasas1603/Monky-Detection-#how-to-train-it)
   * [To collect your own data](https://github.com/RaudelCasas1603/Monky-Detection-#to-collect-your-own-data)
   * [To build your own dataset](https://github.com/RaudelCasas1603/Monky-Detection-#to-build-your-own-dataset)
* [Examples](https://github.com/RaudelCasas1603/Monky-Detection-#Examples)
   * [Video example](https://github.com/RaudelCasas1603/Monky-Detection-#video-example) 
* [References](https://github.com/RaudelCasas1603/Monky-Detection-#references)

# Sign Language Detection
The Sign Language Gesture Recognition project utilizes Python, [OpenCV](https://github.com/opencv/opencv-python), and the powerful Random Forest algorithm. It captures and preprocesses video frames, extracting hand landmarks using [Mediapipe](https://github.com/google/mediapipe). These landmarks are then used as input for the an small nerual network, trained on a labeled dataset of sign language gestures. The neural network learns patterns and correlations between landmarks and gestures, enabling accurate real-time recognition.

# How to install it?
To install Sign Language Detection application, follow these steps:
1. Clone the repository to your local machine:
   ```shell
   git clone https://github.com/RaudelCasas1603/Monky-Detection-.git
   ```
2. Navigate to the project directory:
   ```shell
   cd Monky-Detection-
   ```
3. Create a virtual environment (optional but recommended):
   ```shell
   python3 -m venv env
   ```
4. Activate the virtual environment:
   * On macOS and Linux:
     ```shell
     source env/bin/activate
     ```
   * On Windows:
      ```shell
      .\env\Scripts\activate
      ```
5. Install the package program:
   ```shell
   pip install .
   ```
That's it! You have now successfully installed the Sign Language Detection application.
# How to train it?
## To collect your own data.
You can create your collection of data, firstly make sure that you already have installed the program in your
python environment, then follow the next steps:
1. Open your terminal or command prompt.
2. Navigate to the directory where your eviroment is located. For example:
   ```shell
   cd  /path/to/your/env/sld
   ```
3. Activate the virtual environment if you have created one (optional):
   ```shell
   source env/bin/activate  # On macOS and Linux
   .\env\Scripts\activate  # On Windows
   ```
4. Run the command with the **collect-data** command and specify the desired arguments:
   ```shell
    sld collect-data -n 100 -d directory-to-store-data/ -s signs.json
   ```
   * The **-n 100** flag is optional and specifies that you want to generate 100 pictures per class or sign. By default, the program is programmed to take at least 1000 pictures.
   * The **-d directory-to-store-data/** flag is optional and sets the directory where the collected data will be stored. Replace directory-to-store-data/ with the actual directory path. If the directory doesn't exist, it will be created. By default, it uses the data/ directory.
   * The **-s signs.json** flag is optional and specifies a JSON file with each sign to classify. By default, it uses the American alphabet for sign classification. Use this flag if you want to perform a custom sign classification.
   
5. The command will start collecting the data based on the provided arguments. It will generate pictures for each class and store them in the specified folder.

6. Once the data collection is completed, you will see the message **"Data collection completed."** printed in the terminal.

That's it! You have successfully created a data collection using the collect-data command. Adjust the arguments as needed to customize your data collection process.
## To build your own dataset.
Firstly make sure that you have collected your data, then to build your own dataset just follow the next steps:
1. Open your terminal or command prompt.
2. Navigate to the directory where your environment is located. For example:
   ```shell
   cd /path/to/your/env/sld
   ```
3. Activate the virtual environment if you have created one (optional):
   ```shell
   source env/bin/activate  # On macOS and Linux
   .\env\Scripts\activate  # On Windows
   ```
4. Run the command with the **build-dataset** command and specify the desired arguments:
   ```shell
   sld build-dataset -f dataset.pickle -d data/
   ```
   * **-f dataset.pickle** specifies the output filename of the built dataset. Replace dataset.pickle with the **desired filename**. By default, **data.pickle** is the output dataset filename.
   * **-d data/** sets the directory where the raw data is stored. Replace **data/** with the actual directory. By default, the raw data is stored in the data/ directory.
5. The command will start building the dataset based on the provided arguments. It will process the images from the specified data directory and generate the dataset file.
6. Once the dataset is built, you will see the message **"Dataset built."** printed in the terminal.

## Download our own dataset.
blah blah not avaiable yet >:|

# Examples
## Video example   
working ont eh new video

# References
* Computer vision engineer. (2023, January 26). Sign language detection with Python and Scikit Learn | Landmark detection | Computer vision tutorial [Video]. YouTube. https://www.youtube.com/watch?v=MJCSjXepaAM
* Normalized Nerd. (2021, January 13). Decision Tree Classification Clearly Explained! [Video]. YouTube. https://www.youtube.com/watch?v=ZVR2Way4nwQ
* Normalized Nerd. (2021b, April 21). Random Forest Algorithm Clearly Explained! [Video]. YouTube. https://www.youtube.com/watch?v=v6VJ2RO66A
* Gutta, S. (2022, January 6). Folder Structure for Machine Learning Projects | by Surya Gutta  | Analytics Vidhya. Medium. https://medium.com/analytics-vidhya/folder-structure-for-machine-learning-projects-a7e451a8caaa

* https://www.tensorflow.org/tutorials/images/cnn
* https://stackoverflow.com/questions/40273109/convert-python-opencv-mat-image-to-tensorflow-image-data


