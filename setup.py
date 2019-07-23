from setuptools import setup
import os


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name='pyter',
      version='0.3',
      description='Simple library to evaluate the Translation Edit Rate',
      long_description=read('README.rst'),
      author='Hiroyuki Tanaka, Bram Vanroy',
      author_email='aflc0x@gmail.com',
      url='https://github.com/BramVanroy/pyter',
      platforms='any',
      packages=['pyter'],
      classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Information Technology',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Text Processing',
        ],
      )
