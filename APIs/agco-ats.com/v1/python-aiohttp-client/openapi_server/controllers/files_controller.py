from typing import List, Dict
from aiohttp import web

from openapi_server.models.apii_paged_response_global_resources_shared_models_file_download import APIIPagedResponseGlobalResourcesSharedModelsFileDownload
from openapi_server.models.api_models_api_error import APIModelsApiError
from openapi_server.models.global_resources_shared_models_file_download import GlobalResourcesSharedModelsFileDownload
from openapi_server import util


async def files_delete_file(request: web.Request, id) -> web.Response:
    """Mark a file as &#39;Removed&#39;. Disables download of the file and hides metadata from GET all method

    No Documentation Found.

    :param id: The file&#39;s id.
    :type id: str

    """
    return web.Response(status=200)


async def files_get_file(request: web.Request, id) -> web.Response:
    """Gets a file&#39;s metadata.

    No Documentation Found.

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def files_get_file_contents(request: web.Request, id) -> web.Response:
    """Download the contents of a file. The current State of the File should be &#39;Available&#39;.

    No Documentation Found.

    :param id: The file&#39;s metadata.
    :type id: str

    """
    return web.Response(status=200)


async def files_get_files(request: web.Request, include_deleted=None, limit=None, offset=None) -> web.Response:
    """Get a paged response of file metadata.

    No Documentation Found.

    :param include_deleted: Indicates whether to include files marked as removed.
    :type include_deleted: bool
    :param limit: Optional. The page limit. The default page limit is 10.
    :type limit: int
    :param offset: Optional. The page offset. The default page offset is 0.
    :type offset: int

    """
    return web.Response(status=200)


async def files_post_file(request: web.Request, body) -> web.Response:
    """Create the metadata for a file before uploading. The State of the File should be &#39;Created&#39;.

    No Documentation Found.

    :param body: The file&#39;s metadata.
    :type body: dict | bytes

    """
    body = GlobalResourcesSharedModelsFileDownload.from_dict(body)
    return web.Response(status=200)


async def files_put_file(request: web.Request, id, body) -> web.Response:
    """Update the metadata for a file. Size may not be modified by the client.

    Update the metadata for a file. Size may not be modified by the client.                   Set status to &#39;Available&#39; to publish a file. The file must be uploaded.                  Set status to &#39;Created&#39; to reset a file&#39;s contents and re-upload.                   A file may only be &#39;Removed&#39; by the DELETE method.

    :param id: The file&#39;s id
    :type id: str
    :param body: The file&#39;s metadata
    :type body: dict | bytes

    """
    body = GlobalResourcesSharedModelsFileDownload.from_dict(body)
    return web.Response(status=200)


async def files_put_file_contents(request: web.Request, id) -> web.Response:
    """Upload the contents of a file. The current State of the File should be &#39;Created&#39;.

    No Documentation Found.

    :param id: The file&#39;s metadata.
    :type id: str

    """
    return web.Response(status=200)
