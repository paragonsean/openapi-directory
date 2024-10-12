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
    description="Amazon AppIntegrations Service",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "Amazon AppIntegrations Service"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;p&gt;The Amazon AppIntegrations service enables you to configure and reuse connections to external applications.&lt;/p&gt; &lt;p&gt;For information about how you can use external applications with Amazon Connect, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/crm.html\&quot;&gt;Set up pre-built integrations&lt;/a&gt; and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-wisdom.html\&quot;&gt;Deliver information to agents using Amazon Connect Wisdom&lt;/a&gt; in the &lt;i&gt;Amazon Connect Administrator Guide&lt;/i&gt;.&lt;/p&gt;
    """
)

