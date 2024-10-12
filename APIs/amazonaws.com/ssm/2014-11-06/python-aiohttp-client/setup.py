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
    description="Amazon Simple Systems Manager (SSM)",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "Amazon Simple Systems Manager (SSM)"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;p&gt;Amazon Web Services Systems Manager is the operations hub for your Amazon Web Services applications and resources and a secure end-to-end management solution for hybrid cloud environments that enables safe and secure operations at scale.&lt;/p&gt; &lt;p&gt;This reference is intended to be used with the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/systems-manager/latest/userguide/\&quot;&gt;Amazon Web Services Systems Manager User Guide&lt;/a&gt;. To get started, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-setting-up.html\&quot;&gt;Setting up Amazon Web Services Systems Manager&lt;/a&gt;.&lt;/p&gt; &lt;p class&#x3D;\&quot;title\&quot;&gt; &lt;b&gt;Related resources&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;For information about each of the capabilities that comprise Systems Manager, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/systems-manager-capabilities.html\&quot;&gt;Systems Manager capabilities&lt;/a&gt; in the &lt;i&gt;Amazon Web Services Systems Manager User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;For details about predefined runbooks for Automation, a capability of Amazon Web Services Systems Manager, see the &lt;i&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-runbook-reference.html\&quot;&gt;Systems Manager Automation runbook reference&lt;/a&gt; &lt;/i&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;For information about AppConfig, a capability of Systems Manager, see the &lt;i&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/appconfig/latest/userguide/\&quot;&gt;AppConfig User Guide&lt;/a&gt; &lt;/i&gt; and the &lt;i&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/\&quot;&gt;AppConfig API Reference&lt;/a&gt; &lt;/i&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;For information about Incident Manager, a capability of Systems Manager, see the &lt;i&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/incident-manager/latest/userguide/\&quot;&gt;Systems Manager Incident Manager User Guide&lt;/a&gt; &lt;/i&gt; and the &lt;i&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/incident-manager/latest/APIReference/\&quot;&gt;Systems Manager Incident Manager API Reference&lt;/a&gt; &lt;/i&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    """
)

