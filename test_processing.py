import unittest
from image_processor import resize_image, convert_to_grayscale, save_image, load_image
from PIL import Image

class TestImageProcessor(unittest.TestCase):
    def setUp(self):
        self.image = Image.new('RGB', (100, 100), color='red')
        self.grayscale_image = convert_to_grayscale(self.image)

    def test_resize_image(self):
        resized_image = resize_image(self.image, 50, 50)
        self.assertEqual(resized_image.size, (50, 50))

    def test_convert_to_grayscale(self):
        self.assertEqual(self.grayscale_image.mode, 'L')

    def test_save_and_load_image(self):
        save_image(self.image, 'test_image.png')
        loaded_image = load_image('test_image.png')
        self.assertEqual(self.image.size, loaded_image.size)

if __name__ == '__main__':
    unittest.main()
