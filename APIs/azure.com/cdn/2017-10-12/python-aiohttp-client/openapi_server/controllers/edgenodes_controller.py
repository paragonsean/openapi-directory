from typing import List, Dict
from aiohttp import web

from openapi_server.models.edgenode_result import EdgenodeResult
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def edge_nodes_list(request: web.Request, api_version) -> web.Response:
    """edge_nodes_list

    Edgenodes are the global Point of Presence (POP) locations used to deliver CDN content to end users.

    :param api_version: Version of the API to be used with the client request. Current version is 2017-04-02.
    :type api_version: str

    """
    return web.Response(status=200)
