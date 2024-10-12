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
    description="AWS Key Management Service",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "AWS Key Management Service"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;fullname&gt;Key Management Service&lt;/fullname&gt; &lt;p&gt;Key Management Service (KMS) is an encryption and key management web service. This guide describes the KMS operations that you can call programmatically. For general information about KMS, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kms/latest/developerguide/\&quot;&gt; &lt;i&gt;Key Management Service Developer Guide&lt;/i&gt; &lt;/a&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;KMS has replaced the term &lt;i&gt;customer master key (CMK)&lt;/i&gt; with &lt;i&gt;KMS key&lt;/i&gt; and &lt;i&gt;KMS key&lt;/i&gt;. The concept has not changed. To prevent breaking changes, KMS is keeping some variations of this term.&lt;/p&gt; &lt;p&gt;Amazon Web Services provides SDKs that consist of libraries and sample code for various programming languages and platforms (Java, Ruby, .Net, macOS, Android, etc.). The SDKs provide a convenient way to create programmatic access to KMS and other Amazon Web Services services. For example, the SDKs take care of tasks such as signing requests (see below), managing errors, and retrying requests automatically. For more information about the Amazon Web Services SDKs, including how to download and install them, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/tools/\&quot;&gt;Tools for Amazon Web Services&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;We recommend that you use the Amazon Web Services SDKs to make programmatic API calls to KMS.&lt;/p&gt; &lt;p&gt;If you need to use FIPS 140-2 validated cryptographic modules when communicating with Amazon Web Services, use the FIPS endpoint in your preferred Amazon Web Services Region. For more information about the available FIPS endpoints, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/kms.html#kms_region\&quot;&gt;Service endpoints&lt;/a&gt; in the Key Management Service topic of the &lt;i&gt;Amazon Web Services General Reference&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;All KMS API calls must be signed and be transmitted using Transport Layer Security (TLS). KMS recommends you always use the latest supported TLS version. Clients must also support cipher suites with Perfect Forward Secrecy (PFS) such as Ephemeral Diffie-Hellman (DHE) or Elliptic Curve Ephemeral Diffie-Hellman (ECDHE). Most modern systems such as Java 7 and later support these modes.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Signing Requests&lt;/b&gt; &lt;/p&gt; &lt;p&gt;Requests must be signed using an access key ID and a secret access key. We strongly recommend that you do not use your Amazon Web Services account root access key ID and secret access key for everyday work. You can use the access key ID and secret access key for an IAM user or you can use the Security Token Service (STS) to generate temporary security credentials and use those to sign requests. &lt;/p&gt; &lt;p&gt;All KMS requests must be signed with &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html\&quot;&gt;Signature Version 4&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Logging API Requests&lt;/b&gt; &lt;/p&gt; &lt;p&gt;KMS supports CloudTrail, a service that logs Amazon Web Services API calls and related events for your Amazon Web Services account and delivers them to an Amazon S3 bucket that you specify. By using the information collected by CloudTrail, you can determine what requests were made to KMS, who made the request, when it was made, and so on. To learn more about CloudTrail, including how to turn it on and find your log files, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/awscloudtrail/latest/userguide/\&quot;&gt;CloudTrail User Guide&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Additional Resources&lt;/b&gt; &lt;/p&gt; &lt;p&gt;For more information about credentials and request signing, see the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-security-credentials.html\&quot;&gt;Amazon Web Services Security Credentials&lt;/a&gt; - This topic provides general information about the types of credentials used to access Amazon Web Services.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html\&quot;&gt;Temporary Security Credentials&lt;/a&gt; - This section of the &lt;i&gt;IAM User Guide&lt;/i&gt; describes how to create and use temporary security credentials.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html\&quot;&gt;Signature Version 4 Signing Process&lt;/a&gt; - This set of topics walks you through the process of signing a request using an access key ID and a secret access key.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt; &lt;b&gt;Commonly Used API Operations&lt;/b&gt; &lt;/p&gt; &lt;p&gt;Of the API operations discussed in this guide, the following will prove the most useful for most applications. You will likely perform operations other than these, such as creating keys and assigning policies, by using the console.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;Encrypt&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;Decrypt&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;GenerateDataKey&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;GenerateDataKeyWithoutPlaintext&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    """
)

