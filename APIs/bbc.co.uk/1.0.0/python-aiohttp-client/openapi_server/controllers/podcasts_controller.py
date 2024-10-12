from typing import List, Dict
from aiohttp import web

from openapi_server.models.podcast_episodes_response import PodcastEpisodesResponse
from openapi_server.models.podcast_error_response import PodcastErrorResponse
from openapi_server.models.podcasts_featured_response import PodcastsFeaturedResponse
from openapi_server.models.podcasts_response import PodcastsResponse
from openapi_server import util


async def get_podcast_by_pid(request: web.Request, x_api_key, pid, offset=None, limit=None) -> web.Response:
    """Podcast

    Retrieve data about the podcast with the supplied PID 

    :param x_api_key: API_KEY
    :type x_api_key: str
    :param pid: pid
    :type pid: str
    :param offset: Paginated results offset
    :type offset: int
    :param limit: Paginated results limit
    :type limit: int

    """
    return web.Response(status=200)


async def get_podcast_episodes(request: web.Request, x_api_key, pid, offset=None, limit=None) -> web.Response:
    """Podcast Episodes

    Retrieve all episodes for a specific podcast 

    :param x_api_key: API_KEY
    :type x_api_key: str
    :param pid: pid
    :type pid: str
    :param offset: Paginated results offset
    :type offset: int
    :param limit: Paginated results limit
    :type limit: int

    """
    return web.Response(status=200)


async def get_podcasts(request: web.Request, x_api_key, offset=None, limit=None, sort=None, network=None, network_url_key=None, category=None, q=None, coverage=None) -> web.Response:
    """All Podcasts

    Retrieve all Podcasts 

    :param x_api_key: API_KEY
    :type x_api_key: str
    :param offset: Paginated results offset
    :type offset: int
    :param limit: Paginated results limit
    :type limit: int
    :param sort: Sort order for Podcasts results
    :type sort: str
    :param network: Network Master Brand ID (mid)
    :type network: str
    :param network_url_key: Network URL key
    :type network_url_key: str
    :param category: Category ID
    :type category: str
    :param q: Search query String
    :type q: str
    :param coverage: Local, National or Regional Coverage
    :type coverage: str

    """
    return web.Response(status=200)


async def get_podcasts_featured(request: web.Request, x_api_key) -> web.Response:
    """Featured Podcasts

    Retrieve featured podcasts 

    :param x_api_key: API_KEY
    :type x_api_key: str

    """
    return web.Response(status=200)
