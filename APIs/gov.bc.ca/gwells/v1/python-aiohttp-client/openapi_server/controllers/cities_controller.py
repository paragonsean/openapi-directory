from typing import List, Dict
from aiohttp import web

from openapi_server.models.city_list import CityList
from openapi_server import util


async def cities_drillers_list(request: web.Request, ) -> web.Response:
    """cities_drillers_list

    returns a list of cities with a qualified, registered operator (driller or installer)


    """
    return web.Response(status=200)


async def cities_installers_list(request: web.Request, ) -> web.Response:
    """cities_installers_list

    returns a list of cities with a qualified, registered operator (driller or installer)


    """
    return web.Response(status=200)
