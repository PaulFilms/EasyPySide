from setuptools import setup, find_packages

setup(
      name='lib_test',
      version='0.760',
      description='Python PySide6 Utilities',
      long_description = "README.md",
      author='Pablo GP',
      author_email='pablogonzalezpila@gmail.com',
      url='https://github.com/PaulFilms/lib_test',
      packages=find_packages(),
      include_package_data=True, # muy importante para que se incluyan archivos sin extension .py
      package_data={'lib_test': ['__forms/*']}, 
)

