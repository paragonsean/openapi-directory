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
    description="Test the ExhibitDay API with Swagger",
    author_email="",
    url="",
    keywords=["OpenAPI", "Test the ExhibitDay API with Swagger"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    This API can be used to programmatically pull data out of ExhibitDay or push data into ExhibitDay -- allowing for automation between ExhibitDay and your internal systems (or other third-party software). To use the API, you&#39;ll need working knowledge of consuming REST APIs.&lt;br /&gt;&lt;br /&gt;Docs: https://api.exhibitday.com/swagger/docs/v1
    """
)

