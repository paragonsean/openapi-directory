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
    description="Migration Hub Strategy Recommendations",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "Migration Hub Strategy Recommendations"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;p&gt;&lt;fullname&gt;Migration Hub Strategy Recommendations&lt;/fullname&gt; &lt;p&gt;This API reference provides descriptions, syntax, and other details about each of the actions and data types for Migration Hub Strategy Recommendations (Strategy Recommendations). The topic for each action shows the API request parameters and the response. Alternatively, you can use one of the AWS SDKs to access an API that is tailored to the programming language or platform that you&#39;re using. For more information, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/tools/#SDKs\&quot;&gt;AWS SDKs&lt;/a&gt;.&lt;/p&gt;&lt;/p&gt;
    """
)

