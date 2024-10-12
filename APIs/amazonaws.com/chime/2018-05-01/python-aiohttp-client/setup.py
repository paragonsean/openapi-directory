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
    description="Amazon Chime",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "Amazon Chime"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;important&gt; &lt;p&gt; &lt;b&gt;Most of these APIs are no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest versions in the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/welcome.html\&quot;&gt;Amazon Chime SDK API reference&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest versions requires migrating to dedicated namespaces. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt; &lt;p&gt;The Amazon Chime application programming interface (API) is designed so administrators can perform key tasks, such as creating and managing Amazon Chime accounts, users, and Voice Connectors. This guide provides detailed information about the Amazon Chime API, including operations, types, inputs and outputs, and error codes.&lt;/p&gt; &lt;p&gt;You can use an AWS SDK, the AWS Command Line Interface (AWS CLI), or the REST API to make API calls for Amazon Chime. We recommend using an AWS SDK or the AWS CLI. The page for each API action contains a &lt;i&gt;See Also&lt;/i&gt; section that includes links to information about using the action with a language-specific AWS SDK or the AWS CLI.&lt;/p&gt; &lt;dl&gt; &lt;dt&gt;Using an AWS SDK&lt;/dt&gt; &lt;dd&gt; &lt;p&gt; You don&#39;t need to write code to calculate a signature for request authentication. The SDK clients authenticate your requests by using access keys that you provide. For more information about AWS SDKs, see the &lt;a href&#x3D;\&quot;http://aws.amazon.com/developer/\&quot;&gt;AWS Developer Center&lt;/a&gt;. &lt;/p&gt; &lt;/dd&gt; &lt;dt&gt;Using the AWS CLI&lt;/dt&gt; &lt;dd&gt; &lt;p&gt;Use your access keys with the AWS CLI to make API calls. For information about setting up the AWS CLI, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cli/latest/userguide/installing.html\&quot;&gt;Installing the AWS Command Line Interface&lt;/a&gt; in the &lt;i&gt;AWS Command Line Interface User Guide&lt;/i&gt;. For a list of available Amazon Chime commands, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cli/latest/reference/chime/index.html\&quot;&gt;Amazon Chime commands&lt;/a&gt; in the &lt;i&gt;AWS CLI Command Reference&lt;/i&gt;. &lt;/p&gt; &lt;/dd&gt; &lt;dt&gt;Using REST APIs&lt;/dt&gt; &lt;dd&gt; &lt;p&gt;If you use REST to make API calls, you must authenticate your request by providing a signature. Amazon Chime supports Signature Version 4. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html\&quot;&gt;Signature Version 4 Signing Process&lt;/a&gt; in the &lt;i&gt;Amazon Web Services General Reference&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;When making REST API calls, use the service name &lt;code&gt;chime&lt;/code&gt; and REST endpoint &lt;code&gt;https://service.chime.aws.amazon.com&lt;/code&gt;.&lt;/p&gt; &lt;/dd&gt; &lt;/dl&gt; &lt;p&gt;Administrative permissions are controlled using AWS Identity and Access Management (IAM). For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime/latest/ag/security-iam.html\&quot;&gt;Identity and Access Management for Amazon Chime&lt;/a&gt; in the &lt;i&gt;Amazon Chime Administration Guide&lt;/i&gt;.&lt;/p&gt;
    """
)

