from typing import List, Dict
from aiohttp import web

from openapi_server.models.file_list import FileList
from openapi_server.models.storage_update_file_request import StorageUpdateFileRequest
from openapi_server import util


async def storage_create_file(request: web.Request, file, read=None, write=None) -> web.Response:
    """Create File

    Create a new file. The user who creates the file will automatically be assigned to read and write access unless he has passed custom values for read and write arguments.

    :param file: Binary file.
    :type file: str
    :param read: An array of strings with read permissions. By default only the current user is granted with read permissions. [learn more about permissions](/docs/permissions) and get a full list of available permissions.
    :type read: List[str]
    :param write: An array of strings with write permissions. By default only the current user is granted with write permissions. [learn more about permissions](/docs/permissions) and get a full list of available permissions.
    :type write: List[str]

    """
    return web.Response(status=200)


async def storage_delete_file(request: web.Request, file_id) -> web.Response:
    """Delete File

    Delete a file by its unique ID. Only users with write permissions have access to delete this resource.

    :param file_id: File unique ID.
    :type file_id: str

    """
    return web.Response(status=200)


async def storage_get_file(request: web.Request, file_id) -> web.Response:
    """Get File

    Get a file by its unique ID. This endpoint response returns a JSON object with the file metadata.

    :param file_id: File unique ID.
    :type file_id: str

    """
    return web.Response(status=200)


async def storage_get_file_download(request: web.Request, file_id) -> web.Response:
    """Get File for Download

    Get a file content by its unique ID. The endpoint response return with a &#39;Content-Disposition: attachment&#39; header that tells the browser to start downloading the file to user downloads directory.

    :param file_id: File unique ID.
    :type file_id: str

    """
    return web.Response(status=200)


async def storage_get_file_preview(request: web.Request, file_id, width=None, height=None, gravity=None, quality=None, border_width=None, border_color=None, border_radius=None, opacity=None, rotation=None, background=None, output=None) -> web.Response:
    """Get File Preview

    Get a file preview image. Currently, this method supports preview for image files (jpg, png, and gif), other supported formats, like pdf, docs, slides, and spreadsheets, will return the file icon image. You can also pass query string arguments for cutting and resizing your preview image.

    :param file_id: File unique ID
    :type file_id: str
    :param width: Resize preview image width, Pass an integer between 0 to 4000.
    :type width: int
    :param height: Resize preview image height, Pass an integer between 0 to 4000.
    :type height: int
    :param gravity: Image crop gravity. Can be one of center,top-left,top,top-right,left,right,bottom-left,bottom,bottom-right
    :type gravity: str
    :param quality: Preview image quality. Pass an integer between 0 to 100. Defaults to 100.
    :type quality: int
    :param border_width: Preview image border in pixels. Pass an integer between 0 to 100. Defaults to 0.
    :type border_width: int
    :param border_color: Preview image border color. Use a valid HEX color, no # is needed for prefix.
    :type border_color: str
    :param border_radius: Preview image border radius in pixels. Pass an integer between 0 to 4000.
    :type border_radius: int
    :param opacity: Preview image opacity. Only works with images having an alpha channel (like png). Pass a number between 0 to 1.
    :type opacity: float
    :param rotation: Preview image rotation in degrees. Pass an integer between 0 and 360.
    :type rotation: int
    :param background: Preview image background color. Only works with transparent images (png). Use a valid HEX color, no # is needed for prefix.
    :type background: str
    :param output: Output format type (jpeg, jpg, png, gif and webp).
    :type output: str

    """
    return web.Response(status=200)


async def storage_get_file_view(request: web.Request, file_id) -> web.Response:
    """Get File for View

    Get a file content by its unique ID. This endpoint is similar to the download method but returns with no  &#39;Content-Disposition: attachment&#39; header.

    :param file_id: File unique ID.
    :type file_id: str

    """
    return web.Response(status=200)


async def storage_list_files(request: web.Request, search=None, limit=None, offset=None, order_type=None) -> web.Response:
    """List Files

    Get a list of all the user files. You can use the query params to filter your results. On admin mode, this endpoint will return a list of all of the project&#39;s files. [Learn more about different API modes](/docs/admin).

    :param search: Search term to filter your list results. Max length: 256 chars.
    :type search: str
    :param limit: Results limit value. By default will return maximum 25 results. Maximum of 100 results allowed per request.
    :type limit: int
    :param offset: Results offset. The default value is 0. Use this param to manage pagination.
    :type offset: int
    :param order_type: Order result by ASC or DESC order.
    :type order_type: str

    """
    return web.Response(status=200)


async def storage_update_file(request: web.Request, file_id, body=None) -> web.Response:
    """Update File

    Update a file by its unique ID. Only users with write permissions have access to update this resource.

    :param file_id: File unique ID.
    :type file_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = StorageUpdateFileRequest.from_dict(body)
    return web.Response(status=200)
