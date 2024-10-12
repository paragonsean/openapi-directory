from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.popular_error_response import PopularErrorResponse
from openapi_server.models.popular_response import PopularResponse
from openapi_server.models.programmes_response import ProgrammesResponse
from openapi_server.models.radio_error_response import RadioErrorResponse
from openapi_server import util


async def get_popular_episodes_clips(request: web.Request, x_api_key, type=None, distinct=None, network=None, network_url_key=None, category=None, format=None, group=None, media_type=None, container=None, media_set=None, q=None) -> web.Response:
    """Popular Episodes &amp; Clips

    Retrieve Popular Episodes &amp; Clips 

    :param x_api_key: API_KEY
    :type x_api_key: str
    :param type: Programme type required. Accepts comma separated values
    :type type: str
    :param distinct: Filter by deduplication rule. E.g. &#39;tleo&#39; returns programmes with distinct top level episode objects
    :type distinct: str
    :param network: Filter by network master brand ID (mid). Accepts comma separated values
    :type network: str
    :param network_url_key: Filter by network URL key. Accepts comma separated values
    :type network_url_key: str
    :param category: Filter by category. Accepts comma separated values
    :type category: str
    :param format: Filter by format. Accepts comma separated values
    :type format: str
    :param group: Filter by group. Accepts comma separated values
    :type group: str
    :param media_type: Filter by programme media type. Accepts comma separated values
    :type media_type: str
    :param container: Filter by container. Accepts any pid e.g. brand,series,episode
    :type container: str
    :param media_set: Filter by media set name. Accepts comma separated combinations of the following: pc,mobile-download,android-download-high,apple-ios-download-high,mobile-cellular-main,mobile-phone-main,iptv-all
    :type media_set: List[]
    :param q: Search query String
    :type q: str

    """
    return web.Response(status=200)


async def get_radio_programmes(request: web.Request, x_api_key, kind=None, network=None, network_url_key=None, category=None, sort=None, container=None, type=None) -> web.Response:
    """Radio programmes

    Provides a paginated list of programmes by PID (brand, series, episode and clip). Accepts various filters and sorting methods.  N.B.  Swagger schemas cannot currently handle multiple combinations of object in an array i.e. a mix of Episode and Clip Summaries so we are defining results as an array of Programme Summary here.  This will be resolved in V3 with full support for  anyOf https://www.openapis.org/blog/2017/01/24/a-new-year-a-new-specification 

    :param x_api_key: API_KEY
    :type x_api_key: str
    :param kind: Filter by provided query. E.g. &#39;tleo&#39; returns top level objects, ie. brands, orphaned series, and orphaned episodes
    :type kind: str
    :param network: Filter by network master brand ID (mid). Accepts comma separated values
    :type network: str
    :param network_url_key: Filter by network URL key. Accepts comma separated values
    :type network_url_key: str
    :param category: Filter by category id. Accepts comma separated values. See /category endpoint below for the type of response provided
    :type category: str
    :param sort: Sort by provided query. E.g. &#39;title&#39; sorts in ascending order, and -title sorts in descending order
    :type sort: str
    :param container: Filter by container. Accepts any brand or series pid
    :type container: str
    :param type: Filter by programme type. Accepts comma separated values
    :type type: str

    """
    return web.Response(status=200)


async def get_radio_programmes_by_pid(request: web.Request, x_api_key, pid) -> web.Response:
    """Available radio programme by Pid

    Find programmes by PID (brand, series, episode and clip)  N.B.  Swagger schemas cannot currently handle multiple combinations of object in an array i.e. a mix of Episode and Clip Summaries so we are defining results as an array of Programme Summary here.  This will be resolved in V3 with full support for  anyOf https://www.openapis.org/blog/2017/01/24/a-new-year-a-new-specification 

    :param x_api_key: API_KEY
    :type x_api_key: str
    :param pid: pid
    :type pid: str

    """
    return web.Response(status=200)


async def get_recommendations(request: web.Request, authorization, x_api_key, rights, offset=None, limit=None) -> web.Response:
    """Recommended Programmes

    Recommended Programmes from the Audience Platforms&#39; Recomendations Service 

    :param authorization: Bearer OAUTH_TOKEN
    :type authorization: str
    :param x_api_key: API_KEY
    :type x_api_key: str
    :param rights: Only return available results for the web/mobile.
    :type rights: str
    :param offset: Paginated results offset
    :type offset: int
    :param limit: Paginated results limit
    :type limit: int

    """
    return web.Response(status=200)
