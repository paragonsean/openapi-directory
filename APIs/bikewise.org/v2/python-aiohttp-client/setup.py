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
    description="BikeWise API v2",
    author_email="support@bikeindex.org",
    url="",
    keywords=["OpenAPI", "BikeWise API v2"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;p&gt;This is an API for accessing information about bicycling related incidents. You can find the source code on &lt;a href&#x3D;\&quot;https://github.com/bikeindex/bikewise\&quot;&gt;GitHub&lt;/a&gt;.&lt;/p&gt; 
    """
)

