#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

setup_requirements = ['pytest-runner',]

setup(
    author="Han Zhichao",
    author_email='superhin@126.com',
    description='Pytest plugin for appium',
    long_description='Pytest plugin for appium',
    classifiers=[
        'Framework :: Pytest',
        'Programming Language :: Python',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.7',
    ],
    license="MIT license",
    include_package_data=True,
    keywords=[
        'pytest', 'py.test', 'appium'
    ],
    name='pytest-appium',
    packages=find_packages(include=['pytest_appium']),
    setup_requires=setup_requirements,
    url='https://github.com/hanzhichao/pytest-appium',
    version='0.1',
    zip_safe=True,
    install_requires=[
        'pytest',
        'pytest-runner',
        'Appium-Python-Client',
        'pytest-variables'
    ],
    entry_points={
        'pytest11': [
            'pytest-appium = pytest_appium.plugin',
        ]
    }
)
