import pytz
from datetime import datetime
import numpy as np
import cv2


time_zone = pytz.timezone("Europe/Moscow")
# mp4_name = f"{datetime.now(time_zone)}_opencv.mp4"

def make_words_move(some_words: str) :
    """takes a string and creates a .mp4 ticker using cv2 
        :some_words: text for convert
        :type some_words: str
    """
    width, height = 100, 100 #Оutput file resolution size
    # Set parameters for video
    mp4_name = f"{datetime.now(time_zone)}_opencv.mp4"
    framerate = int(len(some_words) // 1.1)
    print(framerate)
    out = cv2.VideoWriter(
        f"video/{mp4_name}", 
        cv2.VideoWriter_fourcc(*'mp4v'), framerate, # type: ignore
        (width, height))
    print(mp4_name)

    # Create black background
    frame = np.zeros((height, width, 3), dtype=np.uint8)    

    # Starting coordinates for the ticker
    x, y = width, height // 2

    # Setting font parameters
    font = cv2.FONT_HERSHEY_COMPLEX
    font_scale = 1
    font_thickness = 2
    font_color = (255, 255, 255)  # White text color

    # Creating every frame
    for t in range(framerate * 3):  # 3 sec x 24fps
        frame.fill(0)
        x -= 10  # ticker speed
        cv2.putText(
            frame, some_words, (x, y), font, font_scale, font_color, 
            font_thickness)
        # write the frame
        out.write(frame)
    out.release()
    
    return mp4_name

if __name__ == '__main__':
    test_text = "Пример текста!Пример текста!Пример текста!Пример текста!Пример текста!Пример текста!"
    make_words_move(test_text)