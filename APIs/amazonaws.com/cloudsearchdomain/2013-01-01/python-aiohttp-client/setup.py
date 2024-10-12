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
    description="Amazon CloudSearch Domain",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "Amazon CloudSearch Domain"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;p&gt;You use the AmazonCloudSearch2013 API to upload documents to a search domain and search those documents. &lt;/p&gt; &lt;p&gt;The endpoints for submitting &lt;code&gt;UploadDocuments&lt;/code&gt;, &lt;code&gt;Search&lt;/code&gt;, and &lt;code&gt;Suggest&lt;/code&gt; requests are domain-specific. To get the endpoints for your domain, use the Amazon CloudSearch configuration service &lt;code&gt;DescribeDomains&lt;/code&gt; action. The domain endpoints are also displayed on the domain dashboard in the Amazon CloudSearch console. You submit suggest requests to the search endpoint. &lt;/p&gt; &lt;p&gt;For more information, see the &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/cloudsearch/latest/developerguide\&quot;&gt;Amazon CloudSearch Developer Guide&lt;/a&gt;.&lt;/p&gt;
    """
)

