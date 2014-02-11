#!/usr/bin/env python
# encoding: utf-8
# --------------------------------------------------------------------------

from setuptools import setup, find_packages
from apslutils import __VERSION__

setup(
    name='apslutils',
    version=__VERSION__,
    author='APSL',
    author_email='info@apsl.net',
    packages=find_packages(),
    license='Apache',
    description='Utilidades varias de APSL',
    long_description=open('README.md').read(),
    install_requires=[
        
    ],
    classifiers=[
        'Development Status :: Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
    include_package_data=True,
    zip_safe=False
)
