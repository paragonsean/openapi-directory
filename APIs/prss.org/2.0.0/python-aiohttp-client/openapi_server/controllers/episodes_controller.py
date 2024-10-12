from typing import List, Dict
from aiohttp import web

from openapi_server.models.episode import Episode
from openapi_server.models.error import Error
from openapi_server import util


async def api_v2_episodes_get(request: web.Request, program_id, id=None, begin_air_date_after=None, end_air_date_before=None, page_start=None, page_size=None, order_by_id=None) -> web.Response:
    """Gets episodes matching the given criteria.

    

    :param program_id: Matches on the ID of the program that owns the episode.
    :type program_id: int
    :param id: Matches on the ID of the episode.
    :type id: int
    :param begin_air_date_after: Matches on the begin air date of the episode (inclusive).
    :type begin_air_date_after: str
    :param end_air_date_before: Matches on the end air date of the episode (inclusive).
    :type end_air_date_before: str
    :param page_start: The start page of the results to return. The first item is indexed at 0.
    :type page_start: int
    :param page_size: The number of items to return. Must be between 0 and 500, inclusive.
    :type page_size: int
    :param order_by_id: The sort order of the list of episodes, based on episode ID. If unspecified, the episodes are returned in random order. If using paging to iterate through the results, sort order should be specified.
    :type order_by_id: str

    """
    begin_air_date_after = util.deserialize_datetime(begin_air_date_after)
    end_air_date_before = util.deserialize_datetime(end_air_date_before)
    return web.Response(status=200)


async def api_v2_episodes_id_get(request: web.Request, id) -> web.Response:
    """Returns the episode matching the given ID.

    

    :param id: The ID of the episode to operate on.
    :type id: int

    """
    return web.Response(status=200)
