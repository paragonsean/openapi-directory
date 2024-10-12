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
    description="The Water Linked Underwater GPS API",
    author_email="",
    url="",
    keywords=["OpenAPI", "The Water Linked Underwater GPS API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    API for the Water Linked Underwater GPS. For more details: http://www.waterlinked.com  Recommended approach for connecting to a Underwater GPS via the API is: - If \&quot;GET /api/\&quot; times out, the Underwater GPS is not running (on this IP address) - If \&quot;GET /api/\&quot; responds with 200 OK check that the api version returrned (eg \&quot;v1\&quot;) is supported by the client (eg: also supports \&quot;v1\&quot;). - If the api version returned does not match what the client supports: give an error to the user and recommend upgrading. (Eg: response is \&quot;v2\&quot; while client only supports \&quot;v1\&quot;) - If \&quot;GET /api/\&quot; responds with 301 Moved permanently. \&quot;GET /api/v1/version\&quot; to check if the kit has a version earlier than 1.5. - \&quot;GET /api/v1/version\&quot; will always respond with 200 OK on Underwater GPS earlier than 1.5 release.  Configuration API is is not considered stable and will potentially be changed
    """
)

