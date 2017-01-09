#!/usr/bin/env python

from distutils.core import setup
from os.path import abspath, dirname, join
import re

NAME = 'robotbackgroundlogger'
CLASSIFIERS = """
Development Status :: 5 - Production/Stable
License :: OSI Approved :: Apache Software License
Operating System :: OS Independent
Programming Language :: Python :: 2
Programming Language :: Python :: 3
Topic :: Software Development :: Testing
Framework :: Robot Framework
""".strip().splitlines()
CURDIR = dirname(abspath(__file__))
with open(join(CURDIR, NAME+'.py')) as f:
    VERSION = re.search("\n__version__ = '(.*)'\n", f.read()).group(1)
with open(join(CURDIR, 'README.rst')) as f:
    README = f.read()

setup(
    name             = NAME,
    version          = VERSION,
    author           = 'Robot Framework Developers',
    author_email     = 'robotframework@gmail.com',
    url              = 'https://github.com/robotframework/robotbackgroundlogger',
    download_url     = 'https://pypi.python.org/pypi/robotbackgroundlogger',
    license          = 'Apache License 2.0',
    description      = 'A helper module for logging to Robot Framework log '
                       'from background threads.',
    long_description = README,
    keywords         = 'robotframework testing testautomation atdd',
    platforms        = 'any',
    classifiers      = CLASSIFIERS,
    py_modules       = ['robotbackgroundlogger'],
    install_requires = ['robotframework']
)
