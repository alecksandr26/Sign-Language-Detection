
# Some global variables
DEFAULT_DATA_DIR = "./data"
DEFAULT_AMOUNT_OF_SIGNS = 26    # letters
DATA_SIZE = 1000             # 1000 pictures
DEFAULT_DEVICE = 0

# Create an empty dictionary
ALPHABET_DICT = {}

# Loop through the range of numbers corresponding to the alphabets
for num in range(1, 27):
    # Convert the number to an alphabet using the chr() function
    alphabet = chr(num + 96)  # Add 96 to get the lowercase alphabets (a=97)

    # Add the key-value pair to the dictionary
    ALPHABET_DICT[num] = alphabet

from .collect import Collector



