from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_list_of_countries200_response_inner import GetListOfCountries200ResponseInner
from openapi_server import util


async def get_list_of_countries(request: web.Request, format=None) -> web.Response:
    """getListOfCountries

    Get name name, alpha-2, alpha-3 code, latitude and longitude for every country.

    :param format: Format of the response
    :type format: str

    """
    return web.Response(status=200)
