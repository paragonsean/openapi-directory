from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_movie_recommendations(request: web.Request, ignore_collected=None, ignore_watchlisted=None, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get movie recommendations

    #### &amp;#128274; OAuth Required &amp;#10024; Extended Info  Movie recommendations for a user. By default, &#x60;10&#x60; results are returned. You can send a &#x60;limit&#x60; to get up to &#x60;100&#x60; results per page. Set &#x60;ignore_collected&#x3D;true&#x60; to filter out movies the user has already collected or &#x60;ignore_watchlisted&#x3D;true&#x60; to filter out movies the user has already watchlisted.  The &#x60;recommended_by&#x60; array contains all users who recommended the item along with any notes they added.

    :param ignore_collected: filter out collected movies
    :type ignore_collected: str
    :param ignore_watchlisted: filter out watchlisted movies
    :type ignore_watchlisted: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def get_show_recommendations(request: web.Request, ignore_collected=None, ignore_watchlisted=None, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get show recommendations

    #### &amp;#128274; OAuth Required &amp;#10024; Extended Info  TV show recommendations for a user. By default, &#x60;10&#x60; results are returned. You can send a &#x60;limit&#x60; to get up to &#x60;100&#x60; results per page. Set &#x60;ignore_collected&#x3D;true&#x60; to filter out shows the user has already collected or &#x60;ignore_watchlisted&#x3D;true&#x60; to filter out shows the user has already watchlisted.  The &#x60;recommended_by&#x60; array contains all users who recommended the item along with any notes they added.

    :param ignore_collected: filter out collected shows
    :type ignore_collected: str
    :param ignore_watchlisted: filter out watchlisted movies
    :type ignore_watchlisted: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def hide_a_movie_recommendation(request: web.Request, id, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Hide a movie recommendation

    #### &amp;#128274; OAuth Required  Hide a movie from getting recommended anymore.

    :param id: Trakt ID, Trakt slug, or IMDB ID
    :type id: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def hide_a_show_recommendation(request: web.Request, id, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Hide a show recommendation

    #### &amp;#128274; OAuth Required  Hide a show from getting recommended anymore.

    :param id: Trakt ID, Trakt slug, or IMDB ID
    :type id: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)
