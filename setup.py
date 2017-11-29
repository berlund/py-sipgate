import os
from setuptools import setup


# Utility function to read the README file, borrowed from
# https://github.com/Innovailable/pysipgate/blob/master/setup.py
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='sipgate',
    version='0.0.1',
    description='A client for the Sipgate REST API',
    long_description=read('README.md'),
    license='MIT',
    packages=['sipgate'],
    author='Lars Engel',
    author_email='lars.engel@gmail.com',
    keywords=['example'],
    url='https://github.com/berlund/sipgate'
)