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
    description="IP2Proxy Proxy Detection",
    author_email="",
    url="",
    keywords=["OpenAPI", "IP2Proxy Proxy Detection"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    IP2Proxy allows instant detection of anonymous proxy, VPN, TOR exit nodes, search engine robots (SES), data center ranges (PX2-PX10), residential proxies (PX10) and VPN provider name (PX11) by IP address. It also returns the threat type of the proxy (PX9 or higher). Visit https://www.ip2location.com/web-service/ip2proxy for further information.
    """
)

