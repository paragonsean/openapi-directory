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
    description="Container Analysis API",
    author_email="",
    url="",
    keywords=["OpenAPI", "Container Analysis API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    This API is a prerequisite for leveraging Artifact Analysis scanning capabilities in both Artifact Registry and with Advanced Vulnerability Insights (runtime scanning) in GKE. In addition, the Container Analysis API is an implementation of the Grafeas API, which enables storing, querying, and retrieval of critical metadata about all of your software artifacts.
    """
)

