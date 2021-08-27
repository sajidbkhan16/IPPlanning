from setuptools import setup
from setuptools import find_packages
import os

setup(
    name = 'IPPlanning',
    version = '1.0.0',
    description = 'this package can be used to generate subnets',
    author ='Sajid B Khan',
    author_emails = 'sajidbisnarkhan@hotmail.com',
    package = find_packages(),
    install_requires = [
        'pandas>1.0.5', 'openpyxl==3.0.7'
        ]
    
)
    
