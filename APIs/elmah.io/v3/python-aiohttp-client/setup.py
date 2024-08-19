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
    description="elmah.io API",
    author_email="",
    url="",
    keywords=["OpenAPI", "elmah.io API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    This is the public REST API for elmah.io. All of the integrations communicates with elmah.io through this API.&lt;br/&gt;&lt;br/&gt;For additional help getting started with the API, visit the following help articles:&lt;br/&gt;&lt;ul&gt;&lt;li&gt;[Using the REST API](https://docs.elmah.io/using-the-rest-api/)&lt;/li&gt;&lt;li&gt;[Where is my API key?](https://docs.elmah.io/where-is-my-api-key/)&lt;/li&gt;&lt;li&gt;[Where is my log ID?](https://docs.elmah.io/where-is-my-log-id/)&lt;/li&gt;&lt;li&gt;[How to configure API key permissions](https://docs.elmah.io/how-to-configure-api-key-permissions/)&lt;/li&gt;&lt;/ul&gt;
    """
)

