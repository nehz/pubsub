# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='pubsub',
    version='0.1.2',
    description='Simple Python PubSub',
    author='Zhen Wang',
    author_email='mail@zhenwang.info',
    url='https://github.com/nehz/pubsub',
    py_modules=['pubsub'],
    install_requires=[
        'six >= 1, < 2',
    ],
)
