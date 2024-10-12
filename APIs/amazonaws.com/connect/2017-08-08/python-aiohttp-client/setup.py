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
    description="Amazon Connect Service",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "Amazon Connect Service"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;p&gt;Amazon Connect is a cloud-based contact center solution that you use to set up and manage a customer contact center and provide reliable customer engagement at any scale.&lt;/p&gt; &lt;p&gt;Amazon Connect provides metrics and real-time reporting that enable you to optimize contact routing. You can also resolve customer issues more efficiently by getting customers in touch with the appropriate agents.&lt;/p&gt; &lt;p&gt;There are limits to the number of Amazon Connect resources that you can create. There are also limits to the number of requests that you can make per second. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html\&quot;&gt;Amazon Connect Service Quotas&lt;/a&gt; in the &lt;i&gt;Amazon Connect Administrator Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;You can connect programmatically to an Amazon Web Services service by using an endpoint. For a list of Amazon Connect endpoints, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/connect_region.html\&quot;&gt;Amazon Connect Endpoints&lt;/a&gt;.&lt;/p&gt;
    """
)

