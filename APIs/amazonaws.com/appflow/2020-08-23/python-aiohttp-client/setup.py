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
    description="Amazon Appflow",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "Amazon Appflow"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;p&gt;Welcome to the Amazon AppFlow API reference. This guide is for developers who need detailed information about the Amazon AppFlow API operations, data types, and errors. &lt;/p&gt; &lt;p&gt;Amazon AppFlow is a fully managed integration service that enables you to securely transfer data between software as a service (SaaS) applications like Salesforce, Marketo, Slack, and ServiceNow, and Amazon Web Services like Amazon S3 and Amazon Redshift. &lt;/p&gt; &lt;p&gt;Use the following links to get started on the Amazon AppFlow API:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/appflow/1.0/APIReference/API_Operations.html\&quot;&gt;Actions&lt;/a&gt;: An alphabetical list of all Amazon AppFlow API operations.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/appflow/1.0/APIReference/API_Types.html\&quot;&gt;Data types&lt;/a&gt;: An alphabetical list of all Amazon AppFlow data types.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/appflow/1.0/APIReference/CommonParameters.html\&quot;&gt;Common parameters&lt;/a&gt;: Parameters that all Query operations can use.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/appflow/1.0/APIReference/CommonErrors.html\&quot;&gt;Common errors&lt;/a&gt;: Client and server errors that all operations can return.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;If you&#39;re new to Amazon AppFlow, we recommend that you review the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/appflow/latest/userguide/what-is-appflow.html\&quot;&gt;Amazon AppFlow User Guide&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Amazon AppFlow API users can use vendor-specific mechanisms for OAuth, and include applicable OAuth attributes (such as &lt;code&gt;auth-code&lt;/code&gt; and &lt;code&gt;redirecturi&lt;/code&gt;) with the connector-specific &lt;code&gt;ConnectorProfileProperties&lt;/code&gt; when creating a new connector profile using Amazon AppFlow API operations. For example, Salesforce users can refer to the &lt;a href&#x3D;\&quot;https://help.salesforce.com/articleView?id&#x3D;remoteaccess_authenticate.htm\&quot;&gt; &lt;i&gt;Authorize Apps with OAuth&lt;/i&gt; &lt;/a&gt; documentation.&lt;/p&gt;
    """
)

