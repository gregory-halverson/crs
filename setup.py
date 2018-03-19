from os.path import join
from os.path import abspath
from os.path import dirname
from distutils.core import setup

__author__ = 'Gregory Halverson'

NAME = 'crs'
EMAIL = 'gregory.halverson@gmail.com'
URL = 'http://github.com/gregory-halverson/crs'

with open(join(abspath(dirname(__file__)), NAME, 'version.txt')) as f:
    __version__ = f.read()

setup(
    name=NAME,
    version=__version__,
    description="Geographic Coordinate Reference System Encapsulation and Conversion",
    author=__author__,
    author_email=EMAIL,
    url=URL,
    packages=['crs']
)