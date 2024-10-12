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
    description="AWS Resource Groups",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "AWS Resource Groups"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;p&gt;Resource Groups lets you organize Amazon Web Services resources such as Amazon Elastic Compute Cloud instances, Amazon Relational Database Service databases, and Amazon Simple Storage Service buckets into groups using criteria that you define as tags. A resource group is a collection of resources that match the resource types specified in a query, and share one or more tags or portions of tags. You can create a group of resources based on their roles in your cloud infrastructure, lifecycle stages, regions, application layers, or virtually any criteria. Resource Groups enable you to automate management tasks, such as those in Amazon Web Services Systems Manager Automation documents, on tag-related resources in Amazon Web Services Systems Manager. Groups of tagged resources also let you quickly view a custom console in Amazon Web Services Systems Manager that shows Config compliance and other monitoring data about member resources.&lt;/p&gt; &lt;p&gt;To create a resource group, build a resource query, and specify tags that identify the criteria that members of the group have in common. Tags are key-value pairs.&lt;/p&gt; &lt;p&gt;For more information about Resource Groups, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ARG/latest/userguide/welcome.html\&quot;&gt;Resource Groups User Guide&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Resource Groups uses a REST-compliant API that you can use to perform the following types of operations.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Create, Read, Update, and Delete (CRUD) operations on resource groups and resource query entities&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Applying, editing, and removing tags from resource groups&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Resolving resource group member ARNs so they can be returned as search results&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Getting data about resources that are members of a group&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Searching Amazon Web Services resources based on a resource query&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    """
)

