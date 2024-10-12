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
    description="AWS Budgets",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "AWS Budgets"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;p&gt;Use the Amazon Web Services Budgets API to plan your service usage, service costs, and instance reservations. This API reference provides descriptions, syntax, and usage examples for each of the actions and data types for the Amazon Web Services Budgets feature. &lt;/p&gt; &lt;p&gt;Budgets provide you with a way to see the following information:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;How close your plan is to your budgeted amount or to the free tier limits&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Your usage-to-date, including how much you&#39;ve used of your Reserved Instances (RIs)&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Your current estimated charges from Amazon Web Services, and how much your predicted usage will accrue in charges by the end of the month&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;How much of your budget has been used&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Amazon Web Services updates your budget status several times a day. Budgets track your unblended costs, subscriptions, refunds, and RIs. You can create the following types of budgets:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Cost budgets&lt;/b&gt; - Plan how much you want to spend on a service.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Usage budgets&lt;/b&gt; - Plan how much you want to use one or more services.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;RI utilization budgets&lt;/b&gt; - Define a utilization threshold, and receive alerts when your RI usage falls below that threshold. This lets you see if your RIs are unused or under-utilized.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;RI coverage budgets&lt;/b&gt; - Define a coverage threshold, and receive alerts when the number of your instance hours that are covered by RIs fall below that threshold. This lets you see how much of your instance usage is covered by a reservation.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Service Endpoint&lt;/p&gt; &lt;p&gt;The Amazon Web Services Budgets API provides the following endpoint:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;https://budgets.amazonaws.com&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;For information about costs that are associated with the Amazon Web Services Budgets API, see &lt;a href&#x3D;\&quot;https://aws.amazon.com/aws-cost-management/pricing/\&quot;&gt;Amazon Web Services Cost Management Pricing&lt;/a&gt;.&lt;/p&gt;
    """
)

