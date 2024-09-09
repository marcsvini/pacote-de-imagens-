from PIL import Image

def save_image(image, path):
    image.save(path)

def load_image(path):
    return Image.open(path)
