from typing import List, Dict
from aiohttp import web

from openapi_server.models.beez_up_common_error_response_message import BeezUPCommonErrorResponseMessage
from openapi_server.models.channel_catalog_marketplace_properties import ChannelCatalogMarketplaceProperties
from openapi_server.models.channel_catalog_marketplace_settings import ChannelCatalogMarketplaceSettings
from openapi_server.models.set_channel_catalog_marketplace_settings_request import SetChannelCatalogMarketplaceSettingsRequest
from openapi_server import util


async def get_channel_catalog_marketplace_properties(request: web.Request, channel_catalog_id, redirection_page_url, accept_language=None) -> web.Response:
    """Get the marketplace properties for a channel catalog

    

    :param channel_catalog_id: 
    :type channel_catalog_id: str
    :param redirection_page_url: 
    :type redirection_page_url: str
    :param accept_language: Indicates that the client accepts the following languages.
    :type accept_language: List[str]

    """
    return web.Response(status=200)


async def get_channel_catalog_marketplace_settings(request: web.Request, channel_catalog_id) -> web.Response:
    """Get the marketplace settings for a channel catalog

    

    :param channel_catalog_id: Channel Catalog Id to query (required)
    :type channel_catalog_id: str

    """
    return web.Response(status=200)


async def set_channel_catalog_marketplace_settings(request: web.Request, channel_catalog_id, body) -> web.Response:
    """Save new marketplace settings for a channel catalog

    Allow you to configure your marketplace settings. Partial update accepted. 

    :param channel_catalog_id: Channel Catalog Id to query
    :type channel_catalog_id: str
    :param body: Settings to save
    :type body: dict | bytes

    """
    body = SetChannelCatalogMarketplaceSettingsRequest.from_dict(body)
    return web.Response(status=200)
