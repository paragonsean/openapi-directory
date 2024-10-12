from typing import List, Dict
from aiohttp import web

from openapi_server.models.artist_get_get200_response import ArtistGetGet200Response
from openapi_server.models.artist_related_get_get200_response import ArtistRelatedGetGet200Response
from openapi_server.models.chart_artists_get_get200_response import ChartArtistsGetGet200Response
from openapi_server import util


async def artist_get_get(request: web.Request, artist_id, format=None, param_callback=None) -> web.Response:
    """artist_get_get

    

    :param artist_id:  The musiXmatch artist id
    :type artist_id: str
    :param format: output format: json, jsonp, xml.
    :type format: str
    :param param_callback: jsonp callback
    :type param_callback: str

    """
    return web.Response(status=200)


async def artist_related_get_get(request: web.Request, artist_id, format=None, param_callback=None, page_size=None, page=None) -> web.Response:
    """artist_related_get_get

    

    :param artist_id: The musiXmatch artist id
    :type artist_id: str
    :param format: output format: json, jsonp, xml.
    :type format: str
    :param param_callback: jsonp callback
    :type param_callback: str
    :param page_size: Define the page size for paginated results.Range is 1 to 100.
    :type page_size: 
    :param page: Define the page number for paginated results
    :type page: 

    """
    return web.Response(status=200)


async def artist_search_get(request: web.Request, format=None, param_callback=None, q_artist=None, f_artist_id=None, page=None, page_size=None) -> web.Response:
    """artist_search_get

    

    :param format: output format: json, jsonp, xml.
    :type format: str
    :param param_callback: jsonp callback
    :type param_callback: str
    :param q_artist: The song artist
    :type q_artist: str
    :param f_artist_id: When set, filter by this artist id
    :type f_artist_id: 
    :param page: Define the page number for paginated results
    :type page: 
    :param page_size: Define the page size for paginated results.Range is 1 to 100.
    :type page_size: 

    """
    return web.Response(status=200)


async def chart_artists_get_get(request: web.Request, format=None, param_callback=None, page=None, page_size=None, country=None) -> web.Response:
    """chart_artists_get_get

    

    :param format: output format: json, jsonp, xml.
    :type format: str
    :param param_callback: jsonp callback
    :type param_callback: str
    :param page: Define the page number for paginated results
    :type page: 
    :param page_size: Define the page size for paginated results.Range is 1 to 100.
    :type page_size: 
    :param country: A valid ISO 3166 country code
    :type country: str

    """
    return web.Response(status=200)
