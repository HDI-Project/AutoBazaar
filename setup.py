#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.md') as history_file:
    history = history_file.read()

install_requires = [
    'baytune==0.2.4',
    'cloudpickle==0.4.0',
    'keras==2.2.4',
    'numpy==1.15.4',
    'mit-d3m==0.1.2',
    'mlblocks==0.3.0',
    'mlprimitives==0.1.4',
    'pandas==0.23.4',
    'pymongo==3.7.2',
    'scikit-learn==0.20.2',
    'scipy==1.1.0',
    'urllib3==1.23',
    'xgboost==0.81'
]

tests_require = [
    'pytest>=3.4.2',
    'pytest-cov>=2.6.0',
    'mlprimitives>=0.1.3,<0.2',
    'urllib3>=1.20,<1.25'
]

setup_requires = [
    'pytest-runner>=2.11.1',
]

development_requires = [
    # general
    'bumpversion>=0.5.3',
    'pip>=10.0.0',
    'watchdog>=0.8.3',

    # docs
    'm2r>=0.2.0',
    'Sphinx>=1.7.1',
    'sphinx_rtd_theme>=0.2.4',
    'autodocsumm>=0.1.10',

    # style check
    'flake8>=3.5.0',
    'isort>=4.3.4',

    # fix style issues
    'autoflake>=1.1',
    'autopep8>=1.3.5',

    # distribute on PyPI
    'twine>=1.10.0',
    'wheel>=0.30.0',
]

setup(
    author='MIT Data To AI Lab',
    author_email='dailabmit@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
    description='The Machine Learning Bazaar',
    entry_points={
        'console_scripts': [
            'abz=autobazaar.__main__:main'
        ]
    },
    extras_require={
        'dev': development_requires + tests_require,
        'tests': tests_require,
    },
    include_package_data=True,
    install_requires=install_requires,
    license='MIT license',
    long_description=readme + '\n\n' + history,
    long_description_content_type='text/markdown',
    keywords='automl machine learning hyperparameters tuning classification regression autobazaar',
    name='autobazaar',
    packages=find_packages(include=['autobazaar', 'autobazaar.*']),
    setup_requires=setup_requires,
    test_suite='tests',
    tests_require=tests_require,
    url='https://github.com/HDI-project/AutoBazaar',
    version='0.1.0-dev',
    zip_safe=False,
)
