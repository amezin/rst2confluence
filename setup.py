#!/usr/bin/env python
import os
import shutil
from distutils.core import setup

if not os.path.exists('scripts'):
    os.makedirs('scripts')

shutil.copyfile('rst2confluence.py', 'scripts/rst2confluence')
shutil.copyfile('md2confluence.py', 'scripts/md2confluence')

setup(
    name='rst2confluence',
    version='0.6.0',
    description='reStructuredText-to-Confluence markup converter',

    author='Kenichiro TANAKA',
    author_email='tanaka.kenichiro@gmail.com',

    maintainer='Christian Weiske',
    maintainer_email='christian.weiske@netresearch.de',

    url='https://github.com/netresearch/rst2confluence',

    license='AGPL',

    py_modules=['rst2confluence.confluence'],
    # package_dir={'rst2confluence': 'src/rst2confluence'},
    scripts=['scripts/rst2confluence', 'scripts/md2confluence'],

    install_requires=[
        'docutils',
        'Pygments',
        'recommonmark'
    ]
)
