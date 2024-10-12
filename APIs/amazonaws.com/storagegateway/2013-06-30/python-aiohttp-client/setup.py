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
    description="AWS Storage Gateway",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "AWS Storage Gateway"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;fullname&gt;Storage Gateway Service&lt;/fullname&gt; &lt;p&gt;Storage Gateway is the service that connects an on-premises software appliance with cloud-based storage to provide seamless and secure integration between an organization&#39;s on-premises IT environment and the Amazon Web Services storage infrastructure. The service enables you to securely upload data to the Amazon Web Services Cloud for cost effective backup and rapid disaster recovery.&lt;/p&gt; &lt;p&gt;Use the following links to get started using the &lt;i&gt;Storage Gateway Service API Reference&lt;/i&gt;:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/storagegateway/latest/userguide/AWSStorageGatewayAPI.html#AWSStorageGatewayHTTPRequestsHeaders\&quot;&gt;Storage Gateway required request headers&lt;/a&gt;: Describes the required headers that you must send with every POST request to Storage Gateway.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/storagegateway/latest/userguide/AWSStorageGatewayAPI.html#AWSStorageGatewaySigningRequests\&quot;&gt;Signing requests&lt;/a&gt;: Storage Gateway requires that you authenticate every request you send; this topic describes how sign such a request.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/storagegateway/latest/userguide/AWSStorageGatewayAPI.html#APIErrorResponses\&quot;&gt;Error responses&lt;/a&gt;: Provides reference information about Storage Gateway errors.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_Operations.html\&quot;&gt;Operations in Storage Gateway&lt;/a&gt;: Contains detailed descriptions of all Storage Gateway operations, their request parameters, response elements, possible errors, and examples of requests and responses.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/sg.html\&quot;&gt;Storage Gateway endpoints and quotas&lt;/a&gt;: Provides a list of each Amazon Web Services Region and the endpoints available for use with Storage Gateway.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;note&gt; &lt;p&gt;Storage Gateway resource IDs are in uppercase. When you use these resource IDs with the Amazon EC2 API, EC2 expects resource IDs in lowercase. You must change your resource ID to lowercase to use it with the EC2 API. For example, in Storage Gateway the ID for a volume might be &lt;code&gt;vol-AA22BB012345DAF670&lt;/code&gt;. When you use this ID with the EC2 API, you must change it to &lt;code&gt;vol-aa22bb012345daf670&lt;/code&gt;. Otherwise, the EC2 API might not behave as expected.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt;IDs for Storage Gateway volumes and Amazon EBS snapshots created from gateway volumes are changing to a longer format. Starting in December 2016, all new volumes and snapshots will be created with a 17-character string. Starting in April 2016, you will be able to use these longer IDs so you can test your systems with the new format. For more information, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/ec2/faqs/#longer-ids\&quot;&gt;Longer EC2 and EBS resource IDs&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;For example, a volume Amazon Resource Name (ARN) with the longer volume ID format looks like the following:&lt;/p&gt; &lt;p&gt; &lt;code&gt;arn:aws:storagegateway:us-west-2:111122223333:gateway/sgw-12A3456B/volume/vol-1122AABBCCDDEEFFG&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;A snapshot ID with the longer ID format looks like the following: &lt;code&gt;snap-78e226633445566ee&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;http://forums.aws.amazon.com/ann.jspa?annID&#x3D;3557\&quot;&gt;Announcement: Heads-up – Longer Storage Gateway volume and snapshot IDs coming in 2016&lt;/a&gt;.&lt;/p&gt; &lt;/important&gt;
    """
)

