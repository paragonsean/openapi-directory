from typing import List, Dict
from aiohttp import web

from openapi_server.models.countries_country_id_get200_response import CountriesCountryIdGet200Response
from openapi_server.models.countries_get200_response import CountriesGet200Response
from openapi_server.models.error_not_found import ErrorNotFound
from openapi_server import util


async def countries_country_id_get(request: web.Request, country_id) -> web.Response:
    """Get details about one country

    

    :param country_id: 
    :type country_id: str

    """
    return web.Response(status=200)


async def countries_get(request: web.Request, ) -> web.Response:
    """Get list of countries supported in Apacta

    


    """
    return web.Response(status=200)
