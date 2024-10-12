from typing import List, Dict
from aiohttp import web

from openapi_server.models.beez_up_common_error_response_message import BeezUPCommonErrorResponseMessage
from openapi_server.models.channel_catalog_column_mapping import ChannelCatalogColumnMapping
from openapi_server import util


async def configure_channel_catalog_column_mappings(request: web.Request, channel_catalog_id, body) -> web.Response:
    """Configure channel catalog column mappings

    

    :param channel_catalog_id: The channel catalog identifier
    :type channel_catalog_id: str
    :param body: 
    :type body: list | bytes

    """
    body = [ChannelCatalogColumnMapping.from_dict(d) for d in body]
    return web.Response(status=200)
