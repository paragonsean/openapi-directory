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
    description="Verify API",
    author_email="devrel@vonage.com",
    url="",
    keywords=["OpenAPI", "Verify API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    The Verify API helps you to implement 2FA (two-factor authentication) in your applications. This is useful for:  * Protecting against spam, by preventing spammers from creating multiple accounts * Monitoring suspicious activity, by forcing an account user to verify ownership of a number * Ensuring that you can reach your users at any time because you have their correct phone number More information is available at &lt;https://developer.nexmo.com/verify&gt;
    """
)

