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
    description="Nexmo Application API",
    author_email="devrel@nexmo.com",
    url="",
    keywords=["OpenAPI", "Nexmo Application API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;div class&#x3D;\&quot;Vlt-callout Vlt-callout--critical\&quot;&gt; &lt;i&gt;&lt;/i&gt; &lt;div class&#x3D;\&quot;Vlt-callout__content\&quot;&gt;   &lt;h4&gt;Applications V1 is deprecated&lt;/h4&gt;   This version of the API has been deprecated. Please use &lt;a href&#x3D;\&quot;/api/application.v2\&quot;&gt;version 2&lt;/a&gt; going forwards &lt;/div&gt; &lt;/div&gt; A Nexmo application contains the security and configuration information you need to connect to Nexmo endpoints and easily use our products.
    """
)

