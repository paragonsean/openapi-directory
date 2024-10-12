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
    description="AWS ARC - Zonal Shift",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "AWS ARC - Zonal Shift"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;p&gt;This is the API Reference Guide for the zonal shift feature of Amazon Route 53 Application Recovery Controller. This guide is for developers who need detailed information about zonal shift API actions, data types, and errors.&lt;/p&gt; &lt;p&gt;Zonal shift is in preview release for Amazon Route 53 Application Recovery Controller and is subject to change.&lt;/p&gt; &lt;p&gt;Zonal shift in Route 53 ARC enables you to move traffic for a load balancer resource away from an Availability Zone. Starting a zonal shift helps your application recover immediately, for example, from a developer&#39;s bad code deployment or from an AWS infrastructure failure in a single Availability Zone, reducing the impact and time lost from an issue in one zone. &lt;/p&gt; &lt;p&gt;Supported AWS resources are automatically registered with Route 53 ARC. Resources that are registered for zonal shifts in Route 53 ARC are managed resources in Route 53 ARC. You can start a zonal shift for any managed resource in your account in a Region. At this time, you can only start a zonal shift for Network Load Balancers and Application Load Balancers with cross-zone load balancing turned off.&lt;/p&gt; &lt;p&gt;Zonal shifts are temporary. You must specify an expiration when you start a zonal shift, of up to three days initially. If you want to still keep traffic away from an Availability Zone, you can update the zonal shift and set a new expiration. You can also cancel a zonal shift, before it expires, for example, if you&#39;re ready to restore traffic to the Availability Zone.&lt;/p&gt; &lt;p&gt;For more information about using zonal shift, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/r53recovery/latest/dg/what-is-route53-recovery.html\&quot;&gt;Amazon Route 53 Application Recovery Controller Developer Guide&lt;/a&gt;.&lt;/p&gt;
    """
)

