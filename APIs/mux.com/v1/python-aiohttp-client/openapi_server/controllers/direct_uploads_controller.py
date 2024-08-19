from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_upload_request import CreateUploadRequest
from openapi_server.models.list_uploads_response import ListUploadsResponse
from openapi_server.models.upload_response import UploadResponse
from openapi_server import util


async def cancel_direct_upload(request: web.Request, upload_id) -> web.Response:
    """Cancel a direct upload

    Cancels a direct upload and marks it as cancelled. If a pending upload finishes after this request, no asset will be created. This request will only succeed if the upload is still in the &#x60;waiting&#x60; state. 

    :param upload_id: ID of the Upload
    :type upload_id: str

    """
    return web.Response(status=200)


async def create_direct_upload(request: web.Request, body) -> web.Response:
    """Create a new direct upload URL

    Creates a new direct upload, through which video content can be uploaded for ingest to Mux.

    :param body: 
    :type body: dict | bytes

    """
    body = CreateUploadRequest.from_dict(body)
    return web.Response(status=200)


async def get_direct_upload(request: web.Request, upload_id) -> web.Response:
    """Retrieve a single direct upload&#39;s info

    Fetches information about a single direct upload in the current environment.

    :param upload_id: ID of the Upload
    :type upload_id: str

    """
    return web.Response(status=200)


async def list_direct_uploads(request: web.Request, limit=None, page=None) -> web.Response:
    """List direct uploads

    Lists direct uploads in the current environment.

    :param limit: Number of items to include in the response
    :type limit: int
    :param page: Offset by this many pages, of the size of &#x60;limit&#x60;
    :type page: int

    """
    return web.Response(status=200)
