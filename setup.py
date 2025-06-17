# building our application as a package
from setuptools import find_packages, setup

setup(
    name='mlproject',
    version='0.0.1',
    author='abhay',
    author_email='abhaythakre131@gmail.com',
    packages=find_packages(),
    install_requires=['pandas', 'numpy', 'seaborn', 'matplotlib']
)
