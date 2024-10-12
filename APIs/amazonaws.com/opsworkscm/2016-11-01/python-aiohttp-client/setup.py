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
    description="AWS OpsWorks CM",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "AWS OpsWorks CM"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;fullname&gt;AWS OpsWorks CM&lt;/fullname&gt; &lt;p&gt;AWS OpsWorks for configuration management (CM) is a service that runs and manages configuration management servers. You can use AWS OpsWorks CM to create and manage AWS OpsWorks for Chef Automate and AWS OpsWorks for Puppet Enterprise servers, and add or remove nodes for the servers to manage.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Glossary of terms&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Server&lt;/b&gt;: A configuration management server that can be highly-available. The configuration management server runs on an Amazon Elastic Compute Cloud (EC2) instance, and may use various other AWS services, such as Amazon Relational Database Service (RDS) and Elastic Load Balancing. A server is a generic abstraction over the configuration manager that you want to use, much like Amazon RDS. In AWS OpsWorks CM, you do not start or stop servers. After you create servers, they continue to run until they are deleted.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Engine&lt;/b&gt;: The engine is the specific configuration manager that you want to use. Valid values in this release include &lt;code&gt;ChefAutomate&lt;/code&gt; and &lt;code&gt;Puppet&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Backup&lt;/b&gt;: This is an application-level backup of the data that the configuration manager stores. AWS OpsWorks CM creates an S3 bucket for backups when you launch the first server. A backup maintains a snapshot of a server&#39;s configuration-related attributes at the time the backup starts.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Events&lt;/b&gt;: Events are always related to a server. Events are written during server creation, when health checks run, when backups are created, when system maintenance is performed, etc. When you delete a server, the server&#39;s events are also deleted.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Account attributes&lt;/b&gt;: Every account has attributes that are assigned in the AWS OpsWorks CM database. These attributes store information about configuration limits (servers, backups, etc.) and your customer account. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt; &lt;b&gt;Endpoints&lt;/b&gt; &lt;/p&gt; &lt;p&gt;AWS OpsWorks CM supports the following endpoints, all HTTPS. You must connect to one of the following endpoints. Your servers can only be accessed or managed within the endpoint in which they are created.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;opsworks-cm.us-east-1.amazonaws.com&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;opsworks-cm.us-east-2.amazonaws.com&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;opsworks-cm.us-west-1.amazonaws.com&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;opsworks-cm.us-west-2.amazonaws.com&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;opsworks-cm.ap-northeast-1.amazonaws.com&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;opsworks-cm.ap-southeast-1.amazonaws.com&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;opsworks-cm.ap-southeast-2.amazonaws.com&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;opsworks-cm.eu-central-1.amazonaws.com&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;opsworks-cm.eu-west-1.amazonaws.com&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/opsworks-service.html\&quot;&gt;AWS OpsWorks endpoints and quotas&lt;/a&gt; in the AWS General Reference.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Throttling limits&lt;/b&gt; &lt;/p&gt; &lt;p&gt;All API operations allow for five requests per second with a burst of 10 requests per second.&lt;/p&gt;
    """
)

