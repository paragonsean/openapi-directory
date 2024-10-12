from typing import List, Dict
from aiohttp import web

from openapi_server.models.combined_result import CombinedResult
from openapi_server import util


async def get_omdb_search(request: web.Request, r, t=None, i=None, s=None, y=None, type=None, plot=None, tomatoes=None, v=None, page=None, param_callback=None) -> web.Response:
    """OMDb Search

    Find a movie, series or episode from the OMDb by title, IMDb-id or by free-text search

    :param r: The data type to return.
    :type r: str
    :param t: Movie title to search for. One of t, i or s is required.
    :type t: str
    :param i: A valid IMDb ID (e.g. tt1285016). One of t, i or s is required.
    :type i: str
    :param s: Movie title to search for. One of t, i or s is required.
    :type s: str
    :param y: Year of release.
    :type y: int
    :param type: Type of result to return.
    :type type: str
    :param plot: Return short or full plot.
    :type plot: str
    :param tomatoes: Include Rotten Tomatoes ratings.
    :type tomatoes: bool
    :param v: API version (reserved for future use).
    :type v: int
    :param page: Page number to return.
    :type page: int
    :param param_callback: JSONP callback name.
    :type param_callback: str

    """
    return web.Response(status=200)
