from typing import List, Dict
from aiohttp import web

from openapi_server.models.admin_scenarios_get200_response import AdminScenariosGet200Response
from openapi_server import util


async def admin_scenarios_get(request: web.Request, ) -> web.Response:
    """Get all scenarios

    


    """
    return web.Response(status=200)


async def admin_scenarios_reset_post(request: web.Request, ) -> web.Response:
    """Reset the state of all scenarios

    


    """
    return web.Response(status=200)
