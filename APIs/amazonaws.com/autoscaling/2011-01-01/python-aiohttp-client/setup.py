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
    description="Auto Scaling",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "Auto Scaling"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;fullname&gt;Amazon EC2 Auto Scaling&lt;/fullname&gt; &lt;p&gt;Amazon EC2 Auto Scaling is designed to automatically launch and terminate EC2 instances based on user-defined scaling policies, scheduled actions, and health checks.&lt;/p&gt; &lt;p&gt;For more information, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/userguide/\&quot;&gt;Amazon EC2 Auto Scaling User Guide&lt;/a&gt; and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/ec2/APIReference/Welcome.html\&quot;&gt;Amazon EC2 Auto Scaling API Reference&lt;/a&gt;.&lt;/p&gt;
    """
)

