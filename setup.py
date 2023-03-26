from distutils.core import setup
from Cython.Build import cythonize

setup(
    name='copy_files',
    ext_modules=cythonize('copy_files.py'),
)
