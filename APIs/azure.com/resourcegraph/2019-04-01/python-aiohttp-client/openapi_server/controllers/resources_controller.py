from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.query_request import QueryRequest
from openapi_server.models.query_response import QueryResponse
from openapi_server import util


async def resources(request: web.Request, api_version, query) -> web.Response:
    """resources

    Queries the resources managed by Azure Resource Manager for all subscriptions specified in the request.

    :param api_version: API version.
    :type api_version: str
    :param query: Request specifying query and its options.
    :type query: dict | bytes

    """
    query = QueryRequest.from_dict(query)
    return web.Response(status=200)
