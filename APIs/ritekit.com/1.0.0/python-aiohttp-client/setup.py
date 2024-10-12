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
    description="RiteKit API",
    author_email="",
    url="",
    keywords=["OpenAPI", "RiteKit API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    RiteKit API is based on REST principles.  Authentication uses standard OAuth 2.0 process  ##Getting started  1. Sign up for [RiteKit](https://ritekit.com/)  1. Go to [developer dashboard](https://ritekit.com/developer/dashboard/)  1. Click \&quot;Create a token\&quot; button to get your **Client ID** and **Client secret**  1. When you reach your free limit of calls per month, [upgrade to paid tiers](https://ritekit.com/developer/)  ## Options for authorizing API Calls  #### Using Client ID directly  You can directly connect to our API using your **client ID** by sending it as a GET query parameter. This option is simple (no need for oAuth) but it should be used only in case the Client ID is not exposed publicly.  GET  https://api.ritekit.com/v1/stats/multiple-hashtags?tags&#x3D;php&amp;client_id&#x3D;292c6912e7710c838347ae178b4a
    """
)

