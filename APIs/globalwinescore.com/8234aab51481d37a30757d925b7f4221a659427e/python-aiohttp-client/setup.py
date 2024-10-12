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
    description="GlobalWineScore API Documentation",
    author_email="",
    url="",
    keywords=["OpenAPI", "GlobalWineScore API Documentation"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
      The GlobalWineScore API is designed as a RESTful API, providing several resources and methods depending on your usage plan.  For further information please refer to &lt;a href&#x3D;\&quot;https://www.globalwinescore.com/plans\&quot; target&#x3D;\&quot;_blank\&quot;&gt;our plans&lt;/a&gt;.  # Authentication The API uses token-based authentication. In order to authenticate your requests, you need to include a specific header in each of your requests:  &#x60;&#x60;&#x60; Authorization: Token {YOUR-API-TOKEN} &#x60;&#x60;&#x60; The word &lt;b&gt;Token&lt;/b&gt; must be written. Your requests must also use the &lt;b&gt;HTTPS&lt;/b&gt; protocol.  If you don&#39;t have a token yet, you need to apply for one [here](https://www.globalwinescore.com/api/).  Your personal token can be found under the &lt;a href&#x3D;\&quot;https://www.globalwinescore.com/account/api/\&quot; target&#x3D;\&quot;_blank\&quot;&gt;My account &gt; API&lt;/a&gt; section of the GlobalWineScore website  # Format The API provides several rendering formats which you can control using the &#x60;Accept&#x60; header or &#x60;format&#x60; query parameter.  - JSON (default): no header or &#x60;Accept: application/json&#x60; - XML: &#x60;Accept: application/xml&#x60; # Rate limiting For API requests, the rate limit allows for up to 10 requests per minute.  # Error handling  Whether a request succeeded is indicated by the HTTP status code. A 2xx status code indicates success, whereas a 4xx status code indicates failure.  When a request fails, the response body is still JSON, but always contains a &#x60;detail&#x60; field with a description of the error, which you can inspect for debugging.  For example, trying to access the API without proper authentication will return code 403 along with the message:  &#x60;{\&quot;detail\&quot;: \&quot;Authentication credentials were not provided.\&quot;}&#x60;  Found a bug ? send us an email at &lt;a href&#x3D;\&quot;mailto:api@globalwinescore.com\&quot;&gt;api@globalwinescore.com&lt;/a&gt;  # Ordering  At the moment, GlobalWineScores may be sorted by &#x60;date&#x60; and &#x60;score&#x60;. Use \&quot;-\&quot; to sort in descending order.  # Continuous synchronization  If you need to synchronize your database with our API, you can query our API using &#x60;?ordering&#x3D;-date&#x60; to get the newest scores first, which means you won&#39;t have to crawl the whole catalog every time :-)  # Quick search interface If you need to search our catalog (e.g. to align it with yours), we&#39;re providing you with a handy interface accessible here: &lt;a href&#x3D;\&quot;https://api.globalwinescore.com/search/\&quot; target&#x3D;\&quot;_blank\&quot;&gt;https://api.globalwinescore.com/search/&lt;/a&gt;  You need to be logged in (email/password) to access this page, but other than that you can share it with anyone in your team and start searching right away !  # Resources  The details about available endpoints can be found below. You can click on each endpoint to find information about their parameters. 
    """
)

