from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.file import File
from openapi_server import util


async def download_file_by_id(request: web.Request, vault_uuid, item_uuid, file_uuid) -> web.Response:
    """Get the content of a File

    

    :param vault_uuid: The UUID of the Vault the item is in
    :type vault_uuid: str
    :type vault_uuid: str
    :param item_uuid: The UUID of the Item the File is in
    :type item_uuid: str
    :type item_uuid: str
    :param file_uuid: UUID of the file to get content from
    :type file_uuid: str

    """
    return web.Response(status=200)


async def get_details_of_file_by_id(request: web.Request, vault_uuid, item_uuid, file_uuid, inline_files=None) -> web.Response:
    """Get the details of a File

    

    :param vault_uuid: The UUID of the Vault to fetch Item from
    :type vault_uuid: str
    :type vault_uuid: str
    :param item_uuid: The UUID of the Item to fetch File from
    :type item_uuid: str
    :type item_uuid: str
    :param file_uuid: The UUID of the File to fetch
    :type file_uuid: str
    :type file_uuid: str
    :param inline_files: Tells server to return the base64-encoded file contents in the response.
    :type inline_files: bool

    """
    return web.Response(status=200)


async def get_item_files(request: web.Request, vault_uuid, item_uuid, inline_files=None) -> web.Response:
    """Get all the files inside an Item

    

    :param vault_uuid: The UUID of the Vault to fetch Items from
    :type vault_uuid: str
    :type vault_uuid: str
    :param item_uuid: The UUID of the Item to fetch files from
    :type item_uuid: str
    :type item_uuid: str
    :param inline_files: Tells server to return the base64-encoded file contents in the response.
    :type inline_files: bool

    """
    return web.Response(status=200)
