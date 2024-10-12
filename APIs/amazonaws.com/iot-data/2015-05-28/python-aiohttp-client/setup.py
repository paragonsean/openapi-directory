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
    description="AWS IoT Data Plane",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "AWS IoT Data Plane"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;fullname&gt;IoT data&lt;/fullname&gt; &lt;p&gt;IoT data enables secure, bi-directional communication between Internet-connected things (such as sensors, actuators, embedded devices, or smart appliances) and the Amazon Web Services cloud. It implements a broker for applications and things to publish messages over HTTP (Publish) and retrieve, update, and delete shadows. A shadow is a persistent representation of your things and their state in the Amazon Web Services cloud.&lt;/p&gt; &lt;p&gt;Find the endpoint address for actions in IoT data by running this CLI command:&lt;/p&gt; &lt;p&gt; &lt;code&gt;aws iot describe-endpoint --endpoint-type iot:Data-ATS&lt;/code&gt; &lt;/p&gt; &lt;p&gt;The service name used by &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html\&quot;&gt;Amazon Web ServicesSignature Version 4&lt;/a&gt; to sign requests is: &lt;i&gt;iotdevicegateway&lt;/i&gt;.&lt;/p&gt;
    """
)

