from typing import List, Dict
from aiohttp import web

from openapi_server.models.search_hint_result import SearchHintResult
from openapi_server import util


async def get(request: web.Request, search_term, start_index=None, limit=None, user_id=None, include_item_types=None, exclude_item_types=None, media_types=None, parent_id=None, is_movie=None, is_series=None, is_news=None, is_kids=None, is_sports=None, include_people=None, include_media=None, include_genres=None, include_studios=None, include_artists=None) -> web.Response:
    """Gets the search hint result.

    

    :param search_term: The search term to filter on.
    :type search_term: str
    :param start_index: Optional. The record index to start at. All items with a lower index will be dropped from the results.
    :type start_index: int
    :param limit: Optional. The maximum number of records to return.
    :type limit: int
    :param user_id: Optional. Supply a user id to search within a user&#39;s library or omit to search all.
    :type user_id: str
    :type user_id: str
    :param include_item_types: If specified, only results with the specified item types are returned. This allows multiple, comma delimeted.
    :type include_item_types: List[str]
    :param exclude_item_types: If specified, results with these item types are filtered out. This allows multiple, comma delimeted.
    :type exclude_item_types: List[str]
    :param media_types: If specified, only results with the specified media types are returned. This allows multiple, comma delimeted.
    :type media_types: List[str]
    :param parent_id: If specified, only children of the parent are returned.
    :type parent_id: str
    :type parent_id: str
    :param is_movie: Optional filter for movies.
    :type is_movie: bool
    :param is_series: Optional filter for series.
    :type is_series: bool
    :param is_news: Optional filter for news.
    :type is_news: bool
    :param is_kids: Optional filter for kids.
    :type is_kids: bool
    :param is_sports: Optional filter for sports.
    :type is_sports: bool
    :param include_people: Optional filter whether to include people.
    :type include_people: bool
    :param include_media: Optional filter whether to include media.
    :type include_media: bool
    :param include_genres: Optional filter whether to include genres.
    :type include_genres: bool
    :param include_studios: Optional filter whether to include studios.
    :type include_studios: bool
    :param include_artists: Optional filter whether to include artists.
    :type include_artists: bool

    """
    return web.Response(status=200)
