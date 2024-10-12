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
    description="Synthetics",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "Synthetics"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;fullname&gt;Amazon CloudWatch Synthetics&lt;/fullname&gt; &lt;p&gt;You can use Amazon CloudWatch Synthetics to continually monitor your services. You can create and manage &lt;i&gt;canaries&lt;/i&gt;, which are modular, lightweight scripts that monitor your endpoints and APIs from the outside-in. You can set up your canaries to run 24 hours a day, once per minute. The canaries help you check the availability and latency of your web services and troubleshoot anomalies by investigating load time data, screenshots of the UI, logs, and metrics. The canaries seamlessly integrate with CloudWatch ServiceLens to help you trace the causes of impacted nodes in your applications. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ServiceLens.html\&quot;&gt;Using ServiceLens to Monitor the Health of Your Applications&lt;/a&gt; in the &lt;i&gt;Amazon CloudWatch User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;Before you create and manage canaries, be aware of the security considerations. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/servicelens_canaries_security.html\&quot;&gt;Security Considerations for Synthetics Canaries&lt;/a&gt;.&lt;/p&gt;
    """
)

