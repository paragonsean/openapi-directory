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
    description="Amazon OpenSearch Service",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "Amazon OpenSearch Service"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;p&gt;Use the Amazon OpenSearch Service configuration API to create, configure, and manage OpenSearch Service domains.&lt;/p&gt; &lt;p&gt;For sample code that uses the configuration API, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/opensearch-service/latest/developerguide/opensearch-configuration-samples.html\&quot;&gt; &lt;i&gt;Amazon OpenSearch Service Developer Guide&lt;/i&gt; &lt;/a&gt;. The guide also contains &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/opensearch-service/latest/developerguide/request-signing.html\&quot;&gt;sample code&lt;/a&gt; for sending signed HTTP requests to the OpenSearch APIs. The endpoint for configuration service requests is Region specific: es.&lt;i&gt;region&lt;/i&gt;.amazonaws.com. For example, es.us-east-1.amazonaws.com. For a current list of supported Regions and endpoints, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/rande.html#service-regions\&quot;&gt;Amazon Web Services service endpoints&lt;/a&gt;.&lt;/p&gt;
    """
)

