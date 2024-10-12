from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_jo import ErrorJO
from openapi_server.models.rental_object_jo import RentalObjectJO
from openapi_server import util


async def get_rental_object(request: web.Request, rental_object_uid, providernetwork_uid, expand=None) -> web.Response:
    """Get information about the RentalObject.

    Get information about the Rental Object. 

    :param rental_object_uid: 
    :type rental_object_uid: str
    :param providernetwork_uid: 
    :type providernetwork_uid: str
    :param expand: 
    :type expand: str

    """
    return web.Response(status=200)
