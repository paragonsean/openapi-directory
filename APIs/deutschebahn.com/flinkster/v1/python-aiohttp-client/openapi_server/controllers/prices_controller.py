from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_jo import ErrorJO
from openapi_server.models.rental_object_jo import RentalObjectJO
from openapi_server import util


async def get_prices(request: web.Request, providernetwork_uid) -> web.Response:
    """Get information about the prices.

    Prices of a rental object by query params. The params depend on the price determination strategy of the provider network. 

    :param providernetwork_uid: 
    :type providernetwork_uid: str

    """
    return web.Response(status=200)
