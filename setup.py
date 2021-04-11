from setuptools import setup, find_packages

setup(
name='mypackage',
packages=find_packages(exclude=['tests*']),
license='MIT',
description='EDSA example python package',
long_description=open('readme.md').read(),
install_requires=['numpy'],
url='https://github.com/<username>/package-name',
author='<Maghmoood>',
author_email='<maghmoodrichards@gmail.com>',
)