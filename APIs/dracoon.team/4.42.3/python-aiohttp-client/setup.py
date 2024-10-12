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
    description="DRACOON API",
    author_email="",
    url="",
    keywords=["OpenAPI", "DRACOON API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    REST Web Services for DRACOON&lt;br&gt;&lt;br&gt;This page provides an overview of all available and documented DRACOON APIs, which are grouped by tags.&lt;br&gt;Each tag provides a collection of APIs that are intended for a specific area of the DRACOON.&lt;br&gt;&lt;br&gt;&lt;a title&#x3D;&#39;Developer Information&#39; href&#x3D;&#39;https://developer.dracoon.com&#39;&gt;Developer Information&lt;/a&gt;&amp;emsp;&amp;emsp;&lt;a title&#x3D;&#39;Get SDKs on GitHub&#39; href&#x3D;&#39;https://github.com/dracoon&#39;&gt;Get SDKs on GitHub&lt;/a&gt;&lt;br&gt;&lt;br&gt;&lt;a title&#x3D;&#39;Terms of service&#39; href&#x3D;&#39;https://www.dracoon.com/terms/general-terms-and-conditions/&#39;&gt;Terms of service&lt;/a&gt;
    """
)

