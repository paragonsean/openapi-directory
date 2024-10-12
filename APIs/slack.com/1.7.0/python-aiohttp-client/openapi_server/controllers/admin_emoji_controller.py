from typing import List, Dict
from aiohttp import web

from openapi_server.models.default_error_template import DefaultErrorTemplate
from openapi_server.models.default_success_template import DefaultSuccessTemplate
from openapi_server import util


async def admin_emoji_add(request: web.Request, name, token, url) -> web.Response:
    """admin_emoji_add

    Add an emoji.

    :param name: The name of the emoji to be removed. Colons (&#x60;:myemoji:&#x60;) around the value are not required, although they may be included.
    :type name: str
    :param token: Authentication token. Requires scope: &#x60;admin.teams:write&#x60;
    :type token: str
    :param url: The URL of a file to use as an image for the emoji. Square images under 128KB and with transparent backgrounds work best.
    :type url: str

    """
    return web.Response(status=200)


async def admin_emoji_add_alias(request: web.Request, alias_for, name, token) -> web.Response:
    """admin_emoji_add_alias

    Add an emoji alias.

    :param alias_for: The alias of the emoji.
    :type alias_for: str
    :param name: The name of the emoji to be aliased. Colons (&#x60;:myemoji:&#x60;) around the value are not required, although they may be included.
    :type name: str
    :param token: Authentication token. Requires scope: &#x60;admin.teams:write&#x60;
    :type token: str

    """
    return web.Response(status=200)


async def admin_emoji_list(request: web.Request, token, cursor=None, limit=None) -> web.Response:
    """admin_emoji_list

    List emoji for an Enterprise Grid organization.

    :param token: Authentication token. Requires scope: &#x60;admin.teams:read&#x60;
    :type token: str
    :param cursor: Set &#x60;cursor&#x60; to &#x60;next_cursor&#x60; returned by the previous call to list items in the next page
    :type cursor: str
    :param limit: The maximum number of items to return. Must be between 1 - 1000 both inclusive.
    :type limit: int

    """
    return web.Response(status=200)


async def admin_emoji_remove(request: web.Request, name, token) -> web.Response:
    """admin_emoji_remove

    Remove an emoji across an Enterprise Grid organization

    :param name: The name of the emoji to be removed. Colons (&#x60;:myemoji:&#x60;) around the value are not required, although they may be included.
    :type name: str
    :param token: Authentication token. Requires scope: &#x60;admin.teams:write&#x60;
    :type token: str

    """
    return web.Response(status=200)


async def admin_emoji_rename(request: web.Request, name, new_name, token) -> web.Response:
    """admin_emoji_rename

    Rename an emoji.

    :param name: The name of the emoji to be renamed. Colons (&#x60;:myemoji:&#x60;) around the value are not required, although they may be included.
    :type name: str
    :param new_name: The new name of the emoji.
    :type new_name: str
    :param token: Authentication token. Requires scope: &#x60;admin.teams:write&#x60;
    :type token: str

    """
    return web.Response(status=200)
