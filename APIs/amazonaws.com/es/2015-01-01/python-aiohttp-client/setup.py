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
    description="Amazon Elasticsearch Service",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "Amazon Elasticsearch Service"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;fullname&gt;Amazon Elasticsearch Configuration Service&lt;/fullname&gt; &lt;p&gt;Use the Amazon Elasticsearch Configuration API to create, configure, and manage Elasticsearch domains.&lt;/p&gt; &lt;p&gt;For sample code that uses the Configuration API, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-configuration-samples.html\&quot;&gt;Amazon Elasticsearch Service Developer Guide&lt;/a&gt;. The guide also contains &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-request-signing.html\&quot;&gt;sample code for sending signed HTTP requests to the Elasticsearch APIs&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;The endpoint for configuration service requests is region-specific: es.&lt;i&gt;region&lt;/i&gt;.amazonaws.com. For example, es.us-east-1.amazonaws.com. For a current list of supported regions and endpoints, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/general/latest/gr/rande.html#elasticsearch-service-regions\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Regions and Endpoints&lt;/a&gt;.&lt;/p&gt;
    """
)

