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
    description="Board of Ayurvedic and Unani Systems of Medicine, Himachal Pradesh, Himachal Pradesh",
    author_email="",
    url="",
    keywords=["OpenAPI", "Board of Ayurvedic and Unani Systems of Medicine, Himachal Pradesh, Himachal Pradesh"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    Board of Ayurvedic and Unani Systems of Medicine, Himachal Pradesh (http://hpayushboard.org/) is the online service portal by Govt. of Himachal Pradesh. Registration Certificate issued online, can be pulled into citizens DigiLocker accounts.
    """
)

