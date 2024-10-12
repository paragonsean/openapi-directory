from typing import List, Dict
from aiohttp import web

from openapi_server.models.beez_up_common_error_response_message import BeezUPCommonErrorResponseMessage
from openapi_server.models.channel_catalog_export_cache_info_response import ChannelCatalogExportCacheInfoResponse
from openapi_server.models.channel_catalog_exportation_history import ChannelCatalogExportationHistory
from openapi_server import util


async def clear_channel_catalog_exportation_cache(request: web.Request, channel_catalog_id) -> web.Response:
    """Clear the exportation cache

    

    :param channel_catalog_id: The channel catalog identifier
    :type channel_catalog_id: str

    """
    return web.Response(status=200)


async def get_channel_catalog_exportation_cache_info(request: web.Request, channel_catalog_id) -> web.Response:
    """Get the exportation cache information

    

    :param channel_catalog_id: The channel catalog identifier
    :type channel_catalog_id: str

    """
    return web.Response(status=200)


async def get_channel_catalog_exportation_history(request: web.Request, channel_catalog_id, page_number, page_size) -> web.Response:
    """Get the exportation history

    

    :param channel_catalog_id: The channel catalog identifier
    :type channel_catalog_id: str
    :param page_number: The page number you want to get
    :type page_number: int
    :param page_size: The entry count you want to get
    :type page_size: int

    """
    return web.Response(status=200)
