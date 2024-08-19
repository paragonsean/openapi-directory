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
    description="Trello",
    author_email="",
    url="",
    keywords=["OpenAPI", "Trello"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    This document describes the REST API of Trello as published by Trello.com.  - &lt;a href&#x3D;&#39;https://trello.com/docs/index.html&#39; target&#x3D;&#39;_blank&#39;&gt;Official Documentation&lt;/a&gt;  - &lt;a href&#x3D;&#39;https://trello.com/docs/api&#39; target&#x3D;&#39;_blank&#39;&gt;The HTML pages that were scraped in order to generate this specification.&lt;/a&gt;
    """
)

