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
    description="Amazon AppConfig",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "Amazon AppConfig"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;p&gt;Use AppConfig, a capability of Amazon Web Services Systems Manager, to create, manage, and quickly deploy application configurations. AppConfig supports controlled deployments to applications of any size and includes built-in validation checks and monitoring. You can use AppConfig with applications hosted on Amazon EC2 instances, Lambda, containers, mobile applications, or IoT devices.&lt;/p&gt; &lt;p&gt;To prevent errors when deploying application configurations, especially for production systems where a simple typo could cause an unexpected outage, AppConfig includes validators. A validator provides a syntactic or semantic check to ensure that the configuration you want to deploy works as intended. To validate your application configuration data, you provide a schema or an Amazon Web Services Lambda function that runs against the configuration. The configuration deployment or update can only proceed when the configuration data is valid.&lt;/p&gt; &lt;p&gt;During a configuration deployment, AppConfig monitors the application to ensure that the deployment is successful. If the system encounters an error, AppConfig rolls back the change to minimize impact for your application users. You can configure a deployment strategy for each application or environment that includes deployment criteria, including velocity, bake time, and alarms to monitor. Similar to error monitoring, if a deployment triggers an alarm, AppConfig automatically rolls back to the previous version. &lt;/p&gt; &lt;p&gt;AppConfig supports multiple use cases. Here are some examples:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Feature flags&lt;/b&gt;: Use AppConfig to turn on new features that require a timely deployment, such as a product launch or announcement. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Application tuning&lt;/b&gt;: Use AppConfig to carefully introduce changes to your application that can only be tested with production traffic.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Allow list&lt;/b&gt;: Use AppConfig to allow premium subscribers to access paid content. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Operational issues&lt;/b&gt;: Use AppConfig to reduce stress on your application when a dependency or other external factor impacts the system.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;This reference is intended to be used with the &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/appconfig/latest/userguide/what-is-appconfig.html\&quot;&gt;AppConfig User Guide&lt;/a&gt;.&lt;/p&gt;
    """
)

