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
    description="Automata Market Intelligence API",
    author_email="support@byautomata.io",
    url="",
    keywords=["OpenAPI", "Automata Market Intelligence API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    This document provides the documentation for the Market Intelligence API by Automata. Get your API Key at https://apis.byautomata.io and check out our &lt;a href&#x3D;&#39;https://www.getpostman.com/collections/d182a1c78d4491d55e19&#39;&gt;Postman Collection&lt;/a&gt;.&lt;br&gt;&lt;br&gt;The root API endpoint is https://api.byautomata.io. Please refer to the code samples for examples of how to call the Market Intelligence API. The ContentPro endpoints (/contentpro-search and /contentpro-similar-text) are not included in the standard Market Intelligence API plans. Please contact support@byautomata.io for access.
    """
)

