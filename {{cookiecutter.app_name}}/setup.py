from setuptools import setup, find_packages

setup(
    name='{{cookiecutter.app_name}}',
    version='{{cookiecutter.version}}',
    packages=find_packages(exclude=['tests']),
    install_requires=[
        'pylint',
        'torch',
        'torchvision'
    ]
)