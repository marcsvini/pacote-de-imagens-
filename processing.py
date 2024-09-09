from PIL import Image
import cv2
import numpy as np

def resize_image(image, width, height):
    return image.resize((width, height))

def convert_to_grayscale(image):
    return image.convert('L')
