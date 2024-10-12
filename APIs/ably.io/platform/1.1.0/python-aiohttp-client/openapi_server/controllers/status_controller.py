from typing import List, Dict
from aiohttp import web

from openapi_server.models.channel_details import ChannelDetails
from openapi_server.models.error import Error
from openapi_server.models.get_metadata_of_all_channels2_xx_response import GetMetadataOfAllChannels2XXResponse
from openapi_server.models.presence_message import PresenceMessage
from openapi_server import util


async def get_metadata_of_all_channels(request: web.Request, x_ably_version=None, format=None, limit=None, prefix=None, by=None) -> web.Response:
    """Enumerate all active channels of the application

    Enumerate all active channels of the application

    :param x_ably_version: The version of the API you wish to use.
    :type x_ably_version: str
    :param format: The response format you would like
    :type format: str
    :param limit: 
    :type limit: int
    :param prefix: Optionally limits the query to only those channels whose name starts with the given prefix
    :type prefix: str
    :param by: optionally specifies whether to return just channel names (by&#x3D;id) or ChannelDetails (by&#x3D;value)
    :type by: str

    """
    return web.Response(status=200)


async def get_metadata_of_channel(request: web.Request, channel_id, x_ably_version=None, format=None) -> web.Response:
    """Get metadata of a channel

    Get metadata of a channel

    :param channel_id: The [Channel&#39;s ID](https://www.ably.io/documentation/rest/channels).
    :type channel_id: str
    :param x_ably_version: The version of the API you wish to use.
    :type x_ably_version: str
    :param format: The response format you would like
    :type format: str

    """
    return web.Response(status=200)


async def get_presence_of_channel(request: web.Request, channel_id, x_ably_version=None, format=None, client_id=None, connection_id=None, limit=None) -> web.Response:
    """Get presence of a channel

    Get presence on a channel

    :param channel_id: The [Channel&#39;s ID](https://www.ably.io/documentation/rest/channels).
    :type channel_id: str
    :param x_ably_version: The version of the API you wish to use.
    :type x_ably_version: str
    :param format: The response format you would like
    :type format: str
    :param client_id: 
    :type client_id: str
    :param connection_id: 
    :type connection_id: str
    :param limit: 
    :type limit: int

    """
    return web.Response(status=200)
