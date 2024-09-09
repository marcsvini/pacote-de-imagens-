from setuptools import setup, find_packages

setup(
    name='image_processor',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Pillow',
        'opencv-python'
    ],
    description='A package for basic image processing tasks',
    author='Seu Nome',
    author_email='seuemail@example.com',
)
