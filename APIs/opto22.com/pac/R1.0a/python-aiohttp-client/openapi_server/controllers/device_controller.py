from typing import List, Dict
from aiohttp import web

from openapi_server.models.controller_response import ControllerResponse
from openapi_server.models.error_response400_bad_admin_or_value import ErrorResponse400BadAdminOrValue
from openapi_server.models.error_response401_bad_key_for_basic_auth import ErrorResponse401BadKeyForBasicAuth
from openapi_server import util


async def read_device_details_0(request: web.Request, ) -> web.Response:
    """read_device_details_0

    Returns controller&#39;s type; firmware version; both mac addresses; and uptime in seconds


    """
    return web.Response(status=200)
