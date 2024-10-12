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
    description="IoTVAS API",
    author_email="",
    url="",
    keywords=["OpenAPI", "IoTVAS API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    IOTVAS API enables you to discover IoT/Connected devices in the network and provides      detailed real-time risk analysis, including firmware vulnerability analysis without requiring the user to upload the firmware file.     Please visit the [signup page](https://iotvas-api.firmalyzer.com/portal/signup) to create an API key.     IoTVAS API can be easily integrated with vulnerability scanning and network port scanner tools. For example,     we have also released the [IOTVAS NSE script](https://github.com/firmalyzer/iotvas-nmap) that turns the nmap port scanner      to a IoT/connected device discovery and real-time risk assessment tool. For more infromation on IoTVAS and other      solutions please visit [Firmalyzer web site](https://www.firmalyzer.com).
    """
)

