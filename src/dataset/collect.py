import os
import shutil
import cv2

# For the progress bar
from tqdm import tqdm

# Import the constatns
from . import *

class Collector:
    def __init__(self, directory : str = DEFAULT_DATA_DIR, amount_classes : int = DEFAULT_AMOUNT_OF_SIGNS,
                 amount_pics : int = DATA_SIZE, device : int = DEFAULT_DEVICE, classes : dict = ALPHABET_DICT):
        self.directory = directory
        self.amount_classes = amount_classes
        self.amount_pics = amount_pics
        self.device = device
        self.classes = classes

    def _create_directory(self, directory : str):
        if not os.path.exists(os.path.join(directory)):
            os.makedirs(os.path.join(directory))

    def _initialize_device(self):
        self.cam = cv2.VideoCapture(self.device)

    def _shutdown_device(self):
        self.cam.release()
        cv2.destroyAllWindows()

    def start(self):
        self._initialize_device()
        self._create_directory(self.directory)
        for i in tqdm(range(self.amount_classes), desc = "Collecting data"):
            directory = os.path.join(self.directory, self.classes[i])
            tqdm.write('Ready to collect data for sign {} in {}'.format(self.classes[i], directory))
            self._create_directory(directory)  # Create the directory
            
            done = False
            while True:
                ret, frame = self.cam.read()
                line1 = "Ready? To collect the sign:"
                line2 = f"\"{self.classes[i]}\""
                line3 = "Press \"ENTER\" to start!"

                # Determine the position for each line
                x = 100
                y = 50
                line_spacing = 30

                # Display each line separately
                cv2.putText(frame,
                            line1,
                            (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.60, (0, 255, 0), 2,
                            cv2.LINE_AA)
                cv2.putText(frame,
                            line2,
                            (x, y + line_spacing), cv2.FONT_HERSHEY_SIMPLEX, 0.60, (0, 255, 0), 2,
                            cv2.LINE_AA)
                cv2.putText(frame,
                            line3,
                            (x, y + 2 * line_spacing), cv2.FONT_HERSHEY_SIMPLEX, 0.60, (0, 255, 0), 2,
                            cv2.LINE_AA)

                
                cv2.imshow('frame', frame)
                # wait to the user be ready
                if cv2.waitKey(25) == 13:  # 13 = jump line \n = Enter key
                    break
                

            # Start taking a lot of picutres
            for c in tqdm(range(self.amount_pics), leave = False,
                          desc = "Collecting data for sign {} in {}".format(self.classes[i], directory)):
                ret, frame = self.cam.read()
                cv2.imshow('frame', frame)
                cv2.waitKey(25)
                cv2.imwrite(os.path.join(self.directory, str(self.classes[i]), '{}.jpg'.format(c)), frame)
            tqdm.write('Data for sign {} in {}. Collected!'.format(self.classes[i], directory))
                
        self._shutdown_device()
        
    def del_data(self):
        # Deletes all the collected data just for testing
        shutil.rmtree(self.directory)


    def zip_data(self):
        # Compress the data
        pass
    

   


