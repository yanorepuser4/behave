# -*- coding: UTF-8 -*
"""
Setup script for behave.

USAGE:
    python setup.py install
    python setup.py behave_test     # -- XFAIL on Windows (currently).
    python setup.py nosetests

REQUIRES:
* setuptools >= 36.2.0

SEE ALSO:
* https://setuptools.readthedocs.io/en/latest/history.html
"""

import sys
import os.path

HERE0 = os.path.dirname(__file__) or os.curdir
os.chdir(HERE0)
HERE = os.curdir
sys.path.insert(0, HERE)

from setuptools import find_packages, setup
from setuptools_behave import behave_test


# -----------------------------------------------------------------------------
# CONFIGURATION:
# -----------------------------------------------------------------------------
python_version = float("%s.%s" % sys.version_info[:2])
BEHAVE = os.path.join(HERE, "behave")
README = os.path.join(HERE, "README.rst")
description = "".join(open(README).readlines()[4:])


# -----------------------------------------------------------------------------
# UTILITY:
# -----------------------------------------------------------------------------
def find_packages_by_root_package(where):
    """
    Better than excluding everything that is not needed,
    collect only what is needed.
    """
    root_package = os.path.basename(where)
    packages = [ "%s.%s" % (root_package, sub_package)
                 for sub_package in find_packages(where)]
    packages.insert(0, root_package)
    return packages


# -----------------------------------------------------------------------------
# SETUP:
# -----------------------------------------------------------------------------
setup(
    name="behave",
    version="1.2.7.dev5",
    description="behave is behaviour-driven development, Python style",
    long_description=description,
    author="Jens Engel, Benno Rice and Richard Jones",
    author_email="behave-users@googlegroups.com",
    url="https://github.com/behave/behave",
    provides = ["behave", "setuptools_behave"],
    packages = find_packages_by_root_package(BEHAVE),
    py_modules = ["setuptools_behave"],
    entry_points={
        "console_scripts": [
            "behave = behave.__main__:main"
        ],
        "distutils.commands": [
            "behave_test = setuptools_behave:behave_test"
        ]
    },
    # -- REQUIREMENTS:
    # SUPPORT: python2.7, python3.3 (or higher)
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*",
    install_requires=[
        "cucumber-tag-expressions >= 4.1.0",
        "enum34; python_version < '3.4'",
        "parse >= 1.18.0",
        "parse-type >= 0.6.0",
        "six >= 1.15.0",
        "traceback2; python_version < '3.0'",

        # -- PREPARED:
        "win_unicode_console; python_version <= '3.9'",
        "contextlib2;  python_version < '3.5'",
        # DISABLED: "contextlib2 >= 21.6.0;  python_version < '3.5'",
        "colorama >= 0.3.7",

        # -- SUPPORT: "pyproject.toml" (or: "behave.toml")
        "tomli>=1.1.0; python_version >=  '3.0' and python_version < '3.11'",
        "toml>=0.10.2; python_version <  '3.0'",  # py27 support
    ],
    tests_require=[
        "pytest <  5.0; python_version <  '3.0'", # USE: pytest >= 4.2
        "pytest >= 5.0; python_version >= '3.0'",
        "pytest-html >= 1.19.0,<2.0; python_version <  '3.0'",
        "pytest-html >= 2.0;         python_version >= '3.0'",
        "mock  <  4.0;   python_version <  '3.6'",
        "mock  >= 4.0;   python_version >= '3.6'",
        "PyHamcrest >= 2.0.2; python_version >= '3.0'",
        "PyHamcrest <2.2;   python_version <  '3.0'",
        "assertpy >= 1.1",

        # -- HINT: path.py => path (python-install-package was renamed for python3)
        "path >= 13.1.0;         python_version >= '3.5'",
        "path.py >=11.5.0,<13.0; python_version <  '3.5'",
        # -- PYTHON2 BACKPORTS:
        "pathlib;    python_version <= '3.4'",
    ],
    cmdclass = {
        "behave_test": behave_test,
    },
    extras_require={
        "docs": [
            "sphinx >= 7.3.7;   python_version >= '3.7'",
            "sphinx >=1.6,<4.4; python_version < '3.7'",
            "sphinx_bootstrap_theme >= 0.6",
            # -- CONSTRAINTS UNTIL: sphinx > 5.0 can be used -- 2024-01
            # PROBLEM: sphinxcontrib-applehelp v1.0.8 requires sphinx > 5.0
            # SEE: https://stackoverflow.com/questions/77848565/sphinxcontrib-applehelp-breaking-sphinx-builds-with-sphinx-version-less-than-5-0
            "sphinxcontrib-applehelp >= 1.0.8; python_version >= '3.7'",
            "sphinxcontrib-htmlhelp >= 2.0.5;  python_version >= '3.7'",
            # DISABLED: "sphinxcontrib-applehelp==1.0.4",
            # DISABLED: "sphinxcontrib-devhelp==1.0.2",
            # DISABLED: "sphinxcontrib-htmlhelp==2.0.1",
            # DISABLED: "sphinxcontrib-qthelp==1.0.3",
            # DISABLED: "sphinxcontrib-serializinghtml==1.1.5",
        ],
        "develop": [
            "build >= 0.5.1",
            "twine >= 1.13.0",
            "coverage >= 5.0",
            "pytest >=4.2,<5.0; python_version <  '3.0'",  # pytest >= 4.2
            "pytest >= 5.0; python_version >= '3.0'",
            "pytest-html >= 1.19.0,<2.0; python_version <  '3.0'",
            "pytest-html >= 2.0;         python_version >= '3.0'",
            "mock  <  4.0;   python_version <  '3.6'",
            "mock  >= 4.0;   python_version >= '3.6'",
            "PyHamcrest >= 2.0.2; python_version >= '3.0'",
            "PyHamcrest <2.2;   python_version <  '3.0'",
            "pytest-cov",
            "tox   >= 1.8.1,<4.0",   # -- HINT: tox >= 4.0 has breaking changes.
            "virtualenv < 20.22.0",  # -- SUPPORT FOR: Python 2.7, Python <= 3.6
            "invoke >=1.7.0,<2.0; python_version <  '3.6'",
            "invoke >=1.7.0;      python_version >= '3.6'",
            # -- HINT, was RENAMED: path.py => path (for python3)
            "path    >= 13.1.0; python_version >= '3.5'",
            "path.py >= 11.5.0; python_version <  '3.5'",
            "pycmd",
            "pathlib; python_version <= '3.4'",
            "modernize >= 0.5",
            "pylint",
        ],
        'formatters': [
            "behave-html-formatter",
        ],
        'toml': [  # Enable pyproject.toml support.
            "tomli>=1.1.0; python_version >=  '3.0' and python_version < '3.11'",
            "toml>=0.10.2; python_version <  '3.0'",  # py27 support
        ],
    },
    license="BSD",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: Jython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Testing",
        "License :: OSI Approved :: BSD License",
    ],
    zip_safe = True,
)
