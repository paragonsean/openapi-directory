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
    description="Big Red Cloud API",
    author_email="",
    url="",
    keywords=["OpenAPI", "Big Red Cloud API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
      &lt;div style&#x3D;&#39;line-height: 30px;&#39;&gt;      &lt;strong&gt;Welcome to the Big Red Cloud API&lt;/strong&gt;&lt;br/&gt;      This API enables programmatic access to Big Red Cloud data.&lt;br/&gt;      We have used Swagger to auto generate the API documentation on this page, and it also enables direct interaction with the API in this page. &lt;br/&gt;      To get started, you will require an API Key - check out our guide at &lt;a target&#x3D;&#39;_blank&#39; href&#x3D;&#39;https://www.bigredcloud.com/support/generating-api-key-guide/&#39;&gt;https://www.bigredcloud.com/support/generating-api-key-guide/&lt;/a&gt; for information on how to get one. &lt;br/&gt;      Use the  &#39;Enter API Key&#39; button below to enter your API key and start interacting with your Big Red Cloud data right on this page. &lt;br/&gt;      The API key will be stored in your browsers local storage for convenience, but you will be able to delete it at any time if you wish. &lt;br/&gt;      For additional information on the API, check out our support article at &lt;a target&#x3D;&#39;_blank&#39; href&#x3D;&#39;https://www.bigredcloud.com/support/api/&#39;&gt;https://www.bigredcloud.com/support/api/&lt;/a&gt;&lt;br/&gt;  &lt;/div&gt;
    """
)

