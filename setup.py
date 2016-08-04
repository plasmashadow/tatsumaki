# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='tatsumaki',
    version='1.0.0',
    description='Async orm for mongodß',
    long_description=readme,
    author='plasmashadow',
    author_email='plasmashadowx@gmail.com',
    url='https://github.com/plasmashadow/tatsumaki',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=['schematics', 'motor'],
    test_requires=['nose', 'nose-cov']
)
