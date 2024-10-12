# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "openapi_server"
VERSION = "1.0.0"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "connexion==2.14.1",
    "swagger-ui-bundle==0.0.9",
    "aiohttp_jinja2==1.5.0",
]

setup(
    name=NAME,
    version=VERSION,
    description="Haryana State Board of School Education, Haryana",
    author_email="",
    url="",
    keywords=["OpenAPI", "Haryana State Board of School Education, Haryana"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    Board of School Education, Haryana (http://www.bseh.org.in/home/) has made available 2016-2019 Class XII &amp; Class X results in DigiLocker, which can be pulled by students into their accounts.
    """
)

