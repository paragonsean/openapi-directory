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
    description="Payments Gateway API",
    author_email="",
    url="",
    keywords=["OpenAPI", "Payments Gateway API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &gt;ℹ️ Onboarding guide  &gt;  &gt; Check the new [Payments onboarding guide](https://developers.vtex.com/docs/guides/payments-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about Payments and is organized by focusing on the developer&#39;s journey.    The Payments Gateway API allows you to get payment data and process your store&#39;s transactions.
    """
)

