from typing import List, Dict
from aiohttp import web

from openapi_server.models.beez_up_common_error_response_message import BeezUPCommonErrorResponseMessage
from openapi_server import util


async def configure_channel_catalog_product_value_override_copy(request: web.Request, channel_catalog_id, product_id) -> web.Response:
    """Copy channel catalog product value override

    

    :param channel_catalog_id: The channel catalog identifier
    :type channel_catalog_id: str
    :param product_id: The product identifier
    :type product_id: str

    """
    return web.Response(status=200)


async def delete_channel_catalog_product_value_override(request: web.Request, channel_catalog_id, product_id, channel_column_id) -> web.Response:
    """Delete a specific channel catalog product value override

    

    :param channel_catalog_id: The channel catalog identifier
    :type channel_catalog_id: str
    :param product_id: The product identifier
    :type product_id: str
    :param channel_column_id: The channel column identifier
    :type channel_column_id: str

    """
    return web.Response(status=200)


async def get_channel_catalog_product_value_override_copy(request: web.Request, channel_catalog_id, product_id) -> web.Response:
    """Get channel catalog product value override compatibilities status

    

    :param channel_catalog_id: The channel catalog identifier
    :type channel_catalog_id: str
    :param product_id: The product identifier
    :type product_id: str

    """
    return web.Response(status=200)


async def override_channel_catalog_product_values(request: web.Request, channel_catalog_id, product_id, body) -> web.Response:
    """Override channel catalog product values

    

    :param channel_catalog_id: The channel catalog identifier
    :type channel_catalog_id: str
    :param product_id: The product identifier
    :type product_id: str
    :param body: 
    :type body: Dict[str, str]

    """
    return web.Response(status=200)
