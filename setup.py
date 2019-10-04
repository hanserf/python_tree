# import os
from setuptools import setup, find_packages

setup(
    name='pytree',
    version='0.0.1',
    description='Lists folders and files as a tree',
    author='hansef',
    author_email='hans.erik.fjeld@embida.no',
    packages=find_packages(),
    setup_requires=['wheel'],
    install_requires=['termcolor'],
    entry_points={
        'console_scripts': [
            'pytree=pytree.main:main'
        ],
    }
)
