from typing import List, Dict
from aiohttp import web

from openapi_server.models.cities_city_id_get200_response import CitiesCityIdGet200Response
from openapi_server.models.cities_get200_response import CitiesGet200Response
from openapi_server.models.error_not_found import ErrorNotFound
from openapi_server import util


async def cities_city_id_get(request: web.Request, city_id) -> web.Response:
    """Get details about one city

    

    :param city_id: 
    :type city_id: str

    """
    return web.Response(status=200)


async def cities_get(request: web.Request, zip_code=None, name=None, include_all=None) -> web.Response:
    """Get list of cities supported in Apacta

    

    :param zip_code: Used to search for a city with specific zip code
    :type zip_code: str
    :param name: Used to search for a city by name
    :type name: str
    :param include_all: Used to search for a city without filtering by country
    :type include_all: bool

    """
    return web.Response(status=200)
