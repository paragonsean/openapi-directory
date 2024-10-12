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
    description="Rajasthan Board of Secondary Education",
    author_email="",
    url="",
    keywords=["OpenAPI", "Rajasthan Board of Secondary Education"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    Board of High School and Intermediate Education, Rajasthan (http://rajeduboard.rajasthan.gov.in/) has made available Class X (2018-2019)&amp; Class XII (2019) mark sheet available on DigiLocker, which can be pulled by students into their respective accounts
    """
)

