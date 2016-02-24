#!/usr/bin/env python
from setuptools import setup

version = '1.4.1'

setup(
    name='legacy',
    version=version,
    url='https://github.com/evanburchard/legacy',
    description='Legacy',
    long_description=open('README.rst').read() + "\n\n" + open('CHANGES.rst').read(),
    license='MIT license',
    requires=['django (>= 1.2)'],
    packages=['widget_tweaks', 'widget_tweaks.templatetags'],

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
