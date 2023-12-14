import pytz
from datetime import datetime
import numpy as np
import cv2


time_zone = pytz.timezone("Europe/Moscow")
mp4_name = datetime.now(time_zone)

def make_words_move(some_words: str) -> None:
    """takes a string and creates a .mp4 ticker using cv2 
        :some_words: text for convert
        :type some_words: str
    """
    width, height = 100, 100 #Оutput file resolution size
    # Set parameters for video
    out = cv2.VideoWriter(
        f"video/{mp4_name}_opencv.mp4", cv2.VideoWriter_fourcc(*'mp4v'), 24,
        (width, height))

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
    for t in range(72):  # 3 sec x 24fps
        frame.fill(0)
        x -= 10  # ticker speed
        cv2.putText(
            frame, some_words, (x, y), font, font_scale, font_color, 
            font_thickness)
        # write the frame
        out.write(frame)
    out.release()

if __name__ == '__main__':
    test_text = "Пример текста! Text example!"
    make_words_move(test_text)