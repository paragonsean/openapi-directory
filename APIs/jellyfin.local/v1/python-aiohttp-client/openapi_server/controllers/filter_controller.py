from typing import List, Dict
from aiohttp import web

from openapi_server.models.query_filters import QueryFilters
from openapi_server.models.query_filters_legacy import QueryFiltersLegacy
from openapi_server import util


async def get_query_filters(request: web.Request, user_id=None, parent_id=None, include_item_types=None, is_airing=None, is_movie=None, is_sports=None, is_kids=None, is_news=None, is_series=None, recursive=None) -> web.Response:
    """Gets query filters.

    

    :param user_id: Optional. User id.
    :type user_id: str
    :type user_id: str
    :param parent_id: Optional. Specify this to localize the search to a specific item or folder. Omit to use the root.
    :type parent_id: str
    :type parent_id: str
    :param include_item_types: Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimited.
    :type include_item_types: List[str]
    :param is_airing: Optional. Is item airing.
    :type is_airing: bool
    :param is_movie: Optional. Is item movie.
    :type is_movie: bool
    :param is_sports: Optional. Is item sports.
    :type is_sports: bool
    :param is_kids: Optional. Is item kids.
    :type is_kids: bool
    :param is_news: Optional. Is item news.
    :type is_news: bool
    :param is_series: Optional. Is item series.
    :type is_series: bool
    :param recursive: Optional. Search recursive.
    :type recursive: bool

    """
    return web.Response(status=200)


async def get_query_filters_legacy(request: web.Request, user_id=None, parent_id=None, include_item_types=None, media_types=None) -> web.Response:
    """Gets legacy query filters.

    

    :param user_id: Optional. User id.
    :type user_id: str
    :type user_id: str
    :param parent_id: Optional. Parent id.
    :type parent_id: str
    :type parent_id: str
    :param include_item_types: Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimited.
    :type include_item_types: List[str]
    :param media_types: Optional. Filter by MediaType. Allows multiple, comma delimited.
    :type media_types: List[str]

    """
    return web.Response(status=200)
