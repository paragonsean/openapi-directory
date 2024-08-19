from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_routing_keys_response import ListRoutingKeysResponse
from openapi_server import util


async def api_public_v1_org_routing_keys_get(request: web.Request, x_vo_api_id, x_vo_api_key) -> web.Response:
    """List routing keys with associated teams

    Retrieves a list of routing keys and associated teams. This API may be called a maximum of 60 times per minute.

    :param x_vo_api_id: Your API ID
    :type x_vo_api_id: str
    :param x_vo_api_key: Your API Key
    :type x_vo_api_key: str

    """
    return web.Response(status=200)
