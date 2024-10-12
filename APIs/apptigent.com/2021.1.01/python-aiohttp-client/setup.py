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
    description="PowerTools Developer",
    author_email="support@apptigent.com",
    url="",
    keywords=["OpenAPI", "PowerTools Developer"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    Apptigent PowerTools Developer Edition is a powerful suite of API endpoints for custom applications running on any stack. Manipulate text, modify collections, format dates and times, convert currency, perform advanced mathematical calculations, shorten URL&#39;s, encode strings, convert text to speech, translate content into multiple languages, process images, and more. PowerTools is the ultimate developer toolkit.
    """
)

