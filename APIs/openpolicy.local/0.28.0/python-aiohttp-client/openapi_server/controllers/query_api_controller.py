from typing import List, Dict
from aiohttp import web

from openapi_server.models.model400 import Model400
from openapi_server.models.model404 import Model404
from openapi_server.models.post_compile200_response import PostCompile200Response
from openapi_server import util


async def get_query(request: web.Request, q, pretty=None, explain=None, metrics=None) -> web.Response:
    """Execute an ad-hoc query (simple)

    This API endpoint returns bindings for the variables in the query.  For more complex JSON queries, use &#x60;POST /v1/query&#x60; instead.

    :param q: The [URL-encoded](https://www.w3schools.com/tags/ref_urlencode.ASP) ad-hoc query to execute.
    :type q: str
    :param pretty: If true, response will be in a human-readable format.
    :type pretty: bool
    :param explain: If set to *full*, response will include query explanations in addition to the result.
    :type explain: str
    :param metrics: If true, compiler performance metrics will be returned in the response.
    :type metrics: bool

    """
    return web.Response(status=200)


async def post_query(request: web.Request, body, pretty=None, explain=None, metrics=None) -> web.Response:
    """Execute an ad-hoc query (complex)

    This API endpoint returns bindings for the variables in the query.  For simpler JSON queries, you may use &#x60;GET /v1/query&#x60; instead.

    :param body: The test of the query (in JSON format)
    :type body: Dict[str, ]
    :param pretty: If true, response will be in a human-readable format.
    :type pretty: bool
    :param explain: If set to *full*, response will include query explanations in addition to the result.
    :type explain: str
    :param metrics: If true, compiler performance metrics will be returned in the response.
    :type metrics: bool

    """
    return web.Response(status=200)


async def post_simple_query(request: web.Request, body, pretty=None) -> web.Response:
    """Execute a simple query

    This API queries the document at */data/system/main* by default (however, you can [configure OPA](https://www.openpolicyagent.org/docs/latest/configuration/) to use a different path to serve these queries). That document defines the response. For example, use the following in &#x60;PUT /v1/policies/{path}&#x60;) to define a rule that will produce a value for the */data/system/main* document:    &#x60;&#x60;&#x60;yaml   package system   main &#x3D; msg {     msg :&#x3D; sprintf(\&quot;hello, %v\&quot;, input.user)   }   &#x60;&#x60;&#x60;  The server will return a *not found* (404) response if */data/system/main* is undefined.

    :param body: The text of the input document (in JSON format)
    :type body: Dict[str, ]
    :param pretty: If true, response will be in a human-readable format.
    :type pretty: bool

    """
    return web.Response(status=200)
