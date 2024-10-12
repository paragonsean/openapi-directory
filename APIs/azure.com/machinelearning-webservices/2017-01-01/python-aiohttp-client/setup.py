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
    description="Azure ML Web Services Management Client",
    author_email="",
    url="",
    keywords=["OpenAPI", "Azure ML Web Services Management Client"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    These APIs allow end users to operate on Azure Machine Learning Web Services resources. They support the following operations:&lt;ul&gt;&lt;li&gt;Create or update a web service&lt;/li&gt;&lt;li&gt;Get a web service&lt;/li&gt;&lt;li&gt;Patch a web service&lt;/li&gt;&lt;li&gt;Delete a web service&lt;/li&gt;&lt;li&gt;Get All Web Services in a Resource Group &lt;/li&gt;&lt;li&gt;Get All Web Services in a Subscription&lt;/li&gt;&lt;li&gt;Get Web Services Keys&lt;/li&gt;&lt;/ul&gt;
    """
)

