from typing import List, Dict
from aiohttp import web

from openapi_server.models.episode import Episode
from openapi_server.models.last_available_season import LastAvailableSeason
from openapi_server.models.post_result import PostResult
from openapi_server.models.show_status import ShowStatus
from openapi_server.models.tv_information import TVInformation
from openapi_server.models.tv_information_post import TVInformationPost
from openapi_server.models.tv_show_seasons import TVShowSeasons
from openapi_server import util


async def add_tv_show_post(request: web.Request, value) -> web.Response:
    """Add new show to database

    

    :param value: 
    :type value: dict | bytes

    """
    value = TVInformationPost.from_dict(value)
    return web.Response(status=200)


async def episodes_by_id_get(request: web.Request, access_token, id) -> web.Response:
    """Gets all episodes for selected ID

    

    :param access_token: 
    :type access_token: str
    :param id: imdbID
    :type id: str

    """
    return web.Response(status=200)


async def episodes_by_season_get(request: web.Request, access_token, id, season) -> web.Response:
    """Gets list of episodes for specified imdbID and Season number

    

    :param access_token: 
    :type access_token: str
    :param id: imdbID
    :type id: str
    :param season: Season number
    :type season: str

    """
    return web.Response(status=200)


async def episodes_get(request: web.Request, access_token, showname) -> web.Response:
    """Gets all episodes for selected show

    

    :param access_token: 
    :type access_token: str
    :param showname: 
    :type showname: str

    """
    return web.Response(status=200)


async def episodes_last_available_season_get(request: web.Request, access_token, id) -> web.Response:
    """Returns last available season number in database, based on passed imdbID

    

    :param access_token: 
    :type access_token: str
    :param id: imdbID
    :type id: str

    """
    return web.Response(status=200)


async def episodes_last_available_seasonby_name_get(request: web.Request, access_token, name) -> web.Response:
    """Gets latest season number based on show name

    

    :param access_token: 
    :type access_token: str
    :param name: 
    :type name: str

    """
    return web.Response(status=200)


async def episodes_season_count_get(request: web.Request, access_token, id) -> web.Response:
    """Returns number of available seasons and episodes

    

    :param access_token: 
    :type access_token: str
    :param id: imdbID
    :type id: str

    """
    return web.Response(status=200)


async def show_status_get(request: web.Request, access_token, query) -> web.Response:
    """Returns status of queried show (query can be IMDB, TVDB, or showname)

    

    :param access_token: 
    :type access_token: str
    :param query: Query can be IMDB, TVDB, or Show name
    :type query: str

    """
    return web.Response(status=200)


async def t_v_show_by_name_get(request: web.Request, access_token, query) -> web.Response:
    """Returns results based on query, result set limited to 5 records

    

    :param access_token: 
    :type access_token: str
    :param query: 
    :type query: str

    """
    return web.Response(status=200)


async def t_v_show_id_get(request: web.Request, accesstoken, id, imdb_id) -> web.Response:
    """Returns TVShow information based on IMDBid

    

    :param accesstoken: 
    :type accesstoken: str
    :param id: imdbID of show you want info on
    :type id: str
    :param imdb_id: 
    :type imdb_id: str

    """
    return web.Response(status=200)
