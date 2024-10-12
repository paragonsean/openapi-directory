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
    description="OnSched Consumer API",
    author_email="",
    url="",
    keywords=["OpenAPI", "OnSched Consumer API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    Build secure and scalable custom apps for Online Booking. Our flexible API provides many options for availability and booking.  &lt;br&gt;&lt;br&gt;  Take the API for a test drive. Just click on the Authorize button below and authenticate.   You can access our demo company profile if you are not a customer, or your own profile by using your assigned ClientId and Secret.  &lt;br&gt;&lt;br&gt;  The API has two interfaces, consumer and setup.   &lt;ul&gt;  &lt;li&gt;  The consumer interface provides all the endpoints required for implementing consumer booking flows.  &lt;/li&gt;  &lt;li&gt;  The setup interface provides endpoints for profile configuration and setup.  &lt;/li&gt;  &lt;/ul&gt;  Toggle freely between the two interfaces using the swagger tool bar option labelled &#39;Select a definition&#39;.  
    """
)

