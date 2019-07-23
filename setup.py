from setuptools import setup

with open('README.rst', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setup(name='pyter3',
      version='0.3',
      description='Simple library to evaluate the Translation Edit Rate',
      long_description=long_description,
      long_description_content_type='text/markdown',
      author='Hiroyuki Tanaka, Bram Vanroy',
      author_email='afl0x@gmail.com',
      url='https://github.com/BramVanroy/pyter',
      packages=['pyter'],
      license='MIT',
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
        ]
      )
