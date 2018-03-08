from setuptools import setup, find_packages

setup(
    name='window_slider',
    packages=find_packages(exclude=['tests']),
    version='0.4',
    description='A lib to implement sliding window with overlapping on numpy array',
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
