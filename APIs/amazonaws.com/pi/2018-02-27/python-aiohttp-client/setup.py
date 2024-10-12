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
    description="AWS Performance Insights",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "AWS Performance Insights"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;fullname&gt;Amazon RDS Performance Insights&lt;/fullname&gt; &lt;p&gt;Amazon RDS Performance Insights enables you to monitor and explore different dimensions of database load based on data captured from a running DB instance. The guide provides detailed information about Performance Insights data types, parameters and errors.&lt;/p&gt; &lt;p&gt;When Performance Insights is enabled, the Amazon RDS Performance Insights API provides visibility into the performance of your DB instance. Amazon CloudWatch provides the authoritative source for Amazon Web Services service-vended monitoring metrics. Performance Insights offers a domain-specific view of DB load.&lt;/p&gt; &lt;p&gt;DB load is measured as average active sessions. Performance Insights provides the data to API consumers as a two-dimensional time-series dataset. The time dimension provides DB load data for each time point in the queried time range. Each time point decomposes overall load in relation to the requested dimensions, measured at that time point. Examples include SQL, Wait event, User, and Host.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;To learn more about Performance Insights and Amazon Aurora DB instances, go to the &lt;i&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights.html\&quot;&gt; Amazon Aurora User Guide&lt;/a&gt; &lt;/i&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;To learn more about Performance Insights and Amazon RDS DB instances, go to the &lt;i&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.html\&quot;&gt; Amazon RDS User Guide&lt;/a&gt; &lt;/i&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;To learn more about Performance Insights and Amazon DocumentDB clusters, go to the &lt;i&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/documentdb/latest/developerguide/performance-insights.html\&quot;&gt; Amazon DocumentDB Developer Guide&lt;/a&gt; &lt;/i&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    """
)

