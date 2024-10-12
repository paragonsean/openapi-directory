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
    description="Open Targets Platform REST API",
    author_email="support@targetvalidation.org",
    url="",
    keywords=["OpenAPI", "Open Targets Platform REST API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    ### The Open Targets Platform REST API  The Open Targets Platform API (&#39;Application Programming Interface&#39;) allows programmatic retrieval of the Open Targets Platform data via a set of [REST](https://en.wikipedia.org/wiki/Representational_state_transfer) services.  You can make calls to the latest version of our API using the base URL &#x60;https://platform-api.opentargets.io/v3/platform&#x60;. Please make sure you use &#x60;https&#x60; instead of the unencrypted &#x60;http&#x60; calls, which we do not accept.  We list below the methods available to query our data directly from the API, followed by an interactive interface that you can use to try out the parameters and execute the REST-API calls.  For every request you create, the interactive interface will display both a [curl](https://curl.haxx.se/) command and a request URL that you can use to ensure you get the expected response before using your application or workflow.   Check our documentation for some [API tutorials](https://docs.targetvalidation.org/tutorials/api-tutorials) and [get in touch](mailto:support@targetvalidation.org) if you have any questions.  ### Available Methods  The available methods can be grouped in three types:  * __public__ - Methods that serve the core set of our data. These are stable and we fully supported them. * __private__ - Methods used by the web app to serve additional data not specific to our platform. These methods may change without notice and should be used with caution. * __utils__ - Methods to get statistics and technical data about our API.  ### Supported formats  The methods above are all available via a &#x60;GET&#x60; request, and will serve outputs as &#x60;JSON&#x60;.  Alternative output formats, such &#x60;xml&#x60;, &#x60;csv&#x60; and &#x60;tab&#x60;, are also available for some of the methods. However alternative output formats are not supported in interactive interface below where the response will be always in &#x60;JSON.  If you have complex queries with large number of parameters, you should use a &#x60;POST&#x60; request instead of  &#x60;GET&#x60;.  &#x60;POST&#x60; methods require a body encoded as &#x60;json&#x60;. When querying for a specific disease using the latest version of the API, your call would look like the example below:  &#x60;&#x60;&#x60;sh curl -X POST -d &#39;{\&quot;disease\&quot;:[\&quot;EFO_0000253\&quot;]}&#39; --header &#39;Content-Type: application/json&#39; https://platform-api.opentargets.io/v3/platform/public/evidence/filter &#x60;&#x60;&#x60; ### How to interpret a response  Each HTTPS response will serve data in headers and body. The headers will give you details about your query, such as how long it took to run.  In the body of the response, you will find the data you have requested for in &#x60;JSON&#x60; format. The [jq](https://stedolan.github.io/jq/) program is a useful tool to parse the json response while on the command line.  &#x60;&#x60;&#x60;sh curl https://platform-api.opentargets.io/v3/platform/public/association/filter\\?target\\&#x3D;ENSG00000157764 | jq &#x60;&#x60;&#x60;  We do not analyse the nature of any specific API queries except for the purposes of improving the performance of our API. Read more in our [privacy section](https://www.targetvalidation.org/terms_of_use#privacy).  How can we make the Open Targets Platform API more useful to you? Would you like additional methods to be implemented? Please [get in touch](mailto:support@targetvalidation.org) and send your suggestions. 
    """
)

