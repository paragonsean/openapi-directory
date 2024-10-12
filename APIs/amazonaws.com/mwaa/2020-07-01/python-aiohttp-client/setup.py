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
    description="AmazonMWAA",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "AmazonMWAA"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;p&gt;&lt;fullname&gt;Amazon Managed Workflows for Apache Airflow&lt;/fullname&gt; &lt;p&gt;This section contains the Amazon Managed Workflows for Apache Airflow (MWAA) API reference documentation. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/mwaa/latest/userguide/what-is-mwaa.html\&quot;&gt;What is Amazon MWAA?&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Endpoints&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;api.airflow.{region}.amazonaws.com&lt;/code&gt; - This endpoint is used for environment management.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/mwaa/latest/API/API_CreateEnvironment.html\&quot;&gt;CreateEnvironment&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/mwaa/latest/API/API_DeleteEnvironment.html\&quot;&gt;DeleteEnvironment&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/mwaa/latest/API/API_GetEnvironment.html\&quot;&gt;GetEnvironment&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/mwaa/latest/API/API_ListEnvironments.html\&quot;&gt;ListEnvironments&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/mwaa/latest/API/API_ListTagsForResource.html\&quot;&gt;ListTagsForResource&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/mwaa/latest/API/API_TagResource.html\&quot;&gt;TagResource&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/mwaa/latest/API/API_UntagResource.html\&quot;&gt;UntagResource&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/mwaa/latest/API/API_UpdateEnvironment.html\&quot;&gt;UpdateEnvironment&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;env.airflow.{region}.amazonaws.com&lt;/code&gt; - This endpoint is used to operate the Airflow environment.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/mwaa/latest/API/API_CreateCliToken.html \&quot;&gt;CreateCliToken&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/mwaa/latest/API/API_CreateWebLoginToken.html\&quot;&gt;CreateWebLoginToken&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ops.airflow.{region}.amazonaws.com&lt;/code&gt; - This endpoint is used to push environment metrics that track environment health.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/mwaa/latest/API/API_PublishMetrics.html \&quot;&gt;PublishMetrics&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt; &lt;b&gt;Regions&lt;/b&gt; &lt;/p&gt; &lt;p&gt;For a list of regions that Amazon MWAA supports, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/mwaa/latest/userguide/what-is-mwaa.html#regions-mwaa\&quot;&gt;Region availability&lt;/a&gt; in the &lt;i&gt;Amazon MWAA User Guide&lt;/i&gt;.&lt;/p&gt;&lt;/p&gt;
    """
)

