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
    description="AWS Panorama",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "AWS Panorama"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;p&gt;&lt;fullname&gt;AWS Panorama&lt;/fullname&gt; &lt;p&gt; &lt;b&gt;Overview&lt;/b&gt; &lt;/p&gt; &lt;p&gt;This is the &lt;i&gt;AWS Panorama API Reference&lt;/i&gt;. For an introduction to the service, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/panorama/latest/dev/panorama-welcome.html\&quot;&gt;What is AWS Panorama?&lt;/a&gt; in the &lt;i&gt;AWS Panorama Developer Guide&lt;/i&gt;.&lt;/p&gt;&lt;/p&gt;
    """
)

