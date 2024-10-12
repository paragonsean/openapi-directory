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
    description="API docs | logoraisr.com",
    author_email="support@logoraisr.com",
    url="",
    keywords=["OpenAPI", "API docs | logoraisr.com"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;p style&#x3D;\&quot;font-size:110%;\&quot;&gt;Dig into our logoraisr API reference documentation. We also offer an OpenAPI specification to allow easy integration into your systems. You can download the json file by clicking on the download button.&lt;p&gt;&lt;br&gt;&lt;p style&#x3D;\&quot;font-size:110%; font-weight:bold\&quot;&gt;OpenAPI 2.0 Validation Status&lt;/p&gt;&lt;img src&#x3D;\&quot;https://online.swagger.io/validator?url&#x3D;https://docs.logoraisr.com/\&quot;&gt;
    """
)

