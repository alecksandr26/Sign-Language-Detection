import os
import shutil
import cv2


# Import the constatns
from . import *

# TODO: implement a way to the collector to find the data

class Collector:
    def __init__(self, folder = DEFAULT_DATA_DIR, amount_classes = DEFAULT_AMOUNT_OF_SIGNS,
                 amount_pics = DATA_SIZE, device = DEFAULT_DEVICE):
        self.folder = folder
        self.amount_classes = amount_classes
        self.amount_pics = amount_pics
        self.device = device


    def start(self):
        self._initialize_device()
        self._create_directory(self.folder)
        for i in range(self.amount_classes):
            directory = os.path.join(self.folder, ALPHABET_DICT[i])
            print('Collecting data for class {} in {}'.format(ALPHABET_DICT[i], directory))
            self._create_directory(directory)  # Create the directory
            
            done = False
            while True:
                ret, frame = self.cam.read()
                cv2.putText(frame,
                            f"Ready? To collect the letter \"{ALPHABET_DICT[i]}\", Press \"q\" to start ! :)",
                            (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.60, (0, 255, 0), 2,
                            cv2.LINE_AA)
                
                cv2.imshow('frame', frame)
                # wait to the user be ready
                if cv2.waitKey(25) == ord('q'):
                    break
                

            # Start taking a lot of picutres
            c = 0
            while c < self.amount_pics:
                ret, frame = self.cam.read()
                cv2.imshow('frame', frame)
                cv2.waitKey(25)
                cv2.imwrite(os.path.join(self.folder, str(ALPHABET_DICT[i]), '{}.jpg'.format(c)), frame)
                c += 1
                
        self._shutdown_device()
        
    def del_data(self):
        # Deletes all the collected data
        shutil.rmtree(self.folder)

    def _create_directory(self, directory):
        if not os.path.exists(os.path.join(directory)):
            os.makedirs(os.path.join(directory))

    def _initialize_device(self):
        self.cam = cv2.VideoCapture(self.device)

    def _shutdown_device(self):
        self.cam.release()
        cv2.destroyAllWindows()


