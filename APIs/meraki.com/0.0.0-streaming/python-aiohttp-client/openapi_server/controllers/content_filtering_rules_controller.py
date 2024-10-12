from typing import List, Dict
from aiohttp import web

from openapi_server.models.update_network_content_filtering_request import UpdateNetworkContentFilteringRequest
from openapi_server import util


async def get_network_content_filtering(request: web.Request, network_id) -> web.Response:
    """Return the content filtering settings for an MX network

    Return the content filtering settings for an MX network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def update_network_content_filtering(request: web.Request, network_id, body=None) -> web.Response:
    """Update the content filtering settings for an MX network

    Update the content filtering settings for an MX network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkContentFilteringRequest.from_dict(body)
    return web.Response(status=200)
