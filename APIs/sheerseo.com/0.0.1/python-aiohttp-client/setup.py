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
    description="SheerSEO API",
    author_email="",
    url="",
    keywords=["OpenAPI", "SheerSEO API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    Sheerseo API has 2 stages:&lt;br&gt;First stage - initiating the task: You fill in your task and receive in return the task id. &lt;br&gt;Second stage - collecting the results: send a request containing the task ids you got at the first stage and collecting the results.
    """
)

