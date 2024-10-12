from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_countries_dict_out import GetCountriesDictOut
from openapi_server.models.get_currencies_dict_out import GetCurrenciesDictOut
from openapi_server.models.get_product_types_dict_out import GetProductTypesDictOut
from openapi_server import util


async def get_countries_dict(request: web.Request, tax_supported=None) -> web.Response:
    """Countries

    

    :param tax_supported: Should only countries with tax supported be listed?
    :type tax_supported: bool

    """
    return web.Response(status=200)


async def get_currencies_dict(request: web.Request, ) -> web.Response:
    """Currencies

    


    """
    return web.Response(status=200)


async def get_product_types_dict(request: web.Request, ) -> web.Response:
    """Product types

    


    """
    return web.Response(status=200)
