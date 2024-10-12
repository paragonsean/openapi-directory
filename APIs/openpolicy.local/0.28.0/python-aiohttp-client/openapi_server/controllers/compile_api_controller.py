from typing import List, Dict
from aiohttp import web

from openapi_server.models.model400 import Model400
from openapi_server.models.post_compile200_response import PostCompile200Response
from openapi_server import util


async def post_compile(request: web.Request, pretty=None, explain=None, metrics=None, instrument=None, body=None) -> web.Response:
    """Compile

    This API endpoint allows you to partially evaluate Rego queries and obtain a simplified version of the policy. The example below assumes that OPA has been given the following policy (use &#x60;PUT /v1/policies/{path}&#x60;):  &#x60;&#x60;&#x60;yaml package example allow {   input.subject.clearance_level &gt;&#x3D; data.reports[_].clearance_level } &#x60;&#x60;&#x60; Compile API **request body** so that it contain the following fields:  | Field | Type | Required | Description | | --- | --- | --- | --- | | &#x60;query&#x60; | &#x60;string&#x60; | Yes | The query to partially evaluate and compile. | | &#x60;input&#x60; | &#x60;any&#x60; | No | The input document to use during partial evaluation (default: undefined). | | &#x60;unknowns&#x60; | &#x60;array[string]&#x60; | No | The terms to treat as unknown during partial evaluation (default: &#x60;[\&quot;input\&quot;]&#x60;]). |  For example:  &#x60;&#x60;&#x60;json {   \&quot;query\&quot;: \&quot;data.example.allow &#x3D;&#x3D; true\&quot;,   \&quot;input\&quot;: {     \&quot;subject\&quot;: {       \&quot;clearance_level\&quot;: 4     }   },   \&quot;unknowns\&quot;: [     \&quot;data.reports\&quot;     ] } &#x60;&#x60;&#x60; ### Partial evaluation In some cases, the result of partial valuation is a conclusive, unconditional answer. See [the guidance](https://www.openpolicyagent.org/docs/latest/rest-api/#unconditional-results-from-partial-evaluation) for details.

    :param pretty: If true, response will be in a human-readable format.
    :type pretty: bool
    :param explain: If set to *full*, response will include query explanations in addition to the result.
    :type explain: str
    :param metrics: If true, compiler performance metrics will be returned in the response.
    :type metrics: bool
    :param instrument: If true, response will return additional performance metrics in addition to the result and the standard metrics.  **Caution:** This can add significant overhead to query evaluation. The recommendation is to only use this parameter if you are debugging a performance problem.
    :type instrument: bool
    :param body: The query (in JSON format)
    :type body: Dict[str, ]

    """
    return web.Response(status=200)
