from typing import List, Dict
from aiohttp import web

from openapi_server.models.reactions_add_error_schema import ReactionsAddErrorSchema
from openapi_server.models.reactions_add_schema import ReactionsAddSchema
from openapi_server.models.reactions_get_error_schema import ReactionsGetErrorSchema
from openapi_server.models.reactions_get_success_schema_inner import ReactionsGetSuccessSchemaInner
from openapi_server.models.reactions_list_error_schema import ReactionsListErrorSchema
from openapi_server.models.reactions_list_schema import ReactionsListSchema
from openapi_server.models.reactions_remove_error_schema import ReactionsRemoveErrorSchema
from openapi_server.models.reactions_remove_schema import ReactionsRemoveSchema
from openapi_server import util


async def reactions_add(request: web.Request, token, channel, name, timestamp) -> web.Response:
    """reactions_add

    Adds a reaction to an item.

    :param token: Authentication token. Requires scope: &#x60;reactions:write&#x60;
    :type token: str
    :param channel: Channel where the message to add reaction to was posted.
    :type channel: str
    :param name: Reaction (emoji) name.
    :type name: str
    :param timestamp: Timestamp of the message to add reaction to.
    :type timestamp: str

    """
    return web.Response(status=200)


async def reactions_get(request: web.Request, token, channel=None, file=None, file_comment=None, full=None, timestamp=None) -> web.Response:
    """reactions_get

    Gets reactions for an item.

    :param token: Authentication token. Requires scope: &#x60;reactions:read&#x60;
    :type token: str
    :param channel: Channel where the message to get reactions for was posted.
    :type channel: str
    :param file: File to get reactions for.
    :type file: str
    :param file_comment: File comment to get reactions for.
    :type file_comment: str
    :param full: If true always return the complete reaction list.
    :type full: bool
    :param timestamp: Timestamp of the message to get reactions for.
    :type timestamp: str

    """
    return web.Response(status=200)


async def reactions_list(request: web.Request, token, user=None, full=None, count=None, page=None, cursor=None, limit=None) -> web.Response:
    """reactions_list

    Lists reactions made by a user.

    :param token: Authentication token. Requires scope: &#x60;reactions:read&#x60;
    :type token: str
    :param user: Show reactions made by this user. Defaults to the authed user.
    :type user: str
    :param full: If true always return the complete reaction list.
    :type full: bool
    :param count: 
    :type count: int
    :param page: 
    :type page: int
    :param cursor: Parameter for pagination. Set &#x60;cursor&#x60; equal to the &#x60;next_cursor&#x60; attribute returned by the previous request&#39;s &#x60;response_metadata&#x60;. This parameter is optional, but pagination is mandatory: the default value simply fetches the first \&quot;page\&quot; of the collection. See [pagination](/docs/pagination) for more details.
    :type cursor: str
    :param limit: The maximum number of items to return. Fewer than the requested number of items may be returned, even if the end of the list hasn&#39;t been reached.
    :type limit: int

    """
    return web.Response(status=200)


async def reactions_remove(request: web.Request, token, name, channel=None, file=None, file_comment=None, timestamp=None) -> web.Response:
    """reactions_remove

    Removes a reaction from an item.

    :param token: Authentication token. Requires scope: &#x60;reactions:write&#x60;
    :type token: str
    :param name: Reaction (emoji) name.
    :type name: str
    :param channel: Channel where the message to remove reaction from was posted.
    :type channel: str
    :param file: File to remove reaction from.
    :type file: str
    :param file_comment: File comment to remove reaction from.
    :type file_comment: str
    :param timestamp: Timestamp of the message to remove reaction from.
    :type timestamp: str

    """
    return web.Response(status=200)
