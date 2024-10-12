from typing import List, Dict
from aiohttp import web

from openapi_server.models.beez_up_common_error_response_message import BeezUPCommonErrorResponseMessage
from openapi_server.models.cost_settings import CostSettings
from openapi_server.models.general_settings import GeneralSettings
from openapi_server.models.upgrade_offer_required import UpgradeOfferRequired
from openapi_server import util


async def configure_channel_catalog_cost_settings(request: web.Request, channel_catalog_id, body) -> web.Response:
    """Configure channel catalog cost settings

    

    :param channel_catalog_id: The channel catalog identifier
    :type channel_catalog_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CostSettings.from_dict(body)
    return web.Response(status=200)


async def configure_channel_catalog_general_settings(request: web.Request, channel_catalog_id, body) -> web.Response:
    """Configure channel catalog general settings

    

    :param channel_catalog_id: The channel catalog identifier
    :type channel_catalog_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = GeneralSettings.from_dict(body)
    return web.Response(status=200)


async def disable_channel_catalog(request: web.Request, channel_catalog_id) -> web.Response:
    """Disable a channel catalog

    

    :param channel_catalog_id: The channel catalog identifier
    :type channel_catalog_id: str

    """
    return web.Response(status=200)


async def enable_channel_catalog(request: web.Request, channel_catalog_id) -> web.Response:
    """Enable a channel catalog

    

    :param channel_catalog_id: The channel catalog identifier
    :type channel_catalog_id: str

    """
    return web.Response(status=200)
