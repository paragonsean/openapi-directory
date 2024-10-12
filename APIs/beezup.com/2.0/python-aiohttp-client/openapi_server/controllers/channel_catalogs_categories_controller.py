from typing import List, Dict
from aiohttp import web

from openapi_server.models.beez_up_common_error_response_message import BeezUPCommonErrorResponseMessage
from openapi_server.models.channel_catalog_category_configuration_list import ChannelCatalogCategoryConfigurationList
from openapi_server.models.configure_category_request import ConfigureCategoryRequest
from openapi_server import util


async def configure_channel_catalog_category(request: web.Request, channel_catalog_id, body) -> web.Response:
    """Configure channel catalog category

    

    :param channel_catalog_id: The channel catalog identifier
    :type channel_catalog_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ConfigureCategoryRequest.from_dict(body)
    return web.Response(status=200)


async def disable_channel_catalog_category_mapping(request: web.Request, channel_catalog_id) -> web.Response:
    """Disable a channel catalog category mapping

    

    :param channel_catalog_id: The channel catalog identifier
    :type channel_catalog_id: str

    """
    return web.Response(status=200)


async def get_channel_catalog_categories(request: web.Request, channel_catalog_id) -> web.Response:
    """Get channel catalog categories

    

    :param channel_catalog_id: The channel catalog identifier
    :type channel_catalog_id: str

    """
    return web.Response(status=200)


async def reenable_channel_catalog_category_mapping(request: web.Request, channel_catalog_id) -> web.Response:
    """Reenable a channel catalog category mapping

    

    :param channel_catalog_id: The channel catalog identifier
    :type channel_catalog_id: str

    """
    return web.Response(status=200)
