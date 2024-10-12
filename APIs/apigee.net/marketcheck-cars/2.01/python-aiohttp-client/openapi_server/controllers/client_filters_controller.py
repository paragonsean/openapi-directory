from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get(request: web.Request, country, api_key=None) -> web.Response:
    """get client filters

    get client filters

    :param country: To filter listing on Country in which they are listed
    :type country: str
    :param api_key: The API Authentication Key. Mandatory with all API calls.
    :type api_key: str

    """
    return web.Response(status=200)


async def set(request: web.Request, country, csvfile, api_key=None) -> web.Response:
    """set client filters

    set client filters

    :param country: To filter listing on Country in which they are listed
    :type country: str
    :param csvfile: csv file with filters
    :type csvfile: str
    :param api_key: The API Authentication Key. Mandatory with all API calls.
    :type api_key: str

    """
    return web.Response(status=200)
