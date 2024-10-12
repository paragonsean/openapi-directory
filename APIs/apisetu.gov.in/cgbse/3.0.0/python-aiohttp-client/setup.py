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
    description="Chhattisgarh State Board of Secondary Education, Chhattisgarh",
    author_email="",
    url="",
    keywords=["OpenAPI", "Chhattisgarh State Board of Secondary Education, Chhattisgarh"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    CBBSE (http://cgbse.nic.in) is issuing marksheets  through DigiLocker. These can be pulled by students into their DigiLocker accounts. Currently available -2001,2003 - 2017 Class X and 2001 - 2017 Class XII .
    """
)

