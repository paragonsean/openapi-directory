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
    description="goog.io | Unoffical Google Search API",
    author_email="support@goog.io",
    url="",
    keywords=["OpenAPI", "goog.io | Unoffical Google Search API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    # Intoduction  This is the OpenAPI V3 documentation for https://api.goog.io  An API to perform Google Searches. Extremely fast and accurate. Zero proxies. Clean USA IPs.  Simple to use API, but advance enough to support special parameters such as languages, country and geographic locality.  Googio is the ultimate search API for Google Searches, Google News, and Google SERP. # Docs  &gt; An Unofficial Google Search API  An API to perform Google Searches. Extremely fast and accurate. Zero proxies. Clean USA IPs.  Simple to use API, but advance enough to support special parameters such as languages, country and geographic locality.  # Example Code   Check out [Github repo](https://github.com/googio/googio_examples) for example code for calling the API with various languages.  # Authentication  ### API Key  Optional API key for authenticated access. Note that we use \&quot;API key\&quot; interchangably in these docs.  Authenticated requests must include an &#x60;apikey&#x60; header containing your subscription&#39;s API Key.  | Security Schema Type | Header Name | Example Token | | --- | --- | --- | | API Key | &#x60;apikey&#x60; | c5bfb018-ab46-4e61-9271-4ec7e9c04a6e |  In the following example, &#x60;YOU_APIKEY&#x60; represents the auth token for your account.  &#x60;&#x60;&#x60; curl --header &#39;apikey: YOU_APIKEY&#39; &#x60;&#x60;&#x60;  You can view and manage your API keys in the [Dashboard](/dashboard).  Be sure to keep your API keys secure. Do not share them in publicly accessible areas such as GitHub, client-side code, and so forth.  Also note that all API requests must be made over **HTTPS**. Calls made over plain HTTP will attempt to be automatically upgraded to HTTPS, though this use cases is discouraged.   ## Rate Limits  API requests may be rate limited depending on your subscription plan and traffic patterns. The following response headers will be present in these cases:  | Header | Description | | ------ | ----------- | | &#x60;X-RateLimit-Limit&#x60; | The maximum number of requests that the consumer is permitted to make. | | &#x60;X-RateLimit-Remaining&#x60; | The number of requests remaining in the current rate limit window. | | &#x60;X-RateLimit-Reset&#x60; | The time at which the current rate limit window resets in UTC epoch seconds. |  When the rate limit is **exceeded**, an error is returned with the status \&quot;**429 Too Many Requests**\&quot;:  &#x60;&#x60;&#x60;json {   \&quot;error\&quot;: {     \&quot;code\&quot;: \&quot;too_many_requests\&quot;,     \&quot;message\&quot;: \&quot;Rate limit exceeded\&quot;   } } &#x60;&#x60;&#x60;    ## Errors  This API uses conventional HTTP response codes to indicate the success or failure of API requests. In general: Codes in the &#x60;2xx&#x60; range indicate success. Codes in the &#x60;4xx&#x60; range indicate an error that failed given the information provided (e.g., a required parameter was omitted, endpoint not found, etc.). Codes in the &#x60;5xx&#x60; range indicate an error with our API (these are rare).   
    """
)

