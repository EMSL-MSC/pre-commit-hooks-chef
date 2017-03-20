from setuptools import find_packages
from setuptools import setup


setup(
    name='pre_commit_hooks',
    description='Some out-of-the-box hooks for pre-commit.',
    url='https://github.com/pre-commit/pre-commit-hooks',
    version='0.6.1',

    author='Anthony Sottile',
    author_email='asottile@umich.edu',

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],

    packages=find_packages(exclude=('tests*', 'testing*')),
    install_requires=[
        # quickfix to prevent pep8 conflicts
        'flake8!=2.5.3',
        'argparse',
        'autopep8>=1.1',
        'pyyaml',
        'simplejson',
        'six',
    ],
    entry_points={
        'console_scripts': [
            'check-cookstyle = pre_commit_hooks.check_cookstyle:check_cookstyle',
            'check-rspec = pre_commit_hooks.check_rspec:check_rspec',
            'check-foodcritic = pre_commit_hooks.check_foodcritic:check_foodcritic',
        ],
    },
)
