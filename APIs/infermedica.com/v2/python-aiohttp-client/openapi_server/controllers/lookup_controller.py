from typing import List, Dict
from aiohttp import web

from openapi_server.models.search_result import SearchResult
from openapi_server import util


async def get_matching_observation(request: web.Request, phrase, sex=None, age_value=None, age_unit=None) -> web.Response:
    """Find observation matching given phrase

    Returns a single observation matching given phrase.

    :param phrase: phrase to match
    :type phrase: str
    :param sex: sex filter
    :type sex: str
    :param age_value: age value
    :type age_value: int
    :param age_unit: unit in which age value was provided
    :type age_unit: str

    """
    return web.Response(status=200)
