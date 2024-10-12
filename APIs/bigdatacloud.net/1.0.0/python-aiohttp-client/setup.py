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
    description="IP Geolocation API",
    author_email="",
    url="",
    keywords=["OpenAPI", "IP Geolocation API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    BigDataCloud&#39;s IP Geolocation API returns detailed information about the geographical location, ownership and connectivity of the provided IPv4 IP address.  This API is powered by patent-pending ‘Next Generation IP Geolocation Technology&#39;. As a result, the API has sub-millisecond response time.  You can authenticate the API with the use of API keys provided in your BigDataCloud account.  BigDataCloud provides 10K Free queries per month. You can upgrade your package with $2/month per 10K additional queries.  The API has Unprecedented Update Rate - Geolocation data re-evaluated every 2 hours or at least once a day - BGP data updated every 2 hours - Registry data updated at least once a day - Country object data usually updates at least once in a month   You can learn more about the API at [bigdatacloud.com](https://www.bigdatacloud.com/ip-geolocation-apis).
    """
)

