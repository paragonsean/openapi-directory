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
    description="AWS Signer",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "AWS Signer"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;p&gt;AWS Signer is a fully managed code signing service to help you ensure the trust and integrity of your code. &lt;/p&gt; &lt;p&gt;AWS Signer supports the following applications:&lt;/p&gt; &lt;p&gt;With code signing for AWS Lambda, you can sign &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/lambda/latest/dg/\&quot;&gt;AWS Lambda&lt;/a&gt; deployment packages. Integrated support is provided for &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/AmazonS3/latest/gsg/\&quot;&gt;Amazon S3&lt;/a&gt;, &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/\&quot;&gt;Amazon CloudWatch&lt;/a&gt;, and &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/awscloudtrail/latest/userguide/\&quot;&gt;AWS CloudTrail&lt;/a&gt;. In order to sign code, you create a signing profile and then use Signer to sign Lambda zip files in S3. &lt;/p&gt; &lt;p&gt;With code signing for IoT, you can sign code for any IoT device that is supported by AWS. IoT code signing is available for &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/freertos/latest/userguide/\&quot;&gt;Amazon FreeRTOS&lt;/a&gt; and &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/iot/latest/developerguide/\&quot;&gt;AWS IoT Device Management&lt;/a&gt;, and is integrated with &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/acm/latest/userguide/\&quot;&gt;AWS Certificate Manager (ACM)&lt;/a&gt;. In order to sign code, you import a third-party code signing certificate using ACM, and use that to sign updates in Amazon FreeRTOS and AWS IoT Device Management. &lt;/p&gt; &lt;p&gt;With code signing for containers …(TBD)&lt;/p&gt; &lt;p&gt;For more information about AWS Signer, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/signer/latest/developerguide/Welcome.html\&quot;&gt;AWS Signer Developer Guide&lt;/a&gt;.&lt;/p&gt;
    """
)

