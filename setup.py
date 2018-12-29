import pathlib
from os import path

from setuptools import setup, find_packages

ROOT_DIR = pathlib.Path(__file__).parent
README = (ROOT_DIR / "README.md").read_text()


def read_file(filename):
    with open(path.join(path.dirname(__file__), filename)) as file:
        return file.read()


setup(
    name='window_slider',
    packages=find_packages(exclude=['tests']),
    version='0.8',
    description='A lib to implement sliding window with overlapping on numpy array',
    long_description=README,
    long_description_content_type="text/markdown",
    author='Ravi Sharma',
    author_email='ravi.sharma.cs11@gmail.com',
    url='https://github.com/imravishar/sliding_window',
    keywords=['window', 'sliding', 'overlap', 'slider'],
    license='Apache2',
    classifiers=[
        'Environment :: Console',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ]
)
