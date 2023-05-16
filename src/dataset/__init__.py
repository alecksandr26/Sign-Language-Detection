
import mediapipe as mp          # To get the hand landmarks 

# Some global variables
DEFAULT_DATA_DIR = "./data"
DEFAULT_DATASET_FILE = "data.pickle"
DEFAULT_AMOUNT_OF_SIGNS = 26    # letters
DATA_SIZE = 1000             # 1000 pictures
DEFAULT_DEVICE = 0

# Create an empty dictionary
ALPHABET_DICT = {}

# Loop through the range of numbers corresponding to the alphabets
for num in range(26):
    # Convert the number to an alphabet using the chr() function
    alphabet = chr(num + 97)  # Add 97 to get the lowercase alphabets (a=97)

    # Add the key-value pair to the dictionary
    ALPHABET_DICT[num] = alphabet

# Objects to draw the landmarks over the images
MP_HANDS = mp.solutions.hands
MP_DRAWING = mp.solutions.drawing_utils
MP_DRAWING_STYLE = mp.solutions.drawing_styles
HANDS = MP_HANDS.Hands(static_image_mode = True, min_detection_confidence = 0.3)

from .collect import Collector
from .create import DataSet
