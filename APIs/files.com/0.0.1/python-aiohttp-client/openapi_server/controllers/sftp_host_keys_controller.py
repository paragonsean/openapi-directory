from typing import List, Dict
from aiohttp import web

from openapi_server.models.sftp_host_key_entity import SftpHostKeyEntity
from openapi_server import util


async def delete_sftp_host_keys_id(request: web.Request, id) -> web.Response:
    """Delete Sftp Host Key

    Delete Sftp Host Key

    :param id: Sftp Host Key ID.
    :type id: int

    """
    return web.Response(status=200)


async def get_sftp_host_keys(request: web.Request, cursor=None, per_page=None) -> web.Response:
    """List Sftp Host Keys

    List Sftp Host Keys

    :param cursor: Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
    :type cursor: str
    :param per_page: Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
    :type per_page: int

    """
    return web.Response(status=200)


async def get_sftp_host_keys_id(request: web.Request, id) -> web.Response:
    """Show Sftp Host Key

    Show Sftp Host Key

    :param id: Sftp Host Key ID.
    :type id: int

    """
    return web.Response(status=200)


async def patch_sftp_host_keys_id(request: web.Request, id, name=None, private_key=None) -> web.Response:
    """Update Sftp Host Key

    Update Sftp Host Key

    :param id: Sftp Host Key ID.
    :type id: int
    :param name: The friendly name of this SFTP Host Key.
    :type name: str
    :param private_key: The private key data.
    :type private_key: str

    """
    return web.Response(status=200)


async def post_sftp_host_keys(request: web.Request, name=None, private_key=None) -> web.Response:
    """Create Sftp Host Key

    Create Sftp Host Key

    :param name: The friendly name of this SFTP Host Key.
    :type name: str
    :param private_key: The private key data.
    :type private_key: str

    """
    return web.Response(status=200)
