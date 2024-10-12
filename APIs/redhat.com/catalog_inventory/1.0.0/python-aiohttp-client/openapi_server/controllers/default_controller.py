from typing import List, Dict
from aiohttp import web

from openapi_server.models.graph_ql_request import GraphQLRequest
from openapi_server.models.graph_ql_response import GraphQLResponse
from openapi_server import util


async def get_documentation(request: web.Request, ) -> web.Response:
    """Return this API document in JSON format

    


    """
    return web.Response(status=200)


async def post_graph_ql(request: web.Request, body) -> web.Response:
    """Perform a GraphQL Query

    Performs a GraphQL Query

    :param body: GraphQL Query Request
    :type body: dict | bytes

    """
    body = GraphQLRequest.from_dict(body)
    return web.Response(status=200)
