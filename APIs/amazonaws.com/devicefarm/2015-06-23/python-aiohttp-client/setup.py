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
    description="AWS Device Farm",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "AWS Device Farm"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;p&gt;Welcome to the AWS Device Farm API documentation, which contains APIs for:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Testing on desktop browsers&lt;/p&gt; &lt;p&gt; Device Farm makes it possible for you to test your web applications on desktop browsers using Selenium. The APIs for desktop browser testing contain &lt;code&gt;TestGrid&lt;/code&gt; in their names. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/devicefarm/latest/testgrid/\&quot;&gt;Testing Web Applications on Selenium with Device Farm&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Testing on real mobile devices&lt;/p&gt; &lt;p&gt;Device Farm makes it possible for you to test apps on physical phones, tablets, and other devices in the cloud. For more information, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/devicefarm/latest/developerguide/\&quot;&gt;Device Farm Developer Guide&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    """
)

