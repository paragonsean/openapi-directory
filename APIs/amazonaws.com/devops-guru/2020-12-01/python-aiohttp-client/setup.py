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
    description="Amazon DevOps Guru",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "Amazon DevOps Guru"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;p&gt; Amazon DevOps Guru is a fully managed service that helps you identify anomalous behavior in business critical operational applications. You specify the Amazon Web Services resources that you want DevOps Guru to cover, then the Amazon CloudWatch metrics and Amazon Web Services CloudTrail events related to those resources are analyzed. When anomalous behavior is detected, DevOps Guru creates an &lt;i&gt;insight&lt;/i&gt; that includes recommendations, related events, and related metrics that can help you improve your operational applications. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/devops-guru/latest/userguide/welcome.html\&quot;&gt;What is Amazon DevOps Guru&lt;/a&gt;. &lt;/p&gt; &lt;p&gt; You can specify 1 or 2 Amazon Simple Notification Service topics so you are notified every time a new insight is created. You can also enable DevOps Guru to generate an OpsItem in Amazon Web Services Systems Manager for each insight to help you manage and track your work addressing insights. &lt;/p&gt; &lt;p&gt; To learn about the DevOps Guru workflow, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/devops-guru/latest/userguide/welcome.html#how-it-works\&quot;&gt;How DevOps Guru works&lt;/a&gt;. To learn about DevOps Guru concepts, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/devops-guru/latest/userguide/concepts.html\&quot;&gt;Concepts in DevOps Guru&lt;/a&gt;. &lt;/p&gt;
    """
)

