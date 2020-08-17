from pathlib import Path
from setuptools import setup


setup(
    name='mainmethod',
    version='0.1.0',
    description='C-Like main method support',
    long_description=(Path(__file__).parent / 'README.md').read_text(),
    long_description_content_type='text/markdown',
    author='Yanky Hoffman',
    author_email='developer.yankyhoffman@gmail.com',
    url='https://github.com/yankyhoffman/mainmethod',
    packages=['mainmethod'],
)
