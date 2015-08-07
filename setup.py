#!/usr/bin/env python
from setuptools import setup

setup(
    name='erajp',
    version='0.0.4',
    description='Convert datetime to Japanese era',
    author='kasajei',
    author_email='kasajei@me.com',
    url='https://github.com/recruit-mtl/erajp',
    packages=['erajp'],
    install_requires=[
        'six>=1.9.0'
    ],
    extras_require={
        "test": ['nose', 'coverage']
    }
)
