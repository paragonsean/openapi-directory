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
    description="AWS Well-Architected Tool",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "AWS Well-Architected Tool"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;fullname&gt;Well-Architected Tool&lt;/fullname&gt; &lt;p&gt;This is the &lt;i&gt;Well-Architected Tool API Reference&lt;/i&gt;. The WA Tool API provides programmatic access to the &lt;a href&#x3D;\&quot;http://aws.amazon.com/well-architected-tool\&quot;&gt;Well-Architected Tool&lt;/a&gt; in the &lt;a href&#x3D;\&quot;https://console.aws.amazon.com/wellarchitected\&quot;&gt;Amazon Web Services Management Console&lt;/a&gt;. For information about the Well-Architected Tool, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/wellarchitected/latest/userguide/intro.html\&quot;&gt;Well-Architected Tool User Guide&lt;/a&gt;.&lt;/p&gt;
    """
)

