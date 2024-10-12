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
    description="AWS CodeStar connections",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "AWS CodeStar connections"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;fullname&gt;AWS CodeStar Connections&lt;/fullname&gt; &lt;p&gt;This Amazon Web Services CodeStar Connections API Reference provides descriptions and usage examples of the operations and data types for the Amazon Web Services CodeStar Connections API. You can use the connections API to work with connections and installations.&lt;/p&gt; &lt;p&gt; &lt;i&gt;Connections&lt;/i&gt; are configurations that you use to connect Amazon Web Services resources to external code repositories. Each connection is a resource that can be given to services such as CodePipeline to connect to a third-party repository such as Bitbucket. For example, you can add the connection in CodePipeline so that it triggers your pipeline when a code change is made to your third-party code repository. Each connection is named and associated with a unique ARN that is used to reference the connection.&lt;/p&gt; &lt;p&gt;When you create a connection, the console initiates a third-party connection handshake. &lt;i&gt;Installations&lt;/i&gt; are the apps that are used to conduct this handshake. For example, the installation for the Bitbucket provider type is the Bitbucket app. When you create a connection, you can choose an existing installation or create one.&lt;/p&gt; &lt;p&gt;When you want to create a connection to an installed provider type such as GitHub Enterprise Server, you create a &lt;i&gt;host&lt;/i&gt; for your connections.&lt;/p&gt; &lt;p&gt;You can work with connections by calling:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;CreateConnection&lt;/a&gt;, which creates a uniquely named connection that can be referenced by services such as CodePipeline.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;DeleteConnection&lt;/a&gt;, which deletes the specified connection.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;GetConnection&lt;/a&gt;, which returns information about the connection, including the connection status.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;ListConnections&lt;/a&gt;, which lists the connections associated with your account.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;You can work with hosts by calling:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;CreateHost&lt;/a&gt;, which creates a host that represents the infrastructure where your provider is installed.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;DeleteHost&lt;/a&gt;, which deletes the specified host.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;GetHost&lt;/a&gt;, which returns information about the host, including the setup status.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;ListHosts&lt;/a&gt;, which lists the hosts associated with your account.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;You can work with tags in Amazon Web Services CodeStar Connections by calling the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;ListTagsForResource&lt;/a&gt;, which gets information about Amazon Web Services tags for a specified Amazon Resource Name (ARN) in Amazon Web Services CodeStar Connections.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;TagResource&lt;/a&gt;, which adds or updates tags for a resource in Amazon Web Services CodeStar Connections.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;UntagResource&lt;/a&gt;, which removes tags for a resource in Amazon Web Services CodeStar Connections.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;For information about how to use Amazon Web Services CodeStar Connections, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/dtconsole/latest/userguide/welcome-connections.html\&quot;&gt;Developer Tools User Guide&lt;/a&gt;.&lt;/p&gt;
    """
)

