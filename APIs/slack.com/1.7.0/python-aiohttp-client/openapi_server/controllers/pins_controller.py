from typing import List, Dict
from aiohttp import web

from openapi_server.models.pins_add_error_schema import PinsAddErrorSchema
from openapi_server.models.pins_add_schema import PinsAddSchema
from openapi_server.models.pins_list_error_schema import PinsListErrorSchema
from openapi_server.models.pins_list_success_schema_inner import PinsListSuccessSchemaInner
from openapi_server.models.pins_remove_error_schema import PinsRemoveErrorSchema
from openapi_server.models.pins_remove_schema import PinsRemoveSchema
from openapi_server import util


async def pins_add(request: web.Request, token, channel, timestamp=None) -> web.Response:
    """pins_add

    Pins an item to a channel.

    :param token: Authentication token. Requires scope: &#x60;pins:write&#x60;
    :type token: str
    :param channel: Channel to pin the item in.
    :type channel: str
    :param timestamp: Timestamp of the message to pin.
    :type timestamp: str

    """
    return web.Response(status=200)


async def pins_list(request: web.Request, token, channel) -> web.Response:
    """pins_list

    Lists items pinned to a channel.

    :param token: Authentication token. Requires scope: &#x60;pins:read&#x60;
    :type token: str
    :param channel: Channel to get pinned items for.
    :type channel: str

    """
    return web.Response(status=200)


async def pins_remove(request: web.Request, token, channel, timestamp=None) -> web.Response:
    """pins_remove

    Un-pins an item from a channel.

    :param token: Authentication token. Requires scope: &#x60;pins:write&#x60;
    :type token: str
    :param channel: Channel where the item is pinned to.
    :type channel: str
    :param timestamp: Timestamp of the message to un-pin.
    :type timestamp: str

    """
    return web.Response(status=200)
