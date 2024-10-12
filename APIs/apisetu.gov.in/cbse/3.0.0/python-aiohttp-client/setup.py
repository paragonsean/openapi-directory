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
    description="Central Board of Secondary Education",
    author_email="",
    url="",
    keywords=["OpenAPI", "Central Board of Secondary Education"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    CBSE (http://www.cbse.nic.in/) is issuing marksheets, passing certificates, migration certificates etc. through DigiLocker. These are either pushed, or can be pulled by students into their DigiLocker accounts. Currently available - 2004 - 2020 [Class XII], 2004 - 2020 [Class X], 2017 (NEET Rank Letter &amp; Marksheet), 2016 (NEET Rank Letter), 2018 December (CTET Eligibility Certificate &amp; Marksheet).
    """
)

