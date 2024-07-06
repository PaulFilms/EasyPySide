from setuptools import setup, find_packages

setup(name='lib_test',
      version='1.3',
      description='Python Distribution Utilities',
      author='Pablo Pila',
      # author_email='gward@python.net',
      # url='https://www.python.org/sigs/distutils-sig/',
      packages=find_packages(),
      include_package_data=True, # muy importante para que se incluyan archivos sin extension .py
      package_data={'lib_test': ['extra/*']}, 
)
