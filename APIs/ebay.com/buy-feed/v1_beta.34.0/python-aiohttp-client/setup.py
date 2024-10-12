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
    description="Item Feed Service",
    author_email="",
    url="",
    keywords=["OpenAPI", "Item Feed Service"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; This is a &lt;a href&#x3D;\&quot;https://developer.ebay.com/api-docs/static/versioning.html#limited \&quot; target&#x3D;\&quot;_blank\&quot;&gt; &lt;img src&#x3D;\&quot;/cms/img/docs/partners-api.svg\&quot; class&#x3D;\&quot;legend-icon partners-icon\&quot; title&#x3D;\&quot;Limited Release\&quot;  alt&#x3D;\&quot;Limited Release\&quot; /&gt;(Limited Release)&lt;/a&gt; API available only to select developers approved by business units. For information on how to obtain access to this API in production, see the &lt;a href&#x3D;\&quot;api-docs/buy/static/buy-requirements.html\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Buy APIs Requirements&lt;/a&gt;.&lt;/span&gt;&lt;br&gt;&lt;br&gt;The Feed API provides the ability to download TSV_GZIP feed files containing eBay items and an hourly snapshot file of the items that have changed within an hour for a specific category, date and marketplace. &lt;p&gt;In addition to the API, there is an open source &lt;a href&#x3D;\&quot;https://github.com/eBay/FeedSDK \&quot; target&#x3D;\&quot;_blank\&quot;&gt;Feed SDK&lt;/a&gt; written in Java that downloads, combines files into a single file when needed, and unzips the entire feed file. It also lets you specify field filters to curate the items in the file.&lt;/p&gt;
    """
)

