from setuptools import setup, find_packages

setup(name='lib_test',
      version='1.3',
      description='Python Distribution Utilities',
      author='Pablo Pila',
      # author_email='gward@python.net',
      # url='https://www.python.org/sigs/distutils-sig/',
      packages=find_packages(include=['extra', '*.m4a', '*.py']),
     )
