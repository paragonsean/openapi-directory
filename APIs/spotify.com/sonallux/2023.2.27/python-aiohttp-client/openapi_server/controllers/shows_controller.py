from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_multiple_albums401_response import GetMultipleAlbums401Response
from openapi_server.models.get_multiple_shows200_response import GetMultipleShows200Response
from openapi_server.models.paging_saved_show_object import PagingSavedShowObject
from openapi_server.models.paging_simplified_episode_object import PagingSimplifiedEpisodeObject
from openapi_server.models.save_shows_user_request import SaveShowsUserRequest
from openapi_server.models.show_object import ShowObject
from openapi_server import util


async def check_users_saved_shows(request: web.Request, ids) -> web.Response:
    """Check User&#39;s Saved Shows 

    Check if one or more shows is already saved in the current Spotify user&#39;s library. 

    :param ids: 
    :type ids: str

    """
    return web.Response(status=200)


async def get_a_show(request: web.Request, id, market=None) -> web.Response:
    """Get Show 

    Get Spotify catalog information for a single show identified by its unique Spotify ID. 

    :param id: 
    :type id: str
    :param market: 
    :type market: str

    """
    return web.Response(status=200)


async def get_a_shows_episodes(request: web.Request, id, market=None, limit=None, offset=None) -> web.Response:
    """Get Show Episodes 

    Get Spotify catalog information about an show’s episodes. Optional parameters can be used to limit the number of episodes returned. 

    :param id: 
    :type id: str
    :param market: 
    :type market: str
    :param limit: 
    :type limit: int
    :param offset: 
    :type offset: int

    """
    return web.Response(status=200)


async def get_multiple_shows(request: web.Request, ids, market=None) -> web.Response:
    """Get Several Shows 

    Get Spotify catalog information for several shows based on their Spotify IDs. 

    :param ids: 
    :type ids: str
    :param market: 
    :type market: str

    """
    return web.Response(status=200)


async def get_users_saved_shows(request: web.Request, limit=None, offset=None) -> web.Response:
    """Get User&#39;s Saved Shows 

    Get a list of shows saved in the current Spotify user&#39;s library. Optional parameters can be used to limit the number of shows returned. 

    :param limit: 
    :type limit: int
    :param offset: 
    :type offset: int

    """
    return web.Response(status=200)


async def remove_shows_user(request: web.Request, ids, market=None, body=None) -> web.Response:
    """Remove User&#39;s Saved Shows 

    Delete one or more shows from current Spotify user&#39;s library. 

    :param ids: 
    :type ids: str
    :param market: 
    :type market: str
    :param body: 
    :type body: dict | bytes

    """
    body = SaveShowsUserRequest.from_dict(body)
    return web.Response(status=200)


async def save_shows_user(request: web.Request, ids, body=None) -> web.Response:
    """Save Shows for Current User 

    Save one or more shows to current Spotify user&#39;s library. 

    :param ids: 
    :type ids: str
    :param body: 
    :type body: dict | bytes

    """
    body = SaveShowsUserRequest.from_dict(body)
    return web.Response(status=200)
