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
    description="Fitbit Plus API",
    author_email="apiteam@twinehealth.com",
    url="",
    keywords=["OpenAPI", "Fitbit Plus API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    # Overview The Fitbit Plus API is a RESTful API. The requests and responses are formated according to the [JSON API](http://jsonapi.org/format/1.0/) specification.  In addition to this documentation, we also provide an [OpenAPI](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md) \&quot;yaml\&quot; file describing the API: [Fitbit Plus API Specification](swagger.yaml).  # Authentication Authentication for the Fitbit Plus API is based on the [OAuth 2.0 Authorization Framework](https://tools.ietf.org/html/rfc6749). Fitbit Plus currently supports grant types of **client_credentials** and **refresh_token**.  See [POST /oauth/token](#operation/createToken) for details on the request and response formats. &lt;!-- ReDoc-Inject: &lt;security-definitions&gt; --&gt;  ## Building Integrations We will provide customers with unique client credentials for each application/integration they build, allowing us to enforce appropriate access controls and monitor API usage. The client credentials will be scoped to the organization, and allow full access to all patients and related data within that organization.  These credentials are appropriate for creating an integration that does one of the following:  - background reporting/analysis  - synchronizing data with another system (such as an EMR)  The API credentials and oauth flows we currently support are **not** well suited for creating a user-facing application that allows a user (patient, coach, or admin) to login and have access to data which is appropriate to that specific user. It is possible to build such an application, but it is not possible to use Fitbit Plus as a federated identity provider. You would need to have a separate means of verifying a user&#39;s identity. We do not currently support the required password-based oauth flow to make this possible.  # Paging The Fitbit Plus API supports two different pagination strategies for GET collection endpoints.  #### Skip-based paging  Skip-based paging uses the query parameters &#x60;page[size]&#x60; and &#x60;page[number]&#x60; to specify the max number of resources returned and the page number. We default to skip-based paging if there are no page parameters. The response will include a &#x60;links&#x60; object containing links to the first, last, prev, and next pages of data.  If the contents of the collection change while you are iterating through the collection, you will see duplicate or missing documents. For example, if you are iterating through the &#x60;calender_event&#x60; resource via &#x60;GET /pub/calendar_event?sort&#x3D;start_at&amp;page[size]&#x3D;50&amp;page[number]&#x3D;1&#x60;, and a new &#x60;calendar_event&#x60; is created that has a &#x60;start_at&#x60; value before the first &#x60;calendar_event&#x60;, when you fetch the next page at &#x60;GET /pub/calendar_event?sort&#x3D;start_at&amp;page[size]&#x3D;50&amp;page[number]&#x3D;2&#x60;, the first entry in the second response will be a duplicate of the last entry in the first response.  #### Cursor-based paging Cursor-based paging uses the query parameters &#x60;page[limit]&#x60; and &#x60;page[after]&#x60; to specify the max number of entries returned and identify where to begin the next page. Add &#x60;page[limit]&#x60; to the parameters to use cursor-based paging. The response will include a &#x60;links&#x60; object containing a link to the next page of data, if the next page exists.  Cursor-based paging is not subject to duplication if new resources are added to the collection. For example, if you are iterating through the &#x60;calender_event&#x60; resource via &#x60;GET /pub/calendar_event?sort&#x3D;start_at&amp;page[limit]&#x3D;50&#x60;, and a new &#x60;calendar_event&#x60; is created that has a &#x60;start_at&#x60; value before the first &#x60;calendar_event&#x60;, you will not see a duplicate entry when you fetch the next page at &#x60;GET /pub/calendar_event?sort&#x3D;start_at&amp;page[limit]&#x3D;50&amp;page[after]&#x3D;&lt;cursor&gt;&#x60;.  We encourage the use of cursor-based paging for performance reasons.  In either form of paging, you can determine whether any resources were missed by comparing the number of fetched resources against &#x60;meta.count&#x60;. Set &#x60;page[size]&#x60; or &#x60;page[limit]&#x60; to 0 to get only the count.  It is not valid to mix the two strategies. 
    """
)

