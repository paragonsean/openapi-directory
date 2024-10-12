from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_media_files_code200_response import GetMediaFilesCode200Response
from openapi_server.models.media_files import MediaFiles
from openapi_server.models.post_media_files_request import PostMediaFilesRequest
from openapi_server.models.post_token400_response import PostToken400Response
from openapi_server import util


async def get_media_files(request: web.Request, page=None, limit=None, with_count=None) -> web.Response:
    """Get a list of product media files

    This endpoint allows you to get a list of media files that are used as attribute values in products or product models.

    :param page: Number of the page to retrieve when using the &#x60;page&#x60; pagination method type. &lt;strong&gt;Should never be set manually&lt;/strong&gt;, see &lt;a href&#x3D;\&quot;/documentation/pagination.html#pagination\&quot;&gt;Pagination&lt;/a&gt; section
    :type page: int
    :param limit: Number of results by page, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section
    :type limit: int
    :param with_count: Return the count of items in the response. Be carefull with that, on a big catalog, it can decrease performance in a significative way
    :type with_count: bool

    """
    return web.Response(status=200)


async def get_media_files_code(request: web.Request, code) -> web.Response:
    """Get a product media file

    This endpoint allows you to get the information about a given media file that is used as an attribute value of a product or a product model.

    :param code: Code of the resource
    :type code: str

    """
    return web.Response(status=200)


async def get_media_files_code_download(request: web.Request, code) -> web.Response:
    """Download a product media file

    This endpoint allows you to download a given media file that is used as an attribute value of a product or a product model.

    :param code: Code of the resource
    :type code: str

    """
    return web.Response(status=200)


async def post_media_files(request: web.Request, content_type, body=None) -> web.Response:
    """Create a new product media file

    This endpoint allows you to create a new media file and associate it to an attribute value of a given product or product model.

    :param content_type: Equal to &#39;multipart/form-data&#39;, no other value allowed
    :type content_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = PostMediaFilesRequest.from_dict(body)
    return web.Response(status=200)
