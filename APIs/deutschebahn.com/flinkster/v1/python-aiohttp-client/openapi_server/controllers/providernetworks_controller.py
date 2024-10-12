from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_jo import ErrorJO
from openapi_server.models.rental_object_jo import RentalObjectJO
from openapi_server import util


async def get_provider_network(request: web.Request, uid) -> web.Response:
    """Get information about the ProviderNetworkResources.

    Get information about the ProviderNetworkResources. 

    :param uid: 
    :type uid: str

    """
    return web.Response(status=200)
