from src.model import DEFAULT_MODEL_FILE, load_model
import sys
from src.dataset import MP_HANDS, MP_DRAWING, MP_DRAWING_STYLE, HANDS, Collector
import cv2

from src.dataset import ALPHABET_DICT, DEFAULT_DEVICE
from src.dataset.process import process_img
import numpy as np

class Transcripter(Collector):
    def __init__(self, modelfile : str =  DEFAULT_MODEL_FILE, stdout : int = sys.stdout,
                 classes : dict = ALPHABET_DICT, device : int = DEFAULT_DEVICE):
        
        self.model = load_model(modelfile)
        self.model.verbose = 0  # Remove the verbose
        self.device = device
        self.classes = classes
        self.stdout = stdout

    
    def transcript(self):
        self._initialize_device()
        
        prev_label = None
        while True:
            ret, frame = self.cam.read()
            
            H, W, _ = frame.shape
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = HANDS.process(frame_rgb)

            if results.multi_hand_landmarks:
                data, x_min, y_min, x_max, y_max = process_img(results)  # Fetcht the data
                
                prediction = self.model.predict([np.asarray(data).reshape(-1, 84, 1)], verbose = 0)
                prediction_index_label = np.argmax(prediction, axis = 1)[0]
                predicted_label = self.classes[prediction_index_label]
                
                # Wen detectes something different
                if prev_label != predicted_label:
                    print(predicted_label, file = self.stdout, end='')  # Print the transcripted
                    prev_label = predicted_label

                # Mark the detected prediction
                x1 = int(x_min * W) - 10
                y1 = int(y_min * H) - 10
                
                x2 = int(x_max * W) - 10
                y2 = int(y_max * H) - 10

                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 4)
                    
                cv2.putText(frame, predicted_label, (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3,
                            cv2.LINE_AA)

            cv2.imshow('frame', frame)
            
            if cv2.waitKey(25) == ord('q'):  # To quit
                break
        self._shutdown_device()
        
        


