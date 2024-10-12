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
    description="Yodlee Core APIs",
    author_email="developer@yodlee.com",
    url="",
    keywords=["OpenAPI", "Yodlee Core APIs"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    This file describes the Yodlee Platform APIs using the swagger notation. You can use this swagger file to generate client side SDKs to the Yodlee Platform APIs for many different programming languages. Yodlee supports the Java SDK and it is available &lt;a href&#x3D;\&quot;https://developer.yodlee.com/java-sdk-overview \&quot;&gt;here&lt;/a&gt;. You can generate a client SDK for Python, Java, JavaScript, PHP or other languages according to your development needs. For more details about the APIs, refer to &lt;a href&#x3D;\&quot;https://developer.yodlee.com/docs/api/1.1/Overview\&quot;&gt;Yodlee API v1.1 - Overview&lt;/a&gt;.
    """
)

