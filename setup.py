#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

requirements = [
    'click>=7.1.2',
    'pathlib>=1.0.1'
]

test_requirements = [
    'tox>=3.20.0',
    'flake8>=3.8.4'
]

setup(
    name='path_traveller',
    version='0.2.2',
    description="Travel any path and find some files.",
    long_description=readme,
    long_description_content_type='text/markdown',
    author="Vaibhav Hiwase",
    author_email='hiwase.vaibhav@gmail.com',
    url='https://github.com/vhiwase/path-traveller',
    packages=[
        'path_traveller',
    ],
    package_dir={'path_traveller': 'path_traveller'},

    entry_points={
        'console_scripts': [
            'path_traveller=path_traveller.path_traveller_cli:main'
        ]
    },
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='path_traveller',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3.6',
    test_suite='tests',
    tests_require=test_requirements
)
