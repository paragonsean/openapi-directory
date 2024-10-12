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
    description="BC Laws",
    author_email="",
    url="",
    keywords=["OpenAPI", "BC Laws"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    BC Laws is an electronic library providing free public access to the laws of British Columbia. BC Laws is hosted by the Queen&#39;s Printer of British Columbia and published in partnership with the Ministry of Justice and the Law Clerk of the Legislative Assembly.BC Laws contains a comprehensive collection of BC legislation and related materials. It is available on the internet in two forms:First: The library is available as a web site in which users can browse and search the laws of British Columbia.Second: The library is available as a portal to legislation in raw XML data format, accessible via the BC Laws API2. This direct access to raw data is intended to enable third parties to build or add their own custom applications based on the structure of the data and all the associated search functionality inherent in that structure. The BC Laws website itself is an example of one such application.   Please note that you may experience issues when submitting requests to the delivery or test environment if using this [OpenAPI specification](https://github.com/bcgov/api-specs) in other API console viewers.
    """
)

