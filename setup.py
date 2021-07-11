# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='pubsub',
    version='0.1.2',
    description='Simple Python PubSub',
    long_description='Python In-Process messaging, with filtering by topic.',
    author='Zhen Wang',
    author_email='mail@zhenwang.info',
    license='MIT',
    url='https://github.com/nehz/pubsub',
    py_modules=['pubsub'],
    install_requires=[
        'six >= 1, < 2',
    ],
)
