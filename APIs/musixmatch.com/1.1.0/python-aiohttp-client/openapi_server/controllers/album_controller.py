from typing import List, Dict
from aiohttp import web

from openapi_server.models.album_get_get200_response import AlbumGetGet200Response
from openapi_server.models.artist_albums_get_get200_response import ArtistAlbumsGetGet200Response
from openapi_server import util


async def album_get_get(request: web.Request, album_id, format=None, param_callback=None) -> web.Response:
    """album_get_get

    

    :param album_id: The musiXmatch album id
    :type album_id: str
    :param format: output format: json, jsonp, xml.
    :type format: str
    :param param_callback: jsonp callback
    :type param_callback: str

    """
    return web.Response(status=200)


async def artist_albums_get_get(request: web.Request, artist_id, format=None, param_callback=None, s_release_date=None, g_album_name=None, page_size=None, page=None) -> web.Response:
    """artist_albums_get_get

    

    :param artist_id: The musiXmatch artist id
    :type artist_id: str
    :param format: output format: json, jsonp, xml.
    :type format: str
    :param param_callback: jsonp callback
    :type param_callback: str
    :param s_release_date: Sort by release date (asc|desc)
    :type s_release_date: str
    :param g_album_name: Group by Album Name
    :type g_album_name: str
    :param page_size: Define the page size for paginated results.Range is 1 to 100.
    :type page_size: 
    :param page: Define the page number for paginated results
    :type page: 

    """
    return web.Response(status=200)
