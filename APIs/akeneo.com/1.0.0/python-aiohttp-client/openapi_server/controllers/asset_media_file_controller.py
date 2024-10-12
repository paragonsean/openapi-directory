from typing import List, Dict
from aiohttp import web

from openapi_server.models.post_asset_media_files_request import PostAssetMediaFilesRequest
from openapi_server.models.post_token400_response import PostToken400Response
from openapi_server import util


async def get_asset_media_files_code(request: web.Request, code) -> web.Response:
    """Download the media file associated to an asset

    This endpoint allows you to download a given media file that is associated with an asset.

    :param code: Code of the resource
    :type code: str

    """
    return web.Response(status=200)


async def post_asset_media_files(request: web.Request, content_type, body=None) -> web.Response:
    """Create a new media file for an asset

    This endpoint allows you to create a new media file and associate it to a media file attribute value of an asset.

    :param content_type: Equal to &#39;multipart/form-data&#39;, no other value allowed
    :type content_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = PostAssetMediaFilesRequest.from_dict(body)
    return web.Response(status=200)
