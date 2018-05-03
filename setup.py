#!/usr/bin/env python

from distutils.core import setup

import spc

setup(name='spc-spectra',
      version=spc.__version__,
      description=spc.__doc__,
      author=spc.__author__,
      author_email=spc.__author_email__,
      url='https://github.com/NickMacro/spc-spectra',
      download_url='https://github.com/NickMacro/spc-spectra/archive/0.4.0.tar.gz',
      packages=['spc-spectra'],
      classifiers=[],
      )
