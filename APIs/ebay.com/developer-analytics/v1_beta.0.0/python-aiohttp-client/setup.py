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
    description="Analytics API",
    author_email="",
    url="",
    keywords=["OpenAPI", "Analytics API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    The &lt;b&gt;Analytics API&lt;/b&gt; retrieves call-limit data and the quotas that are set for the RESTful APIs and the legacy Trading API.  &lt;br&gt;&lt;br&gt;Responses from calls made to &lt;b&gt;getRateLimits&lt;/b&gt; and &lt;b&gt;getUerRateLimits&lt;/b&gt; include a list of the applicable resources and the \&quot;call limit\&quot;, or quota, that is set for each resource. In addition to quota information, the response also includes the number of remaining calls available before the limit is reached, the time remaining before the quota resets, and the length of the \&quot;time window\&quot; to which the quota applies.  &lt;br&gt;&lt;br&gt;The &lt;b&gt;getRateLimits&lt;/b&gt; and &lt;b&gt;getUserRateLimits&lt;/b&gt; methods retrieve call-limit information for either an application or user, respectively, and each method must be called with an appropriate OAuth token. That is, &lt;b&gt;getRateLimites&lt;/b&gt; requires an access token generated with a client credentials grant and &lt;b&gt;getUserRateLimites&lt;/b&gt; requires an access token generated with an authorization code grant. For more information, see &lt;a href&#x3D;\&quot;/api-docs/static/oauth-tokens.html\&quot;&gt;OAuth tokens&lt;/a&gt;.  &lt;br&gt;&lt;br&gt;Users can analyze the response data to see whether or not a limit might be reached, and from that determine if any action needs to be taken (such as programmatically throttling their request rate). For more on call limits, see &lt;a href&#x3D;\&quot;https://developer.ebay.com/support/app-check \&quot; target&#x3D;\&quot;_blank\&quot;&gt;Compatible Application Check&lt;/a&gt;.
    """
)

