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
    description="Account API",
    author_email="",
    url="",
    keywords=["OpenAPI", "Account API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    The &lt;b&gt;Account API&lt;/b&gt; gives sellers the ability to configure their eBay seller accounts, including the seller&#39;s policies (eBay business policies and seller-defined custom policies), opt in and out of eBay seller programs, configure sales tax tables, and get account information.  &lt;br/&gt;&lt;br/&gt;For details on the availability of the methods in this API, see &lt;a href&#x3D;\&quot;/api-docs/sell/account/overview.html#requirements\&quot;&gt;Account API requirements and restrictions&lt;/a&gt;.
    """
)

