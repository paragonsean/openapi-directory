from typing import List, Dict
from aiohttp import web

from openapi_server.models.public_key_entity import PublicKeyEntity
from openapi_server import util


async def delete_public_keys_id(request: web.Request, id) -> web.Response:
    """Delete Public Key

    Delete Public Key

    :param id: Public Key ID.
    :type id: int

    """
    return web.Response(status=200)


async def get_public_keys(request: web.Request, user_id=None, cursor=None, per_page=None) -> web.Response:
    """List Public Keys

    List Public Keys

    :param user_id: User ID.  Provide a value of &#x60;0&#x60; to operate the current session&#39;s user.
    :type user_id: int
    :param cursor: Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
    :type cursor: str
    :param per_page: Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
    :type per_page: int

    """
    return web.Response(status=200)


async def get_public_keys_id(request: web.Request, id) -> web.Response:
    """Show Public Key

    Show Public Key

    :param id: Public Key ID.
    :type id: int

    """
    return web.Response(status=200)


async def patch_public_keys_id(request: web.Request, id, title) -> web.Response:
    """Update Public Key

    Update Public Key

    :param id: Public Key ID.
    :type id: int
    :param title: Internal reference for key.
    :type title: str

    """
    return web.Response(status=200)


async def post_public_keys(request: web.Request, public_key, title, user_id=None) -> web.Response:
    """Create Public Key

    Create Public Key

    :param public_key: Actual contents of SSH key.
    :type public_key: str
    :param title: Internal reference for key.
    :type title: str
    :param user_id: User ID.  Provide a value of &#x60;0&#x60; to operate the current session&#39;s user.
    :type user_id: int

    """
    return web.Response(status=200)
