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
    description="AWS SimSpace Weaver",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "AWS SimSpace Weaver"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;p&gt;SimSpace Weaver (SimSpace Weaver) is a managed service that you can use to build and operate large-scale spatial simulations in the Amazon Web Services Cloud. For example, you can create a digital twin of a city, crowd simulations with millions of people and objects, and massively multiplayer games with hundreds of thousands of connected players. For more information about SimSpace Weaver, see the &lt;i&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/simspaceweaver/latest/userguide/\&quot;&gt;SimSpace Weaver User Guide&lt;/a&gt; &lt;/i&gt;.&lt;/p&gt; &lt;p&gt;This API reference describes the API operations and data types that you can use to communicate directly with SimSpace Weaver.&lt;/p&gt; &lt;p&gt;SimSpace Weaver also provides the SimSpace Weaver app SDK, which you use for app development. The SimSpace Weaver app SDK API reference is included in the SimSpace Weaver app SDK documentation. This documentation is part of the SimSpace Weaver app SDK distributable package.&lt;/p&gt;
    """
)

