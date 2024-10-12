from typing import List, Dict
from aiohttp import web

from openapi_server.models.message_model import MessageModel
from openapi_server.models.segment_query_filter_config_model import SegmentQueryFilterConfigModel
from openapi_server.models.segment_query_filter_list_model import SegmentQueryFilterListModel
from openapi_server import util


async def get_segment_query_filters_config_using_get(request: web.Request, api_key) -> web.Response:
    """getSegmentQueryFiltersConfig

    

    :param api_key: apiKey
    :type api_key: str

    """
    return web.Response(status=200)


async def get_segment_query_filters_using_get(request: web.Request, api_key) -> web.Response:
    """getSegmentQueryFilters

    

    :param api_key: apiKey
    :type api_key: str

    """
    return web.Response(status=200)


async def get_segment_query_standard_filters_using_get(request: web.Request, api_key) -> web.Response:
    """getSegmentQueryStandardFilters

    

    :param api_key: apiKey
    :type api_key: str

    """
    return web.Response(status=200)


async def update_segment_query_filters_config_using_put(request: web.Request, api_key, body) -> web.Response:
    """updateSegmentQueryFiltersConfig

    

    :param api_key: apiKey
    :type api_key: str
    :param body: segmentQueryConfig
    :type body: dict | bytes

    """
    body = SegmentQueryFilterConfigModel.from_dict(body)
    return web.Response(status=200)
