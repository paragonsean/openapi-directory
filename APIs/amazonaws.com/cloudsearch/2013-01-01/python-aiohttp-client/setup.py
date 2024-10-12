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
    description="Amazon CloudSearch",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "Amazon CloudSearch"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;fullname&gt;Amazon CloudSearch Configuration Service&lt;/fullname&gt; &lt;p&gt;You use the Amazon CloudSearch configuration service to create, configure, and manage search domains. Configuration service requests are submitted using the AWS Query protocol. AWS Query requests are HTTP or HTTPS requests submitted via HTTP GET or POST with a query parameter named Action.&lt;/p&gt; &lt;p&gt;The endpoint for configuration service requests is region-specific: cloudsearch.&lt;i&gt;region&lt;/i&gt;.amazonaws.com. For example, cloudsearch.us-east-1.amazonaws.com. For a current list of supported regions and endpoints, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/general/latest/gr/rande.html#cloudsearch_region\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Regions and Endpoints&lt;/a&gt;.&lt;/p&gt;
    """
)

