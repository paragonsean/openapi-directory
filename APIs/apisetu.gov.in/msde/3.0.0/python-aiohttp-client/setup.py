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
    description="Ministry of Skill Development And Entrepreneurship",
    author_email="",
    url="",
    keywords=["OpenAPI", "Ministry of Skill Development And Entrepreneurship"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    National Council for Vocational Training (NCVT) under Ministry of Skill Development And Entrepreneurship has been entrusted with the responsibilities of prescribing standards and curricula for craftsmen training and conducting All India Trade Tests and awarding National Trade Certificates. All the ITI certificates under the purview of NCVT are available to download through Citizen&#39;s DigiLocker account.
    """
)

