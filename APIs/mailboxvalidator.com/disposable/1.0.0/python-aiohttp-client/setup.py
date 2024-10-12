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
    description="MailboxValidator Disposable Email Checker",
    author_email="",
    url="",
    keywords=["OpenAPI", "MailboxValidator Disposable Email Checker"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    The MailboxValidator Disposable Email Checker API checks if a single email address is from a disposable email provider and returns the results in either JSON or XML format. Refer to https://www.mailboxvalidator.com/api-email-disposable for further information.
    """
)

