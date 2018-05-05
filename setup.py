#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author="Viyat Bhalodia",
    author_email='viyat.bhalodia@owasp.org',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    description="Optional features that can be plugged into OWTF to extend its functionality.",
    install_requires=requirements,
    license="BSD license",
    long_description=__doc__,
    include_package_data=True,
    keywords='owtf_extensions',
    name='owtf_extensions',
    packages=find_packages(include=['owtf_extensions']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/owtf/owtf-extensions',
    version='0.1.0',
    zip_safe=False,
)
