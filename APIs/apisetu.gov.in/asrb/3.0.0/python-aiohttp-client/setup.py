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
    description="Agricultural Scientists Recruitment Board",
    author_email="",
    url="",
    keywords=["OpenAPI", "Agricultural Scientists Recruitment Board"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    Agricultural Scientist Recruitment Board (ASRB) is now integrated with DigiLocker to publish Digital Marksheet and results for the National Eligibility Test (NET-I) &amp; (NET-II) for the years of 2019. Concerned participants and students can get this certificates on their DigiLocker account.
    """
)

