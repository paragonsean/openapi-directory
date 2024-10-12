from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_v2_cddrive_folders_folder_id_items_get200_response import ApiV2CddriveFoldersFolderIdItemsGet200Response
from openapi_server.models.cd_drive_file import CDDriveFile
from openapi_server.models.cd_drive_folder import CDDriveFolder
from openapi_server import util


async def api_v2_cddrive_files_content_post(request: web.Request, content_md5=None, file=None, name=None, parent_id=None) -> web.Response:
    """Upload a file.

    Upload a file to the customer&#39;s private CD Drive.

    :param content_md5: If present, the MD5 will be compared against the file received as a message integrity check.
    :type content_md5: str
    :param file: The file content being uploaded.
    :type file: str
    :param name: The name of the file, including extension.
    :type name: str
    :param parent_id: The ID of the parent folder or 0 for the root folder.
    :type parent_id: int

    """
    return web.Response(status=200)


async def api_v2_cddrive_files_file_id_content_get(request: web.Request, file_id, range=None) -> web.Response:
    """UNDER DEVELOPMENT - Download a file.

    Download a file from the customer&#39;s private CD Drive.

    :param file_id: The ID of the file to download.
    :type file_id: int
    :param range: Can be used to limit the range of bytes retrieved. Only a single byte range in the format &#x60;&#x60;&#x60;bytes&#x3D;{start-range}-{end-range}&#x60;&#x60;&#x60; is supported.
    :type range: str

    """
    return web.Response(status=200)


async def api_v2_cddrive_files_file_id_delete(request: web.Request, file_id) -> web.Response:
    """Delete a file.

    Delete a file from the customer&#39;s private CD Drive.

    :param file_id: The ID of the file to access.
    :type file_id: int

    """
    return web.Response(status=200)


async def api_v2_cddrive_files_file_id_get(request: web.Request, file_id) -> web.Response:
    """Get file information.

    Get the information about a file in the customer&#39;s private CD Drive.

    :param file_id: The ID of the file to access.
    :type file_id: int

    """
    return web.Response(status=200)


async def api_v2_cddrive_folders_folder_id_delete(request: web.Request, folder_id, recursive=None) -> web.Response:
    """UNDER DEVELOPMENT - Delete a folder.

    Delete a file from the customer&#39;s private CD Drive.

    :param folder_id: The ID of the folder to get.
    :type folder_id: int
    :param recursive: Flag to indicate if the folder should be deleted if it has items inside of it.
    :type recursive: bool

    """
    return web.Response(status=200)


async def api_v2_cddrive_folders_folder_id_get(request: web.Request, folder_id) -> web.Response:
    """UNDER DEVELOPMENT - Get folder information.

    Get the information about a folder in the customer&#39;s private CD Drive.

    :param folder_id: The ID of the folder to get.
    :type folder_id: int

    """
    return web.Response(status=200)


async def api_v2_cddrive_folders_folder_id_items_get(request: web.Request, folder_id, offset=None, limit=None) -> web.Response:
    """Get the items in the folder.

    Get the information about a folder in the customer&#39;s private CD Drive.

    :param folder_id: The ID of the folder to get. Folder ID 0 represents the uppermost CD drive folder.
    :type folder_id: int
    :param offset: The offset into the items to begin the response.
    :type offset: int
    :param limit: The maximum number of items to return in the response.
    :type limit: int

    """
    return web.Response(status=200)


async def api_v2_cddrive_folders_post(request: web.Request, name=None, parent_id=None) -> web.Response:
    """Create a folder.

    Create a new folder in the customer&#39;s private CD Drive.

    :param name: the name of the folder
    :type name: str
    :param parent_id: The ID of the parent folder or 0 for the root folder.
    :type parent_id: int

    """
    return web.Response(status=200)
