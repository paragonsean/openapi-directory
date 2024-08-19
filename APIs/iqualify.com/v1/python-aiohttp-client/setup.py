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
    description="iQualify Management API",
    author_email="",
    url="",
    keywords=["OpenAPI", "iQualify Management API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    The iQualify API offers management responses for building learning experiences using your iQualify instance data.  Once you’ve registered with iQualify, you can request an API access token by navigating to the API access section of the \&quot;Account Settings\&quot; area.  Find out how to [Request your API access token](https://www.iqualify.com/help/connecting-iqualify-to-other-systems/api/how-to-access-and-manage-your-api-token) on our Knowledge base.  All endpoints are only accessible via https and are located at api.iqualify.com. For instance: you can find your current offerings by accessing the following URL:      https://api.iqualify.com/v1/offerings/current  
    """
)

