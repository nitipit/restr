#!/usr/bin/env python

from distutils.core import setup
import os

data = list()
for d in os.walk('restr/'):
    if len(d[2]) > 0:
        path_list = map(
            lambda x: str.join('/', os.path.join(d[0], x).split('/')[1:]),
            d[2]
        )
        data.extend(path_list)

setup(
    # Metadata
    name="Restr",
    version='0.1.4',
    author="Nitipit Nontasuwan",
    author_email="nitipit@gmail.com",
    url="http://nitipit.github.com/restr/",
    license="MIT",
    description="Restructured Text editor for Gnome",
    platforms=['linux'],
    keywords=['editor', 'restructured text', 'rst'],

    # Setup config
    packages=['restr'],
    package_dir={'restr': 'restr'},
    package_data={'restr': data},
    scripts=['restr/restr'],
    install_requires=['docutils', 'appkit>=0.2.8', ]
)
