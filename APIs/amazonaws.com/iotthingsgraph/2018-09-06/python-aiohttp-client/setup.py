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
    description="AWS IoT Things Graph",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "AWS IoT Things Graph"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;fullname&gt;AWS IoT Things Graph&lt;/fullname&gt; &lt;p&gt;AWS IoT Things Graph provides an integrated set of tools that enable developers to connect devices and services that use different standards, such as units of measure and communication protocols. AWS IoT Things Graph makes it possible to build IoT applications with little to no code by connecting devices and services and defining how they interact at an abstract level.&lt;/p&gt; &lt;p&gt;For more information about how AWS IoT Things Graph works, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/thingsgraph/latest/ug/iot-tg-whatis.html\&quot;&gt;User Guide&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;The AWS IoT Things Graph service is discontinued.&lt;/p&gt;
    """
)

