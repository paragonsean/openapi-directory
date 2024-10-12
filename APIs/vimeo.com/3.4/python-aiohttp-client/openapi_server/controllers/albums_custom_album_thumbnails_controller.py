from typing import List, Dict
from aiohttp import web

from openapi_server.models.legacy_error import LegacyError
from openapi_server.models.picture import Picture
from openapi_server.models.replace_album_custom_thumb_request import ReplaceAlbumCustomThumbRequest
from openapi_server import util


async def create_album_custom_thumb(request: web.Request, album_id, user_id) -> web.Response:
    """Add a custom uploaded thumbnail

    

    :param album_id: The ID of the album.
    :type album_id: 
    :param user_id: The ID of the user.
    :type user_id: 

    """
    return web.Response(status=200)


async def delete_album_custom_thumbnail(request: web.Request, album_id, thumbnail_id, user_id) -> web.Response:
    """Remove a custom uploaded album thumbnail

    This method removes a custom uploaded thumbnail from the specified album.

    :param album_id: The ID of the album.
    :type album_id: 
    :param thumbnail_id: The ID of the custom thumbnail.
    :type thumbnail_id: 
    :param user_id: The ID of the user.
    :type user_id: 

    """
    return web.Response(status=200)


async def get_album_custom_thumbnail(request: web.Request, album_id, thumbnail_id, user_id) -> web.Response:
    """Get a specific custom uploaded album thumbnail

    

    :param album_id: The ID of the album.
    :type album_id: 
    :param thumbnail_id: The ID of the custom thumbnail.
    :type thumbnail_id: 
    :param user_id: The ID of the user.
    :type user_id: 

    """
    return web.Response(status=200)


async def get_album_custom_thumbs(request: web.Request, album_id, user_id, page=None, per_page=None) -> web.Response:
    """Get all the custom upload thumbnails of an album

    

    :param album_id: The ID of the album.
    :type album_id: 
    :param user_id: The ID of the user.
    :type user_id: 
    :param page: The page number of the results to show.
    :type page: 
    :param per_page: The number of items to show on each page of results, up to a maximum of 100.
    :type per_page: 

    """
    return web.Response(status=200)


async def replace_album_custom_thumb(request: web.Request, album_id, thumbnail_id, user_id, body=None) -> web.Response:
    """Replace a custom uploaded album thumbnail

    

    :param album_id: The ID of the album.
    :type album_id: 
    :param thumbnail_id: The ID of the custom thumbnail.
    :type thumbnail_id: 
    :param user_id: The ID of the user.
    :type user_id: 
    :param body: 
    :type body: dict | bytes

    """
    body = ReplaceAlbumCustomThumbRequest.from_dict(body)
    return web.Response(status=200)
