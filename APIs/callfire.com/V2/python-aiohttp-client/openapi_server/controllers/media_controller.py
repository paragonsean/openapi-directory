from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.media import Media
from openapi_server.models.media_page import MediaPage
from openapi_server.models.resource_id import ResourceId
from openapi_server import util


async def create_media(request: web.Request, file, name=None) -> web.Response:
    """Create media

    Uploads media file to account, acceptable media formats: bmp, gif, jpg, m4a, mp3, mp4, png, wav

    :param file: Binary media file
    :type file: str
    :param name: A name of a media file
    :type name: str

    """
    return web.Response(status=200)


async def find_media(request: web.Request, limit=None, offset=None, filter=None, fields=None) -> web.Response:
    """Find media

    Find media files created by user

    :param limit: To set the maximum number of records to return in a paged list response. The default is 100
    :type limit: int
    :param offset: Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API.
    :type offset: int
    :param filter: value to filter file names again; this value is used to check if the filename contains the filter value.
    :type filter: str
    :param fields: Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
    :type fields: str

    """
    return web.Response(status=200)


async def get_media(request: web.Request, id, fields=None) -> web.Response:
    """Get a specific media

    Get media resource by id

    :param id: An id of a media resource
    :type id: int
    :param fields: Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
    :type fields: str

    """
    return web.Response(status=200)


async def get_media_data(request: web.Request, id, extension) -> web.Response:
    """Download media by extension

    Download a media file. Available types of files: bmp, gif, jpg, m4a, mp3, mp4, png, wav. Content type in response depends on &#39;extension&#39; parameter, e.g. image/jpeg, image/png, audio/mp3, etc

    :param id: An id of a media resource
    :type id: int
    :param extension: Media file type. Available types: bmp, gif, jpg, m4a, mp3, mp4, png, wav
    :type extension: str

    """
    return web.Response(status=200)


async def get_media_data_binary(request: web.Request, id) -> web.Response:
    """Download a MP3 media

    Download a MP3 media, endpoint returns application/binary content-type

    :param id: An id of a media resource
    :type id: int

    """
    return web.Response(status=200)


async def get_media_data_by_key(request: web.Request, key, extension) -> web.Response:
    """Download media by extension

    Download a media file. Available types of files: bmp, gif, jpg, m4a, mp3, mp4, png, wav. Content type in response depends on &#39;extension&#39; parameter, e.g. image/jpeg, image/png, audio/mp3, etc

    :param key: A hash-key of a media resource
    :type key: str
    :param extension: Media file type, available types: bmp, gif, jpg, m4a, mp3, mp4, png, wav
    :type extension: str

    """
    return web.Response(status=200)
