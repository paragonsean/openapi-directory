from typing import List, Dict
from aiohttp import web

from openapi_server.models.channel_column import ChannelColumn
from openapi_server.models.channel_header import ChannelHeader
from openapi_server.models.channel_info import ChannelInfo
from openapi_server.models.channel_root_category import ChannelRootCategory
from openapi_server import util


async def get_available_channels(request: web.Request, store_id) -> web.Response:
    """List all available channel for this store

    

    :param store_id: The store identifier
    :type store_id: str

    """
    return web.Response(status=200)


async def get_channel_categories(request: web.Request, channel_id, accept_encoding) -> web.Response:
    """Get channel categories

    

    :param channel_id: The channel identifier
    :type channel_id: str
    :param accept_encoding: Indicates that the client accepts that the response will be compressed to reduce traffic size.
    :type accept_encoding: List[str]

    """
    return web.Response(status=200)


async def get_channel_columns(request: web.Request, channel_id, accept_encoding, body=None) -> web.Response:
    """Get channel columns

    

    :param channel_id: The channel identifier
    :type channel_id: str
    :param accept_encoding: Indicates that the client accepts that the response will be compressed to reduce traffic size.
    :type accept_encoding: List[str]
    :param body: Allow you to filter the channel column identifier list your want to get
    :type body: List[str]

    """
    return web.Response(status=200)


async def get_channel_info(request: web.Request, channel_id) -> web.Response:
    """Get channel information

    

    :param channel_id: The channel identifier
    :type channel_id: str

    """
    return web.Response(status=200)
