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
    description="AWS Audit Manager",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "AWS Audit Manager"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;p&gt;Welcome to the Audit Manager API reference. This guide is for developers who need detailed information about the Audit Manager API operations, data types, and errors. &lt;/p&gt; &lt;p&gt;Audit Manager is a service that provides automated evidence collection so that you can continually audit your Amazon Web Services usage. You can use it to assess the effectiveness of your controls, manage risk, and simplify compliance.&lt;/p&gt; &lt;p&gt;Audit Manager provides prebuilt frameworks that structure and automate assessments for a given compliance standard. Frameworks include a prebuilt collection of controls with descriptions and testing procedures. These controls are grouped according to the requirements of the specified compliance standard or regulation. You can also customize frameworks and controls to support internal audits with specific requirements. &lt;/p&gt; &lt;p&gt;Use the following links to get started with the Audit Manager API:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_Operations.html\&quot;&gt;Actions&lt;/a&gt;: An alphabetical list of all Audit Manager API operations.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_Types.html\&quot;&gt;Data types&lt;/a&gt;: An alphabetical list of all Audit Manager data types.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/audit-manager/latest/APIReference/CommonParameters.html\&quot;&gt;Common parameters&lt;/a&gt;: Parameters that all operations can use.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/audit-manager/latest/APIReference/CommonErrors.html\&quot;&gt;Common errors&lt;/a&gt;: Client and server errors that all operations can return.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;If you&#39;re new to Audit Manager, we recommend that you review the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/audit-manager/latest/userguide/what-is.html\&quot;&gt; Audit Manager User Guide&lt;/a&gt;.&lt;/p&gt;
    """
)

