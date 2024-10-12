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
    description="EmailVerify",
    author_email="hello@paypi.dev",
    url="",
    keywords=["OpenAPI", "EmailVerify"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    OTP email verification API by PayPI. &lt;br/&gt;&lt;br/&gt; EmailVerify provides a simple way to verify email addresses. We send emails ourselves taking the burden of setting up email systems and tracking codes. &lt;br/&gt;&lt;br/&gt; To learn more about this API, check out [EmailVerify documentation](https://emailverify.paypi.dev/) &lt;br/&gt;&lt;br/&gt;  ## Authentication All requests to the EmailVerify API must be authenticated with an API Key. To get an API key, subscribe to the EmailVerify [here](https://app.paypi.dev/subscribe/c2VydmljZTo1OGQxZDNmMy05OWQ5LTQ3ZjYtOWJkNi02OWNkMTY1OGFmOWU&#x3D;).  \\ Set your &#x60;Authorization&#x60; header to &#x60;Bearer YOUR-API-KEY&#x60;.  &#x60;&#x60;&#x60; curl -H \&quot;Content-Type: application/json\&quot; \\ -H \&quot;Authorization: Bearer YOUR-API-KEY\&quot; \\ ... &#x60;&#x60;&#x60; 
    """
)

