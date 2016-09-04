from setuptools import setup

setup(
  name='JazzDragon',
  version='0.1',
  py_modules=['jazz_dragon'],
  install_requires=[
    'Click'
  ],
  entry_points='''
    [console_scripts]
    dragon=dragon:cli
  ''',
)
