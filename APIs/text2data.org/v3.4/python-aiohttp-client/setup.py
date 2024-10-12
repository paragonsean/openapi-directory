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
    description="Text Analytics &amp; Sentiment Analysis API | api.text2data.com",
    author_email="",
    url="",
    keywords=["OpenAPI", "Text Analytics &amp; Sentiment Analysis API | api.text2data.com"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;p&gt;The current api version is &lt;b&gt;v3.4&lt;/b&gt;&lt;/p&gt;&lt;br&gt;&lt;br&gt;&lt;p&gt;The api methods listed below can be called directly from this page to test the output. You might set the api_key to pre-authenticate all requests on this page (this will work if your secret is blank).&lt;/p&gt;&lt;br&gt;&lt;br&gt; API endpoint URL: http://{apiName}.text2data.com/v3/ {method}&lt;br&gt;&lt;br&gt;The api can be consumed directly or using our SDK. Our Excel Add-In and Google Sheets Add-on are also using this api to process the data.
    """
)

