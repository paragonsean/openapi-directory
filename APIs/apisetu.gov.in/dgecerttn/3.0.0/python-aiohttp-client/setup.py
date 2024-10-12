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
    description="Tamil Nadu State Board (Tamil Nadu Directorate of Government Examinations), Tamil Nadu",
    author_email="",
    url="",
    keywords=["OpenAPI", "Tamil Nadu State Board (Tamil Nadu Directorate of Government Examinations), Tamil Nadu"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    Tamilnadu - Government Examinations (https://dgecert.tn.nic.in/) is issuing Mark Certificates through DigiLocker. These can be pulled by students into their DigiLocker accounts. Currently Class X (2016-2019) and XII (2016-2018) marksheets are available.
    """
)

