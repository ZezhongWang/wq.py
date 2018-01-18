
import os
from setuptools import setup

import wqpy


def get_subpackages(name):
    """获取该模块下所有的子模块名称"""
    splist = []

    for dirpath, _dirnames, _filenames in os.walk(name):
        if os.path.isfile(os.path.join(dirpath, '__init__.py')):
            splist.append(".".join(dirpath.split(os.sep)))

    return splist


setup(
    name='wqpy',
    version=wqpy.__version__,
    author=wqpy.__author__,
    description='A framework for developing Quantitative Trading programmes',
    long_description = __doc__,
    keywords='quant quantitative investment trading algotrading',
    classifiers=['Development Status :: 4 - Beta',
                 'Operating System :: Microsoft :: Windows :: Windows 7',
                 'Operating System :: Microsoft :: Windows :: Windows 8',
                 'Operating System :: Microsoft :: Windows :: Windows 10',
                 'Operating System :: Microsoft :: Windows :: Windows Server 2008',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.6',
                 'Topic :: Office/Business :: Financial :: Investment',
                 'Programming Language :: Python :: Implementation :: CPython',
                 'License :: OSI Approved :: MIT License'],
    packages=get_subpackages('wqpy'),
    package_data={'': ['*.json', '*.md', '*.ico',
                       '*.h', '*.cpp', '*.bash', '*.txt',
                       '*.dll', '*.lib', '*.so', '*.pyd',
                       '*.dat', '*.ini', '*.pfx', '*.scc', '*.crt', '*.key']},
    extras_require={
        'tq': ["tornado>=4.5.1", "sortedcontainers>=1.5.7"],
    }
)