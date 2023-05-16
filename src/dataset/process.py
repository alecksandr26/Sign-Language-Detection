from . import DEFAULT_ARRAY_SIZE

def process_img(results) -> ([float], float, float):
    data = [0.0] * DEFAULT_ARRAY_SIZE  # Allocates a new buffer
    x_aux = []
    y_aux = []
    j = 0                   # A simple iterator for data
    
    # Process the results of the hand
    for hand_landmarks in results.multi_hand_landmarks:
        landmark = hand_landmarks.landmark  # Get the list of landmarks
    
        # Dump the landmarks to the  data_aux
        for i in range(len(landmark)):
            # Catch just the x and y coordinates
            x = landmark[i].x
            y = landmark[i].y
                
            x_aux.append(x)
            y_aux.append(y)

        x_min = min(x_aux)
        y_min = min(y_aux)
        x_max = max(x_aux)
        y_max = max(y_aux)

        for i in range(len(landmark)):
            x = landmark[i].x
            y = landmark[i].y

            data[j] = x - x_min
            j += 1
            data[j] = y - y_min
            j += 1
        
        
    return (data, x_min, y_min, x_max, y_max)
