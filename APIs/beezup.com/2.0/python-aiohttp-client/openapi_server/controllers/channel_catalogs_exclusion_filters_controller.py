from typing import List, Dict
from aiohttp import web

from openapi_server.models.beez_up_common_error_response_message import BeezUPCommonErrorResponseMessage
from openapi_server.models.exclusion_filter import ExclusionFilter
from openapi_server.models.exclusion_filters_response import ExclusionFiltersResponse
from openapi_server import util


async def configure_channel_catalog_exclusion_filters(request: web.Request, channel_catalog_id, body) -> web.Response:
    """Configure channel catalog exclusion filters

    

    :param channel_catalog_id: The channel catalog identifier
    :type channel_catalog_id: str
    :param body: 
    :type body: list | bytes

    """
    body = [ExclusionFilter.from_dict(d) for d in body]
    return web.Response(status=200)


async def get_channel_catalog_exclusion_filters(request: web.Request, channel_catalog_id) -> web.Response:
    """Get channel catalog exclusion filters

    

    :param channel_catalog_id: The channel catalog identifier
    :type channel_catalog_id: str

    """
    return web.Response(status=200)
