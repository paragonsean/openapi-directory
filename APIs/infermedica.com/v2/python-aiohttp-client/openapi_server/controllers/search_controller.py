from typing import List, Dict
from aiohttp import web

from openapi_server.models.search_result import SearchResult
from openapi_server import util


async def get_matching_observations(request: web.Request, phrase, sex=None, age_value=None, age_unit=None, max_results=None, type=None) -> web.Response:
    """Find observations matching given phrase

    Returns list of observations matching the given phrase.

    :param phrase: phrase to match
    :type phrase: str
    :param sex: sex filter
    :type sex: str
    :param age_value: age value
    :type age_value: int
    :param age_unit: unit in which age value was provided
    :type age_unit: str
    :param max_results: maximum number of results
    :type max_results: int
    :param type: type of results
    :type type: List[str]

    """
    return web.Response(status=200)
