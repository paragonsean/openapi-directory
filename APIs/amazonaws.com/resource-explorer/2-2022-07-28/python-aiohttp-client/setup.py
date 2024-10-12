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
    description="AWS Resource Explorer",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "AWS Resource Explorer"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;p&gt;Amazon Web Services Resource Explorer is a resource search and discovery service. By using Resource Explorer, you can explore your resources using an internet search engine-like experience. Examples of resources include Amazon Relational Database Service (Amazon RDS) instances, Amazon Simple Storage Service (Amazon S3) buckets, or Amazon DynamoDB tables. You can search for your resources using resource metadata like names, tags, and IDs. Resource Explorer can search across all of the Amazon Web Services Regions in your account in which you turn the service on, to simplify your cross-Region workloads.&lt;/p&gt; &lt;p&gt;Resource Explorer scans the resources in each of the Amazon Web Services Regions in your Amazon Web Services account in which you turn on Resource Explorer. Resource Explorer &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/resource-explorer/latest/userguide/getting-started-terms-and-concepts.html#term-index\&quot;&gt;creates and maintains an index&lt;/a&gt; in each Region, with the details of that Region&#39;s resources.&lt;/p&gt; &lt;p&gt;You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/resource-explorer/latest/userguide/manage-aggregator-region.html\&quot;&gt;search across all of the indexed Regions in your account&lt;/a&gt; by designating one of your Amazon Web Services Regions to contain the aggregator index for the account. When you &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/resource-explorer/latest/userguide/manage-aggregator-region-turn-on.html\&quot;&gt;promote a local index in a Region to become the aggregator index for the account&lt;/a&gt;, Resource Explorer automatically replicates the index information from all local indexes in the other Regions to the aggregator index. Therefore, the Region with the aggregator index has a copy of all resource information for all Regions in the account where you turned on Resource Explorer. As a result, views in the aggregator index Region include resources from all of the indexed Regions in your account.&lt;/p&gt; &lt;p&gt;For more information about Amazon Web Services Resource Explorer, including how to enable and configure the service, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/resource-explorer/latest/userguide/\&quot;&gt;Amazon Web Services Resource Explorer User Guide&lt;/a&gt;.&lt;/p&gt;
    """
)

