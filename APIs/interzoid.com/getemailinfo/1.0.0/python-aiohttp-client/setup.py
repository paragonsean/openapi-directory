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
    description="Interzoid Get Email Information API",
    author_email="support@interzoid.com",
    url="",
    keywords=["OpenAPI", "Interzoid Get Email Information API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    This API provides validation information for email addresses to aid in deliverability. Syntax, existence of mail servers, and other tests are run to ensure delivery. Additional demographics are provided for the email address as well, including identifying generic, vulgar, education, government, or other entity type email addresses.
    """
)

