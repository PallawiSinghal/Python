
import cv2
import numpy as np
from PIL import Image


if __name__ == '__main__':
    foreground_path = "/1.png"
    background_path = "/back.png"
    back = Image.open(background_path).convert("RGBA")
    front = Image.open(foreground_path).convert("RGBA")
    mask = Image.new('L', front.size, 255)
    mask.show()
    front = front.rotate(10, expand=True)
    mask = mask.rotate(10, expand=True)
    back.paste(front, (100,100), mask)
    back.save("image.png")
 
