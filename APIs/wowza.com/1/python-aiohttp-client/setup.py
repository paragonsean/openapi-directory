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
    description="Wowza Streaming Cloud REST API Reference Documentation",
    author_email="",
    url="",
    keywords=["OpenAPI", "Wowza Streaming Cloud REST API Reference Documentation"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
     # About the REST API  The Wowza Streaming Cloud&lt;sup&gt;TM&lt;/sup&gt; REST API (application programming interface) offers complete programmatic control over live streams, transcoders, stream sources, and stream targets. Anything you can do in the Wowza Streaming Cloud UI can also be achieved by making HTTP-based requests to cloud-based servers through the REST API.  The Wowza Streaming Cloud REST API features *cross-origin resource sharing*, or CORS. CORS is a [W3C specification](https://www.w3.org/TR/cors/) that provides headers in HTTP requests to enable a web server to safely make a network request to another domain.  In order to protect shared resources, the Wowza Streaming Cloud REST API is subject to limits. For details, see [Wowza Streaming Cloud REST API limits](https://www.wowza.com/docs/wowza-streaming-cloud-rest-api-limits). # About this documentation This reference documentation is based on the open-source [Swagger framework](http://swagger.io/specification/). It allows you to view the operations, parameters, and request and reponse schemas for every resource. Request samples are presented in cURL (Shell) and JavaScript; some samples also include just the JSON object. Response samples are all JSON.  For more information and examples on using the Wowza Streaming Cloud REST API, see our [library of Wowza Streaming Cloud REST API technical articles](https://www.wowza.com/docs/wowza-streaming-cloud-rest-api).  # Query requirements The Wowza Streaming Cloud REST API uses HTTP requests to retrieve data from cloud-based servers. Requests must contain proper JSON, two authentication keys, and the correct version number in the base path.  ## JSON The Wowza Streaming Cloud REST API uses the [JSON API specification](http://jsonapi.org/format/) to request and return data. This means requests must include the header &#x60;Content-Type: application/json&#x60; and must include a single resource object in JSON format as primary data.  Responses include HTTP status codes that indicate whether the query was successful. If there was an error, a description explains the problem so that you can fix it and try again.  ## Authentication Requests to the Wowza Streaming Cloud REST API must be authenticated with two keys: an API key and an access key. Each key is a 64-character alphanumeric string that you can find on the **API Access** page in Wowza Streaming Cloud.  Use the &#x60;wsc-api-key&#x60; and &#x60;wsc-access-key&#x60; headers to authenticate requests, like this (in cURL):  &#x60;&#x60;&#x60;bash curl -H &#39;wsc-api-key: [64-character-api-key-goes-here]&#39; -H &#39;wsc-access-key: [64-character-access-key-goes-here]&#39; &#x60;&#x60;&#x60;  &lt;!-- ReDoc-Inject: &lt;security-definitions&gt; --&gt;  ## Version The Wowza Streaming Cloud API is currently at version 1.0.0. Use &#x60;v1&#x60; in your base path in every request, like this path to the live_streams endpoint: &#x60;&#x60;&#x60; https://api.cloud.wowza.com/api/v1/live_streams &#x60;&#x60;&#x60; ## Example query Here is a complete example POST request, in cURL, with proper JSON syntax, headers, authentication, and version information: &#x60;&#x60;&#x60;bash curl -H &#39;wsc-api-key: [64-character-api-key-goes-here]&#39; -H &#39;wsc-access-key: [64-character-access-key-goes-here]&#39;   -H &#39;Content-Type: application/json&#39; -X POST -d &#39;{     \&quot;live_stream\&quot;: {       \&quot;name\&quot;: \&quot;My live Stream\&quot;,       \&quot;...\&quot;: \&quot;...\&quot;     }   }&#39; https://api.cloud.wowza.com/api/v1/live_streams &#x60;&#x60;&#x60; 
    """
)

