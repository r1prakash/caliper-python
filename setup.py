#!/usr/bin/env python3


"""
distutils/setuptools install script.
"""

import os
import sys
from codecs import open

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

import caliper

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

_packages = [ 'caliper',
              'caliper.extern',
              'caliper.util',
              'caliper_tests' ]
    
_requires = [ 'future >= 0.14.3',
              'oauthlib >= 0.7.2',
              'requests >= 2.7.0' ]

_fixtures = [ 'fixtures_local/*.json',
              'fixtures_common/src/test/resources/fixtures/*.json' ]

with open('README.rst', 'r', 'utf-8') as f:
          readme = f.read()
with open('HISTORY.rst', 'r', 'utf-8') as f:
          history = f.read()

setup(
    name = caliper.__title__,
    version = caliper.__version__,
    description = 'Caliper API for Python. Provides implementation for the IMS Caliper Sensor API.',
    long_description = readme + '\n\n' + history,
    maintainer = caliper.__author__,
    maintainer_email = 'info@imsglobal.org',
    url = 'https://github.com/IMSGlobal/caliper-python',
    packages = _packages,
    package_data = {'caliper_tests' : _fixtures },
    install_requires = _requires,
    license = caliper.__license__,
    zip_safe = False,
    classifiers = (
        'Development Status :: 3 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4'
    ),
)
