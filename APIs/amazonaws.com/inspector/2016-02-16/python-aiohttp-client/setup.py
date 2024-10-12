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
    description="Amazon Inspector",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "Amazon Inspector"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;fullname&gt;Amazon Inspector&lt;/fullname&gt; &lt;p&gt;Amazon Inspector enables you to analyze the behavior of your AWS resources and to identify potential security issues. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/inspector/latest/userguide/inspector_introduction.html\&quot;&gt; Amazon Inspector User Guide&lt;/a&gt;.&lt;/p&gt;
    """
)

