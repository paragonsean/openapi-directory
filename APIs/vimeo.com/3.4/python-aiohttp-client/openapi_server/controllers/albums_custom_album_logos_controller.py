from typing import List, Dict
from aiohttp import web

from openapi_server.models.legacy_error import LegacyError
from openapi_server.models.picture import Picture
from openapi_server.models.replace_album_logo_request import ReplaceAlbumLogoRequest
from openapi_server import util


async def create_album_logo(request: web.Request, album_id, user_id) -> web.Response:
    """Add a custom album logo

    

    :param album_id: The ID of the album.
    :type album_id: 
    :param user_id: The ID of the user.
    :type user_id: 

    """
    return web.Response(status=200)


async def delete_album_logo(request: web.Request, album_id, logo_id, user_id) -> web.Response:
    """Remove a custom album logo

    This method removes a custom logo from the specified album.

    :param album_id: The ID of the album.
    :type album_id: 
    :param logo_id: The ID of the custom logo.
    :type logo_id: 
    :param user_id: The ID of the user.
    :type user_id: 

    """
    return web.Response(status=200)


async def get_album_logo(request: web.Request, album_id, logo_id, user_id) -> web.Response:
    """Get a specific custom album logo

    

    :param album_id: The ID of the album.
    :type album_id: 
    :param logo_id: The ID of the custom logo.
    :type logo_id: 
    :param user_id: The ID of the user.
    :type user_id: 

    """
    return web.Response(status=200)


async def get_album_logos(request: web.Request, album_id, user_id, page=None, per_page=None) -> web.Response:
    """Get all the custom logos of an album

    

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


async def replace_album_logo(request: web.Request, album_id, logo_id, user_id, body=None) -> web.Response:
    """Replace a custom album logo

    

    :param album_id: The ID of the album.
    :type album_id: 
    :param logo_id: The ID of the custom logo.
    :type logo_id: 
    :param user_id: The ID of the user.
    :type user_id: 
    :param body: 
    :type body: dict | bytes

    """
    body = ReplaceAlbumLogoRequest.from_dict(body)
    return web.Response(status=200)
