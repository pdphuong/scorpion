#!/usr/bin/env python
try:
    from setuptools import setup, find_packages
except ImportError:
    import ez_setup
    ez_setup.use_setuptools()
from setuptools import setup, find_packages
import scorpion

setup(name="scorpion",
      version=scorpion.__version__,
      description="scorpion",
      license="MIT",
      author="Eugene Wu",
      author_email="eugenewu@mit.edu",
      url="http://github.com/sirrice/scorpion",
      include_package_data = True,      
      packages = find_packages(),
      package_dir = {'scorpion' : 'scorpion'},
      #scripts = ['scorpion/server.py'],
      package_data = {
        'scorpion': [
          'jars/*'
        ]
      },
      install_requires = [
        'flask', 'psycopg2', 'sqlalchemy', 
        'orange', 'numpy', 'scipy', 'sklearn',
        'matplotlib', 'bsddb', 'pyparsing', 
        'monetdb', 'pymongo', 'rtree'
      ],
      keywords= "")