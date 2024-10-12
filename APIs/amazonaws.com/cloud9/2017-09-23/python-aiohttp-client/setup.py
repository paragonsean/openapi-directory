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
    description="AWS Cloud9",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "AWS Cloud9"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;fullname&gt;Cloud9&lt;/fullname&gt; &lt;p&gt;Cloud9 is a collection of tools that you can use to code, build, run, test, debug, and release software in the cloud.&lt;/p&gt; &lt;p&gt;For more information about Cloud9, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloud9/latest/user-guide\&quot;&gt;Cloud9 User Guide&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Cloud9 supports these operations:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;CreateEnvironmentEC2&lt;/code&gt;: Creates an Cloud9 development environment, launches an Amazon EC2 instance, and then connects from the instance to the environment.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;CreateEnvironmentMembership&lt;/code&gt;: Adds an environment member to an environment.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;DeleteEnvironment&lt;/code&gt;: Deletes an environment. If an Amazon EC2 instance is connected to the environment, also terminates the instance.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;DeleteEnvironmentMembership&lt;/code&gt;: Deletes an environment member from an environment.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;DescribeEnvironmentMemberships&lt;/code&gt;: Gets information about environment members for an environment.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;DescribeEnvironments&lt;/code&gt;: Gets information about environments.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;DescribeEnvironmentStatus&lt;/code&gt;: Gets status information for an environment.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ListEnvironments&lt;/code&gt;: Gets a list of environment identifiers.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ListTagsForResource&lt;/code&gt;: Gets the tags for an environment.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;TagResource&lt;/code&gt;: Adds tags to an environment.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;UntagResource&lt;/code&gt;: Removes tags from an environment.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;UpdateEnvironment&lt;/code&gt;: Changes the settings of an existing environment.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;UpdateEnvironmentMembership&lt;/code&gt;: Changes the settings of an existing environment member for an environment.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    """
)

