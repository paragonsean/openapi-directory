from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_channel_catalog_request import AddChannelCatalogRequest
from openapi_server.models.beez_up_common_error_response_message import BeezUPCommonErrorResponseMessage
from openapi_server.models.channel_catalog import ChannelCatalog
from openapi_server.models.channel_catalog_list import ChannelCatalogList
from openapi_server.models.filter_operator import FilterOperator
from openapi_server.models.links_get_channel_catalog_link import LinksGetChannelCatalogLink
from openapi_server import util


async def add_channel_catalog(request: web.Request, body) -> web.Response:
    """Add a new channel catalog

    

    :param body: 
    :type body: dict | bytes

    """
    body = AddChannelCatalogRequest.from_dict(body)
    return web.Response(status=200)


async def delete_channel_catalog(request: web.Request, channel_catalog_id) -> web.Response:
    """Delete the channel catalog

    

    :param channel_catalog_id: The channel catalog identifier
    :type channel_catalog_id: str

    """
    return web.Response(status=200)


async def get_channel_catalog(request: web.Request, channel_catalog_id) -> web.Response:
    """Get the channel catalog information

    

    :param channel_catalog_id: The channel catalog identifier
    :type channel_catalog_id: str

    """
    return web.Response(status=200)


async def get_channel_catalog_filter_operators(request: web.Request, ) -> web.Response:
    """Get channel catalog filter operators

    


    """
    return web.Response(status=200)


async def get_channel_catalogs(request: web.Request, store_id=None) -> web.Response:
    """List all your current channel catalogs

    

    :param store_id: The store identifier
    :type store_id: str

    """
    return web.Response(status=200)
