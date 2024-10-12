from typing import List, Dict
from aiohttp import web

from openapi_server.models.search_in_index1_request import SearchInIndex1Request
from openapi_server import util


async def search_in_index(request: web.Request, q=None, offset=None, limit=None, attributes_to_retrieve=None, attributes_to_crop=None, attributes_to_highlight=None, crop_length=None, crop_marker=None, filter=None, show_matches_position=None, facets=None, sort=None, highlight_pre_tag=None, highlight_post_tag=None, matching_strategy=None, page=None, hits_per_page=None) -> web.Response:
    """Search in index

    Search in index

    :param q: 
    :type q: str
    :param offset: 
    :type offset: str
    :param limit: 
    :type limit: str
    :param attributes_to_retrieve: 
    :type attributes_to_retrieve: str
    :param attributes_to_crop: 
    :type attributes_to_crop: str
    :param attributes_to_highlight: 
    :type attributes_to_highlight: str
    :param crop_length: 
    :type crop_length: str
    :param crop_marker: 
    :type crop_marker: str
    :param filter: 
    :type filter: str
    :param show_matches_position: 
    :type show_matches_position: str
    :param facets: 
    :type facets: str
    :param sort: 
    :type sort: str
    :param highlight_pre_tag: 
    :type highlight_pre_tag: str
    :param highlight_post_tag: 
    :type highlight_post_tag: str
    :param matching_strategy: 
    :type matching_strategy: str
    :param page: 
    :type page: str
    :param hits_per_page: 
    :type hits_per_page: str

    """
    return web.Response(status=200)


async def search_in_index1(request: web.Request, body=None) -> web.Response:
    """Search in index

    Search in index

    :param body: 
    :type body: dict | bytes

    """
    body = SearchInIndex1Request.from_dict(body)
    return web.Response(status=200)
