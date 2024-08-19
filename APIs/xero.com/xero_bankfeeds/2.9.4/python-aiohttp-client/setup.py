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
    description="Xero Bank Feeds API",
    author_email="api@xero.com",
    url="",
    keywords=["OpenAPI", "Xero Bank Feeds API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    The Bank Feeds API is a closed API that is only available to financial institutions that have an established financial services partnership with Xero. If you&#39;re an existing financial services partner that wants access, contact your local Partner Manager. If you&#39;re a financial institution who wants to provide bank feeds to your business customers, contact us to become a financial services partner.
    """
)

