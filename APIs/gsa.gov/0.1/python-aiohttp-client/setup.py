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
    description="Discovery Market Research",
    author_email="discovery-18f@gsa.gov",
    url="",
    keywords=["OpenAPI", "Discovery Market Research"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;p&gt;This API drives the &lt;a href&#x3D;\&quot;https://discovery.gsa.gov\&quot;&gt;Discovery Market Research Tool&lt;/a&gt;. It contains information on the vendors that are part of the OASIS and OASIS Small Business contracting vehicles, such as their contracting history, their elligibility for contract awards, and their small business designations. To learn more about the tool, please visit &lt;a href&#x3D;\&quot;https://discovery.gsa.gov\&quot;&gt;Discovery&lt;/a&gt; or see the README on our &lt;a href&#x3D;\&quot;https://github.com/PSHCDevOps/discovery\&quot;&gt;GitHub repository&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;&lt;strong&gt;Please note that the base path for this API is &lt;code&gt;https://api.data.gov/gsa/discovery/&lt;/code&gt;&lt;/strong&gt;&lt;/p&gt; &lt;p&gt;It requires an API key, obtainable at &lt;a href&#x3D;\&quot;http://api.data.gov/\&quot;&gt;api.data.gov&lt;/a&gt;. It must be passed in the &lt;code&gt;api_key&lt;/code&gt; parameter with each request.&lt;/p&gt;
    """
)

