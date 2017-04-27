import compileall
import os

from contextlib import contextmanager

# pylint: disable=import-error,no-name-in-module
from distutils.core import setup
from distutils.command.build_ext import build_ext
# pylint: enable=import-error,no-name-in-module
from setuptools import find_packages, Extension

requirements = []

if __name__ == '__main__':
    setup(
        name='bulgarian_stemmer',
        version='0.1.0',
        #author='Rafael Perez',
        #author_email='hdkmraf@gmail.com',
        packages=find_packages(exclude=['tests']),
        #url='',
        #license='',
        #description='Intellica core functions',
        #install_requires=requirements,
    )
