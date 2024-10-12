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
    description="Amazon Glacier",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "Amazon Glacier"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;p&gt; Amazon S3 Glacier (Glacier) is a storage solution for \&quot;cold data.\&quot;&lt;/p&gt; &lt;p&gt;Glacier is an extremely low-cost storage service that provides secure, durable, and easy-to-use storage for data backup and archival. With Glacier, customers can store their data cost effectively for months, years, or decades. Glacier also enables customers to offload the administrative burdens of operating and scaling storage to AWS, so they don&#39;t have to worry about capacity planning, hardware provisioning, data replication, hardware failure and recovery, or time-consuming hardware migrations.&lt;/p&gt; &lt;p&gt;Glacier is a great storage choice when low storage cost is paramount and your data is rarely retrieved. If your application requires fast or frequent access to your data, consider using Amazon S3. For more information, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/s3/\&quot;&gt;Amazon Simple Storage Service (Amazon S3)&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;You can store any kind of data in any format. There is no maximum limit on the total amount of data you can store in Glacier.&lt;/p&gt; &lt;p&gt;If you are a first-time user of Glacier, we recommend that you begin by reading the following sections in the &lt;i&gt;Amazon S3 Glacier Developer Guide&lt;/i&gt;:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonglacier/latest/dev/introduction.html\&quot;&gt;What is Amazon S3 Glacier&lt;/a&gt; - This section of the Developer Guide describes the underlying data model, the operations it supports, and the AWS SDKs that you can use to interact with the service.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonglacier/latest/dev/amazon-glacier-getting-started.html\&quot;&gt;Getting Started with Amazon S3 Glacier&lt;/a&gt; - The Getting Started section walks you through the process of creating a vault, uploading archives, creating jobs to download archives, retrieving the job output, and deleting archives.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    """
)

