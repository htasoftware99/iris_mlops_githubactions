from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='iris_mlops_project2',
    version='0.1',
    author='HasanTugraAykac',
    packages=find_packages(),
    install_requires=requirements,
)