from typing import List, Dict
from aiohttp import web

from openapi_server.models.category_object import CategoryObject
from openapi_server.models.get_categories200_response import GetCategories200Response
from openapi_server.models.get_multiple_albums401_response import GetMultipleAlbums401Response
from openapi_server.models.paging_featured_playlist_object import PagingFeaturedPlaylistObject
from openapi_server import util


async def get_a_categories_playlists_0(request: web.Request, category_id, country=None, limit=None, offset=None) -> web.Response:
    """Get Category&#39;s Playlists 

    Get a list of Spotify playlists tagged with a particular category. 

    :param category_id: 
    :type category_id: str
    :param country: 
    :type country: str
    :param limit: 
    :type limit: int
    :param offset: 
    :type offset: int

    """
    return web.Response(status=200)


async def get_a_category(request: web.Request, category_id, country=None, locale=None) -> web.Response:
    """Get Single Browse Category 

    Get a single category used to tag items in Spotify (on, for example, the Spotify player’s “Browse” tab). 

    :param category_id: 
    :type category_id: str
    :param country: 
    :type country: str
    :param locale: 
    :type locale: str

    """
    return web.Response(status=200)


async def get_categories(request: web.Request, country=None, locale=None, limit=None, offset=None) -> web.Response:
    """Get Several Browse Categories 

    Get a list of categories used to tag items in Spotify (on, for example, the Spotify player’s “Browse” tab). 

    :param country: 
    :type country: str
    :param locale: 
    :type locale: str
    :param limit: 
    :type limit: int
    :param offset: 
    :type offset: int

    """
    return web.Response(status=200)
