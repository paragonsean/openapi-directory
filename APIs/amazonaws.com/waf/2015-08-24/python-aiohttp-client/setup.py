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
    description="AWS WAF",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "AWS WAF"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;note&gt; &lt;p&gt;This is &lt;b&gt;AWS WAF Classic&lt;/b&gt; documentation. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html\&quot;&gt;AWS WAF Classic&lt;/a&gt; in the developer guide.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For the latest version of AWS WAF&lt;/b&gt;, use the AWS WAFV2 API and see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;. With the latest version, AWS WAF has a single set of endpoints for regional and global use. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;This is the &lt;i&gt;AWS WAF Classic API Reference&lt;/i&gt; for using AWS WAF Classic with Amazon CloudFront. The AWS WAF Classic actions and data types listed in the reference are available for protecting Amazon CloudFront distributions. You can use these actions and data types via the endpoint &lt;i&gt;waf.amazonaws.com&lt;/i&gt;. This guide is for developers who need detailed information about the AWS WAF Classic API actions, data types, and errors. For detailed information about AWS WAF Classic features and an overview of how to use the AWS WAF Classic API, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html\&quot;&gt;AWS WAF Classic&lt;/a&gt; in the developer guide.&lt;/p&gt;
    """
)

