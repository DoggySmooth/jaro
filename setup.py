#!/usr/bin/env python

from setuptools import find_packages, setup

setup(
    packages=find_packages(),
    entry_points={
        'console_scripts': ['jaro = jaro.script.console:main']
    }
)
