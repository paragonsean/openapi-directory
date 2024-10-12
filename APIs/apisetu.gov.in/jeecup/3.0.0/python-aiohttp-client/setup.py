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
    description="Joint Entrance Examination Council, Uttar Pradesh, Uttar Pradesh",
    author_email="",
    url="",
    keywords=["OpenAPI", "Joint Entrance Examination Council, Uttar Pradesh, Uttar Pradesh"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    Joint Entrance Examination Council (https://jeecup.nic.in) is providing digital Admit Cards for 2018 entrance examination of Diploma courses in the Polytechnics / Institutes affiliated to Board Of Technical Education, U.P.
    """
)

