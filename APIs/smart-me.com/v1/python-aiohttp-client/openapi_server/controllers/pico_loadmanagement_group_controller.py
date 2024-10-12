from typing import List, Dict
from aiohttp import web

from openapi_server.models.pico_loadmanagement_group_dto import PicoLoadmanagementGroupDto
from openapi_server import util


async def api_pico_loadmanagementgroup_get(request: web.Request, ) -> web.Response:
    """GET: api/pico/loadmanagementgroup                            Returns all available load management groups

    


    """
    return web.Response(status=200)


async def pico_loadmanagement_group_get(request: web.Request, id) -> web.Response:
    """GET: api/pico/loadmanagementgroup                            Returns a pico load management group by it&#39;s id

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)
