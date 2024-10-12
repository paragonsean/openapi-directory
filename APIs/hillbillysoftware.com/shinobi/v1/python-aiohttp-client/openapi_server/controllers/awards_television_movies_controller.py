from typing import List, Dict
from aiohttp import web

from openapi_server.models.awards import Awards
from openapi_server import util


async def awards_get(request: web.Request, year) -> web.Response:
    """Gets all awards for requested year

    

    :param year: 
    :type year: str

    """
    return web.Response(status=200)


async def awardsby_winner_get(request: web.Request, access_token, nominee) -> web.Response:
    """Gets all awards by nominiee

    

    :param access_token: 
    :type access_token: str
    :param nominee: 
    :type nominee: str

    """
    return web.Response(status=200)
