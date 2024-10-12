from typing import List, Dict
from aiohttp import web

from openapi_server.models.stars_add_error_schema import StarsAddErrorSchema
from openapi_server.models.stars_add_schema import StarsAddSchema
from openapi_server.models.stars_list_error_schema import StarsListErrorSchema
from openapi_server.models.stars_list_schema import StarsListSchema
from openapi_server.models.stars_remove_error_schema import StarsRemoveErrorSchema
from openapi_server.models.stars_remove_schema import StarsRemoveSchema
from openapi_server import util


async def stars_add(request: web.Request, token, channel=None, file=None, file_comment=None, timestamp=None) -> web.Response:
    """stars_add

    Adds a star to an item.

    :param token: Authentication token. Requires scope: &#x60;stars:write&#x60;
    :type token: str
    :param channel: Channel to add star to, or channel where the message to add star to was posted (used with &#x60;timestamp&#x60;).
    :type channel: str
    :param file: File to add star to.
    :type file: str
    :param file_comment: File comment to add star to.
    :type file_comment: str
    :param timestamp: Timestamp of the message to add star to.
    :type timestamp: str

    """
    return web.Response(status=200)


async def stars_list(request: web.Request, token=None, count=None, page=None, cursor=None, limit=None) -> web.Response:
    """stars_list

    Lists stars for a user.

    :param token: Authentication token. Requires scope: &#x60;stars:read&#x60;
    :type token: str
    :param count: 
    :type count: str
    :param page: 
    :type page: str
    :param cursor: Parameter for pagination. Set &#x60;cursor&#x60; equal to the &#x60;next_cursor&#x60; attribute returned by the previous request&#39;s &#x60;response_metadata&#x60;. This parameter is optional, but pagination is mandatory: the default value simply fetches the first \&quot;page\&quot; of the collection. See [pagination](/docs/pagination) for more details.
    :type cursor: str
    :param limit: The maximum number of items to return. Fewer than the requested number of items may be returned, even if the end of the list hasn&#39;t been reached.
    :type limit: int

    """
    return web.Response(status=200)


async def stars_remove(request: web.Request, token, channel=None, file=None, file_comment=None, timestamp=None) -> web.Response:
    """stars_remove

    Removes a star from an item.

    :param token: Authentication token. Requires scope: &#x60;stars:write&#x60;
    :type token: str
    :param channel: Channel to remove star from, or channel where the message to remove star from was posted (used with &#x60;timestamp&#x60;).
    :type channel: str
    :param file: File to remove star from.
    :type file: str
    :param file_comment: File comment to remove star from.
    :type file_comment: str
    :param timestamp: Timestamp of the message to remove star from.
    :type timestamp: str

    """
    return web.Response(status=200)
