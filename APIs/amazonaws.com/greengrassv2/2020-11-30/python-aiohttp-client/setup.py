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
    description="AWS IoT Greengrass V2",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "AWS IoT Greengrass V2"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;p&gt;IoT Greengrass brings local compute, messaging, data management, sync, and ML inference capabilities to edge devices. This enables devices to collect and analyze data closer to the source of information, react autonomously to local events, and communicate securely with each other on local networks. Local devices can also communicate securely with Amazon Web Services IoT Core and export IoT data to the Amazon Web Services Cloud. IoT Greengrass developers can use Lambda functions and components to create and deploy applications to fleets of edge devices for local operation.&lt;/p&gt; &lt;p&gt;IoT Greengrass Version 2 provides a new major version of the IoT Greengrass Core software, new APIs, and a new console. Use this API reference to learn how to use the IoT Greengrass V2 API operations to manage components, manage deployments, and core devices.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/greengrass/v2/developerguide/what-is-iot-greengrass.html\&quot;&gt;What is IoT Greengrass?&lt;/a&gt; in the &lt;i&gt;IoT Greengrass V2 Developer Guide&lt;/i&gt;.&lt;/p&gt;
    """
)

