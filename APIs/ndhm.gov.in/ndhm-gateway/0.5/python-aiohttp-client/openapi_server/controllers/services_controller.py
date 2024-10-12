from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.service_profile_response import ServiceProfileResponse
from openapi_server import util


async def v05_hi_services_service_id_get(request: web.Request, authorization, service_id) -> web.Response:
    """Get bridge service details/profile by the serviceId provided.

    This API is meant for displaying the bridge service details by the serviceId provided . 

    :param authorization: Access token which was issued after successful login with gateway auth server.
    :type authorization: str
    :param service_id: 
    :type service_id: str

    """
    return web.Response(status=200)
