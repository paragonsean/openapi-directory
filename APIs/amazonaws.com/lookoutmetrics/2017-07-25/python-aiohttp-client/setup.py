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
    description="Amazon Lookout for Metrics",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "Amazon Lookout for Metrics"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    This is the &lt;i&gt;Amazon Lookout for Metrics API Reference&lt;/i&gt;. For an introduction to the service with tutorials for getting started, visit &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lookoutmetrics/latest/dev\&quot;&gt;Amazon Lookout for Metrics Developer Guide&lt;/a&gt;.
    """
)

