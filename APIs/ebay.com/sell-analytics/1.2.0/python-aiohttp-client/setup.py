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
    description=" Seller Service Metrics API ",
    author_email="",
    url="",
    keywords=["OpenAPI", " Seller Service Metrics API "],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    The &lt;i&gt;Analytics API&lt;/i&gt; provides data and information about a seller and their eBay business.  &lt;br&gt;&lt;br&gt;The resources and methods in this API let sellers review information on their listing performance, metrics on their customer service performance, and details on their eBay seller performance rating.  &lt;br&gt;&lt;br&gt;The three resources in the Analytics API provide the following data and information: &lt;ul&gt;&lt;li&gt;&lt;b&gt;Customer Service Metric&lt;/b&gt; &amp;ndash; Returns data on a seller&#39;s customer service performance as compared to other seller&#39;s in the same peer group.&lt;/li&gt; &lt;li&gt;&lt;b&gt;Traffic Report&lt;/b&gt; &amp;ndash; Returns data that shows how buyers are engaging with a seller&#39;s listings.&lt;/li&gt; &lt;li&gt;&lt;b&gt;Seller Standards Profile&lt;/b&gt; &amp;ndash; Returns data pertaining to a seller&#39;s performance rating.&lt;/li&gt;&lt;/ul&gt; Sellers can use the data and information returned by the various Analytics API methods to determine where they can make improvements to increase sales and how they might improve their seller status as viewed by eBay buyers.  &lt;br&gt;&lt;br&gt;For details on using this API, see &lt;a href&#x3D;\&quot;/api-docs/sell/static/performance/analyzing-performance.html\&quot; title&#x3D;\&quot;Selling Integration Guide\&quot;&gt;Analyzing seller performance&lt;/a&gt;.
    """
)

