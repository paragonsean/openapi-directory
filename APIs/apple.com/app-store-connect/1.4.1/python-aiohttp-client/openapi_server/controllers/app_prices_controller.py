from typing import List, Dict
from aiohttp import web

from openapi_server.models.app_price_response import AppPriceResponse
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def app_prices_get_instance(request: web.Request, id, fields_app_prices=None, include=None) -> web.Response:
    """app_prices_get_instance

    

    :param id: the id of the requested resource
    :type id: str
    :param fields_app_prices: the fields to include for returned resources of type appPrices
    :type fields_app_prices: List[str]
    :param include: comma-separated list of relationships to include
    :type include: List[str]

    """
    return web.Response(status=200)
