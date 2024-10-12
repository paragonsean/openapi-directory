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
    description="BulkSMS JSON REST API",
    author_email="",
    url="",
    keywords=["OpenAPI", "BulkSMS JSON REST API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    ## Overview  The JSON REST API allows you to submit and receive [BulkSMS](https://www.bulksms.com/) messages. You can also get access to past messages and see your account profile.  The base URL to use for this service is &#x60;https://api.bulksms.com/v1&#x60;.  The base URL cannot be used on its own; you must append a path that identifies an operation and you may have to specify some path parameters as well.  [Click here](/developer/) to go to the main BulkSMS developer site.  In order to give you an idea on how the API can be used, some JSON snippets are provided below.  Have a look at the [messages section](#tag/Message) for more information.  Probably the most simple example  &#x60;&#x60;&#x60; {     \&quot;to\&quot;: \&quot;+27001234567\&quot;,     \&quot;body\&quot;: \&quot;Hello World!\&quot; } &#x60;&#x60;&#x60;   You can send unicode automatically using the &#x60;auto-unicode&#x60; query parameter.  Alternatively, you can specify &#x60;UNICODE&#x60; for the &#x60;encoding&#x60; property in the request body.  Please note: when &#x60;auto-unicode&#x60; is specified and the value of the &#x60;encoding&#x60; property is &#x60;UNICODE&#x60;, the message will always be sent as &#x60;UNICODE&#x60;.  Here is an example that sets the &#x60;encoding&#x60; explicitly  &#x60;&#x60;&#x60; {   \&quot;to\&quot;: \&quot;+27001234567\&quot;,   \&quot;body\&quot;: \&quot;Dobrá práce! Jak se máš?\&quot;,   \&quot;encoding\&quot;: \&quot;UNICODE\&quot; } &#x60;&#x60;&#x60;  You can also specify a from number  &#x60;&#x60;&#x60; {     \&quot;from\&quot;: \&quot;+27007654321\&quot;,     \&quot;to\&quot;: \&quot;+27001234567\&quot;,     \&quot;body\&quot;: \&quot;Hello World!\&quot; } &#x60;&#x60;&#x60;  Similar to above, but repliable  &#x60;&#x60;&#x60; {     \&quot;from\&quot;: { \&quot;type\&quot;: \&quot;REPLIABLE\&quot; },     \&quot;to\&quot;: \&quot;+27001234567\&quot;,     \&quot;body\&quot;: \&quot;Hello World!\&quot; } &#x60;&#x60;&#x60;  A message to a group called Everyone  &#x60;&#x60;&#x60; {     \&quot;to\&quot;: { \&quot;type\&quot;: \&quot;GROUP\&quot;, \&quot;name\&quot;: \&quot;Everyone\&quot; },     \&quot;body\&quot;: \&quot;Hello World!\&quot; } &#x60;&#x60;&#x60;  A message to multiple recipients  &#x60;&#x60;&#x60; {     \&quot;to\&quot;: [\&quot;+27001234567\&quot;, \&quot;+27002345678\&quot;, \&quot;+27003456789\&quot;],     \&quot;body\&quot;: \&quot;Happy Holidays!\&quot; } &#x60;&#x60;&#x60;  Sending more than one message in the same request  &#x60;&#x60;&#x60; [     {         \&quot;to\&quot;: \&quot;+27001234567\&quot;,         \&quot;body\&quot;: \&quot;Hello World!\&quot;     },     {         \&quot;to\&quot;: \&quot;+27002345678\&quot;,         \&quot;body\&quot;: \&quot;Hello Universe!\&quot;     } ] &#x60;&#x60;&#x60;  **The insecure base URL &#x60;http://api.bulksms.com/v1&#x60; is deprecated** and may in future result in a &#x60;301&#x60; redirect response, or insecure requests may be rejected outright. Please use the secure (&#x60;https&#x60;) URI above.  ### HTTP Content Type  All API methods expect requests to supply a &#x60;Content-Type&#x60; header with the value &#x60;application/json&#x60;. All responses will have the &#x60;Content-Type&#x60; header set to &#x60;application/json&#x60;.  ### JSON Formatting  You are advised to format your JSON resources according to strict JSON format rules. While the API does attempt to parse strictly invalid JSON documents, doing so may lead to incorrect interpretation and unexpected results.  Good JSON libraries will produce valid JSON suitable for submission, but if you are manually generating the JSON text, be careful to follow the JSON format. This include correct escaping of control characters and double quoting of property names.  See the [JSON specification](https://tools.ietf.org/html/rfc4627) for further information.  ### Date Formatting  Dates are formatted according to ISO-8601, such as &#x60;1970-01-01T10:00:00+01:00&#x60; for 1st January 1970, 10AM UTC+1.  See the [Wikipedia ISO 8601 reference](https://en.wikipedia.org/wiki/ISO_8601) for further information.  Specifically, calendar dates are formatted with the &#39;extended&#39; format &#x60;YYYY-MM-DD&#x60;. Basic format, week dates and ordinal dates are not supported. Times are also formatted in the &#39;extended&#39; format &#x60;hh:mm:ss&#x60;. Hours, minutes and seconds are mandatory. Offset from UTC must be provided; this is to ensure that there is no misunderstanding regarding times provided to the API.  The format we look for is &#x60;yyyy-MM-ddThh:mm:ss[Z|[+-]hh:mm]&#x60;  Examples of valid date/times are&#x60;2011-12-31T12:00:00Z&#x60; &#x60;2011-12-31T12:00:00+02:00&#x60;  ### Entity Format Modifications  It is expected that over time some changes will be made to the request and response formats of various methods available in the API. Where possible, these will be implemented in a backwards compatible way. To make this possible you are required to ignore unknown properties. This enables the addition of information in response documents while maintaining compatibility with older clients.  ### Optional Request Entity Properties  There are many instances where requests can be made without having to specify every single property allowable in the request format. Any such optional properties are noted as such in the documentation and their default value is noted. 
    """
)

