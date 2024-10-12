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
    description="AWS Certificate Manager Private Certificate Authority",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "AWS Certificate Manager Private Certificate Authority"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;p&gt;This is the &lt;i&gt;Amazon Web Services Private Certificate Authority API Reference&lt;/i&gt;. It provides descriptions, syntax, and usage examples for each of the actions and data types involved in creating and managing a private certificate authority (CA) for your organization.&lt;/p&gt; &lt;p&gt;The documentation for each action shows the API request parameters and the JSON response. Alternatively, you can use one of the Amazon Web Services SDKs to access an API that is tailored to the programming language or platform that you prefer. For more information, see &lt;a href&#x3D;\&quot;https://aws.amazon.com/tools/#SDKs\&quot;&gt;Amazon Web Services SDKs&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Each Amazon Web Services Private CA API operation has a quota that determines the number of times the operation can be called per second. Amazon Web Services Private CA throttles API requests at different rates depending on the operation. Throttling means that Amazon Web Services Private CA rejects an otherwise valid request because the request exceeds the operation&#39;s quota for the number of requests per second. When a request is throttled, Amazon Web Services Private CA returns a &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/privateca/latest/APIReference/CommonErrors.html\&quot;&gt;ThrottlingException&lt;/a&gt; error. Amazon Web Services Private CA does not guarantee a minimum request rate for APIs. &lt;/p&gt; &lt;p&gt;To see an up-to-date list of your Amazon Web Services Private CA quotas, or to request a quota increase, log into your Amazon Web Services account and visit the &lt;a href&#x3D;\&quot;https://console.aws.amazon.com/servicequotas/\&quot;&gt;Service Quotas&lt;/a&gt; console.&lt;/p&gt;
    """
)

