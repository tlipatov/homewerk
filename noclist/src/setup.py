from setuptools import setup, find_packages

with open('requirements.txt') as f:
  required = [line for line in f.read().splitlines()
    if not line.startswith("#")]

setup(
  name="badsec",
  version="0.0.1",
  packages=find_packages(),
  author="DaMan",
  author_email="DaMan",
  description="BadSec",
  license="",
  keywords="badsec",
  url="http://da.man",
  install_requires=required,
  entry_points={
      'console_scripts': [
          'badsec = badsec.main:main'
      ]
  },
  zip_safe=False,
  include_package_data=True,
)
