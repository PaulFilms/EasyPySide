from setuptools import setup, find_packages, Extension

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
      name='easypyside',
      version='2025-08-07',
      description='Python PySide6 Utilities',
      long_description = "README.md",
      author='Pablo GP',
      author_email='pablogonzalezpila@gmail.com',
      url='https://github.com/PaulFilms/easypyside',
      packages=find_packages(),
      include_package_data=True,
      package_data={'easypyside': ['__forms/*']}, 
      install_requires=requirements,
)

