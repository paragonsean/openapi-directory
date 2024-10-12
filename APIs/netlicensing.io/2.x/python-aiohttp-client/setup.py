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
    description="Labs64 NetLicensing RESTful API Test Center",
    author_email="",
    url="",
    keywords=["OpenAPI", "Labs64 NetLicensing RESTful API Test Center"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    The Labs64 &lt;a href&#x3D;&#39;https://netlicensing.io/wiki/restful-api&#39; target&#x3D;&#39;_blank&#39;&gt;NetLicensing RESTful API&lt;/a&gt; gives you access to NetLicensing’s core features.&lt;br/&gt;&lt;br/&gt;&lt;strong&gt;Authentication&lt;/strong&gt;&lt;br/&gt;You authenticate to the NetLicensing API by providing your account credentials or simply use our demo account - &lt;code&gt;demo:demo&lt;/code&gt;&lt;br/&gt;&lt;br/&gt;Find out more about Labs64 NetLicensing at &lt;a href&#x3D;&#39;https://netlicensing.io&#39; target&#x3D;&#39;_blank&#39;&gt;netlicensing.io&lt;/a&gt;
    """
)

