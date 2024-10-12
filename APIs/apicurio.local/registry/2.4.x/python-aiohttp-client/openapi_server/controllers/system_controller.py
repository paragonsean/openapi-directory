from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.limits import Limits
from openapi_server.models.system_info import SystemInfo
from openapi_server import util


async def get_resource_limits(request: web.Request, ) -> web.Response:
    """Get resource limits information

    This operation retrieves the list of limitations on used resources, that are applied on the current instance of Registry.


    """
    return web.Response(status=200)


async def get_system_info(request: web.Request, ) -> web.Response:
    """Get system information

    This operation retrieves information about the running registry system, such as the version of the software and when it was built.


    """
    return web.Response(status=200)
