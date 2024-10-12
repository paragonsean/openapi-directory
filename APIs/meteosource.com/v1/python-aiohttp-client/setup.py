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
    description="Interactive documentation for your Premium plan",
    author_email="",
    url="",
    keywords=["OpenAPI", "Interactive documentation for your Premium plan"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
      This interactive documentation is using your API key which is filled in automatically, you can find and change this in [your dashboard](https://www.meteosource.com/client).  Using the &#x60;GET&#x60; button, open your selected endpoint and read the introduction. You will find a detailed description of available parameters. You can complete the &#x60;Parameters&#x60; section and hit &#x60;Execute&#x60; to view a full API response. You can then inspect the JSON response, copy the &#x60;curl&#x60; command to run it on your machine, or obtain a URL of the request. In this way, you can easily build request command for the data you need. 
    """
)

