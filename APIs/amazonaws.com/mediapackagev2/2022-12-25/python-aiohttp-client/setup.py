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
    description="AWS Elemental MediaPackage v2",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "AWS Elemental MediaPackage v2"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;note&gt; &lt;p&gt;This guide is intended for creating AWS Elemental MediaPackage resources in MediaPackage Version 2 (v2) starting from May 2023. To get started with MediaPackage v2, create your MediaPackage resources. There isn&#39;t an automated process to migrate your resources from MediaPackage v1 to MediaPackage v2. &lt;/p&gt; &lt;p&gt;The names of the entities that you use to access this API, like URLs and ARNs, all have the versioning information added, like \&quot;v2\&quot;, to distinguish from the prior version. If you used MediaPackage prior to this release, you can&#39;t use the MediaPackage v2 CLI or the MediaPackage v2 API to access any MediaPackage v1 resources.&lt;/p&gt; &lt;p&gt;If you created resources in MediaPackage v1, use video on demand (VOD) workflows, and aren&#39;t looking to migrate to MediaPackage v2 yet, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/mediapackage/latest/apireference/what-is.html\&quot;&gt;MediaPackage v1 Live API Reference&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;This is the AWS Elemental MediaPackage v2 Live REST API Reference. It describes all the MediaPackage API operations for live content in detail, and provides sample requests, responses, and errors for the supported web services protocols.&lt;/p&gt; &lt;p&gt;We assume that you have the IAM permissions that you need to use MediaPackage via the REST API. We also assume that you are familiar with the features and operations of MediaPackage, as described in the AWS Elemental MediaPackage User Guide.&lt;/p&gt;
    """
)

