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
    description="Logistics API",
    author_email="",
    url="",
    keywords=["OpenAPI", "Logistics API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; This is a &lt;a href&#x3D;\&quot;https://developer.ebay.com/api-docs/static/versioning.html#limited\&quot; target&#x3D;\&quot;_blank\&quot;&gt; &lt;img src&#x3D;\&quot;/cms/img/docs/partners-api.svg\&quot; class&#x3D;\&quot;legend-icon partners-icon\&quot; title&#x3D;\&quot;Limited Release\&quot;  alt&#x3D;\&quot;Limited Release\&quot; /&gt;(Limited Release)&lt;/a&gt; API available only to select developers approved by business units.&lt;/span&gt;&lt;br /&gt;&lt;br /&gt;The &lt;b&gt;Logistics API&lt;/b&gt; resources offer the following capabilities: &lt;ul&gt;&lt;li&gt;&lt;b&gt;shipping_quote&lt;/b&gt; &amp;ndash; Consolidates into a list a set of live shipping rates, or quotes, from which you can select a rate to ship a package.&lt;/li&gt; &lt;li&gt;&lt;b&gt;shipment&lt;/b&gt; &amp;ndash; Creates a \&quot;shipment\&quot; for the selected shipping rate.&lt;/li&gt;&lt;/ul&gt; Call &lt;b&gt;createShippingQuote&lt;/b&gt; to get a list of live shipping rates. The rates returned are all valid for a specific time window and all quoted prices are at eBay-negotiated rates. &lt;br&gt;&lt;br&gt;Select one of the live rates and using its associated &lt;b&gt;rateId&lt;/b&gt;, create a \&quot;shipment\&quot; for the package by calling &lt;b&gt;createFromShippingQuote&lt;/b&gt;. Creating a shipment completes an agreement, and the cost of the base service and any added shipping options are summed into the returned &lt;b&gt;totalShippingCost&lt;/b&gt; value. This action also generates a shipping label that you can use to ship the package.  The total cost of the shipment is incurred when the package is shipped using the supplied shipping label.  &lt;p class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Important!&lt;/b&gt; Sellers must set up a payment method via their eBay account before they can use the methods in this API to create a shipment and the associated shipping label.&lt;/p&gt;
    """
)

