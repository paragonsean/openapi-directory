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
    description="AWS CodeStar Notifications",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "AWS CodeStar Notifications"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;p&gt;This AWS CodeStar Notifications API Reference provides descriptions and usage examples of the operations and data types for the AWS CodeStar Notifications API. You can use the AWS CodeStar Notifications API to work with the following objects:&lt;/p&gt; &lt;p&gt;Notification rules, by calling the following: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;CreateNotificationRule&lt;/a&gt;, which creates a notification rule for a resource in your account. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;DeleteNotificationRule&lt;/a&gt;, which deletes a notification rule. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;DescribeNotificationRule&lt;/a&gt;, which provides information about a notification rule. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;ListNotificationRules&lt;/a&gt;, which lists the notification rules associated with your account. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;UpdateNotificationRule&lt;/a&gt;, which changes the name, events, or targets associated with a notification rule. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;Subscribe&lt;/a&gt;, which subscribes a target to a notification rule. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;Unsubscribe&lt;/a&gt;, which removes a target from a notification rule. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Targets, by calling the following: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;DeleteTarget&lt;/a&gt;, which removes a notification rule target from a notification rule. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;ListTargets&lt;/a&gt;, which lists the targets associated with a notification rule. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Events, by calling the following: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;ListEventTypes&lt;/a&gt;, which lists the event types you can include in a notification rule. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Tags, by calling the following: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;ListTagsForResource&lt;/a&gt;, which lists the tags already associated with a notification rule in your account. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;TagResource&lt;/a&gt;, which associates a tag you provide with a notification rule in your account. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;UntagResource&lt;/a&gt;, which removes a tag from a notification rule in your account. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt; For information about how to use AWS CodeStar Notifications, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/dtconsole/latest/userguide/what-is-dtconsole.html\&quot;&gt;Amazon Web Services Developer Tools Console User Guide&lt;/a&gt;. &lt;/p&gt;
    """
)

