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
    description="Redact API",
    author_email="devrel@vonage.com",
    url="",
    keywords=["OpenAPI", "Redact API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    The [Redact API](/redact/overview) helps organisations meet their privacy compliance obligations. It provides controlled, on-demand redaction of private information from transactional records in the long-term storage. Note, Redact API does not have the capability to redact the short-lived server logs that are retained for a few weeks. For SMS customers that need immediate redaction, Vonage suggests using [Advanced Auto-redact](/redact/overview#auto-redact-vs-redact-api).
    """
)

