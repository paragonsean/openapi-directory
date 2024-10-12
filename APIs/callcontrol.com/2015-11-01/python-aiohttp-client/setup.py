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
    description="Call Control API",
    author_email="info@kedlin.com",
    url="",
    keywords=["OpenAPI", "Call Control API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    API for blocking phone calls with Call Control. Data is from crowdsourced community blacklist from 12+ million users and government agencies (FTC, FCC, IRS) Try with api_key &#39;demo&#39;, hit explore above, and then try phone numbers 18008472911,13157244022,17275567300,18008276655,12061231234.
    """
)

