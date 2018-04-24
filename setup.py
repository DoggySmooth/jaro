#!/usr/bin/env python

from setuptools import find_packages, setup

setup(
    packages=find_packages(),
    scripts=[
    
	'bin/plimc',
	'bin/xmllint',
	'bin/jsonlint',
	'bin/xml2json.py

    ]
)
