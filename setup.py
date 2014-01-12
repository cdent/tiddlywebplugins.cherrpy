import sys
import os

from setuptools import setup, find_packages

VERSION = '0.1.0'

CLASSIFIERS = """
Environment :: Web Environment
License :: OSI Approved :: BSD License
Operating System :: OS Independent
Programming Language :: Python :: 2.7
Programming Language :: Python :: 3.3
Topic :: Internet :: WWW/HTTP :: WSGI
""".strip().splitlines()


META = {
    'namespace_packages': ['tiddlywebplugins'],
    'name': 'tiddlywebplugins.cherrypy',
    'version': VERSION,
    'description': 'An improved server for TiddlyWeb.',
    'long_description': open(os.path.join(os.path.dirname(__file__), 'README')).read(),
    'author': 'Chris Dent',
    'author_email': 'cdent@peermore.com',
    'url': 'http://pypi.python.org/pypi/tiddlywebplugins.cherrypy',
    'packages': find_packages(exclude=['test']),
    'platforms': 'Posix; MacOS X; Windows',
    'classifiers': CLASSIFIERS,
    'install_requires': ['setuptools',
        'tiddlyweb',
        'CherryPy'
    ],
    'zip_safe': False,
}

if __name__ == '__main__':
    setup(**META)
