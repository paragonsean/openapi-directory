from typing import List, Dict
from aiohttp import web

from openapi_server.models.magnets import Magnets
from openapi_server import util


async def magnets_by_date_get_async(request: web.Request, access_token, _date) -> web.Response:
    """Gets available magnet hashes on passed date (yyyy-mm-dd).  Feature not available on free plan, please donate to be able to use this feature.

    

    :param access_token: 
    :type access_token: str
    :param _date: 
    :type _date: str

    """
    return web.Response(status=200)


async def magnets_byimdb_id_get_async(request: web.Request, access_token, imdb_id) -> web.Response:
    """Returns list of magnet hashes for passed IMDBID.  Feature not available on free plan, please donate to be able to use this feature.

    

    :param access_token: 
    :type access_token: str
    :param imdb_id: ID with or without tt prefix
    :type imdb_id: str

    """
    return web.Response(status=200)


async def magnets_movie_by_id_get_async(request: web.Request, access_token, query) -> web.Response:
    """Try and find magnet links for queried movie.  Feature not available on free plan, please donate to be able to use this feature

    

    :param access_token: 
    :type access_token: str
    :param query: Name or part of name of movie or tv show
    :type query: str

    """
    return web.Response(status=200)


async def t_v_showsearch_get(request: web.Request, access_token, tv_show) -> web.Response:
    """Returns results based on query, Feature not available on free plan, please donate to be able to use this feature.

    

    :param access_token: 
    :type access_token: str
    :param tv_show: 
    :type tv_show: str

    """
    return web.Response(status=200)
