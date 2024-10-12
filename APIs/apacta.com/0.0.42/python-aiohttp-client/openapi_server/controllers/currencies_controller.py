from typing import List, Dict
from aiohttp import web

from openapi_server.models.currencies_currency_id_get200_response import CurrenciesCurrencyIdGet200Response
from openapi_server.models.currencies_get200_response import CurrenciesGet200Response
from openapi_server.models.error_not_found import ErrorNotFound
from openapi_server import util


async def currencies_currency_id_get(request: web.Request, currency_id) -> web.Response:
    """Get details about one currency

    

    :param currency_id: 
    :type currency_id: str

    """
    return web.Response(status=200)


async def currencies_get(request: web.Request, ) -> web.Response:
    """Get list of currencies supported in Apacta

    


    """
    return web.Response(status=200)
