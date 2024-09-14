from setuptools import setup, find_packages

setup(
      name='easypyside',
      version='0.77',
      description='Python PySide6 Utilities',
      long_description = "README.md",
      author='Pablo GP',
      author_email='pablogonzalezpila@gmail.com',
      url='https://github.com/PaulFilms/easypyside',
      packages=find_packages(),
      include_package_data=True,
      package_data={'easypyside': ['__forms/*']}, 
)

