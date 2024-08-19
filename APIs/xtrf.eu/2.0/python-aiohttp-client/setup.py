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
    description="XTRF Home Portal API",
    author_email="",
    url="",
    keywords=["OpenAPI", "XTRF Home Portal API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    XTRF Home Portal API enables you to perform operations on Projects, Quotes, Customers, Vendors etc. as a XTRF Home Portal user. &lt;br&gt;The documentation is generated from OpenAPI specification 3.0 available &lt;a href&#x3D;\&quot;/home-api/openapi.json\&quot;&gt;here&lt;/a&gt; &lt;br&gt;   The API client/consumer code may be easily generated in 60+ programming languages using an open source code generator available at the time of writing this documentation at &lt;a href&#x3D;&#39;https://editor.swagger.io/&#39;&gt;https://editor.swagger.io/&lt;/a&gt; Thank you for using XTRF Application Programming interface (XTRF API). By using the API you agree to the terms below. If you disagree with any of these terms, XTRF does not grant you a license to use the XTRF API. XTRF reserves the right to update and change these terms from time to time without a prior notice of API users. You can always find the most recent version of these terms here: 
    """
)

