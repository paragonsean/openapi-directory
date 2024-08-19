from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.metric_definition_collection import MetricDefinitionCollection
from openapi_server import util


async def metric_definitions_list(request: web.Request, resource_uri, api_version, filter=None) -> web.Response:
    """metric_definitions_list

    Lists the metric definitions for the resource.

    :param resource_uri: The identifier of the resource.
    :type resource_uri: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param filter: Reduces the set of data collected by retrieving particular metric definitions from all the definitions available for the resource.&lt;br&gt;For example, to get just the definition for the &#39;CPU percentage&#39; counter: $filter&#x3D;name.value eq &#39;\\Processor(_Total)\\% Processor Time&#39;.&lt;br&gt;Multiple metrics can be retrieved by joining together *&#39;name eq &lt;value&gt;&#39;* clauses separated by *or* logical operators.&lt;br&gt;**NOTE**: No other syntax is allowed.
    :type filter: str

    """
    return web.Response(status=200)
