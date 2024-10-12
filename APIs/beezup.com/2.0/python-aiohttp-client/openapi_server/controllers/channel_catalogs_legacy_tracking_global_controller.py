from typing import List, Dict
from aiohttp import web

from openapi_server.models.beez_up_common_error_response_message import BeezUPCommonErrorResponseMessage
from openapi_server.models.legacy_tracking_channel_catalog import LegacyTrackingChannelCatalog
from openapi_server.models.legacy_tracking_channel_catalog_list import LegacyTrackingChannelCatalogList
from openapi_server import util


async def get_legacy_tracking_channel_catalog(request: web.Request, channel_catalog_id) -> web.Response:
    """Get the channel catalog configured to use legacy tracking format information

    

    :param channel_catalog_id: The channel catalog identifier
    :type channel_catalog_id: str

    """
    return web.Response(status=200)


async def get_legacy_tracking_channel_catalogs(request: web.Request, store_id=None) -> web.Response:
    """List all your current channel catalogs configured to use legacy tracking format

    

    :param store_id: The store identifier
    :type store_id: str

    """
    return web.Response(status=200)


async def migrate_legacy_tracking_channel_catalog(request: web.Request, channel_catalog_id) -> web.Response:
    """Migrate a channel catalog to current tracking format

    

    :param channel_catalog_id: The channel catalog identifier
    :type channel_catalog_id: str

    """
    return web.Response(status=200)
