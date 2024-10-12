from typing import List, Dict
from aiohttp import web

from openapi_server.models.instance import Instance
from openapi_server.models.instance_error import InstanceError
from openapi_server.models.instance_list import InstanceList
from openapi_server import util


async def get_instance_info(request: web.Request, id) -> web.Response:
    """Get information about an instance

    Get information about an instance.

    :param id: instance ID
    :type id: int

    """
    return web.Response(status=200)


async def get_instances_info(request: web.Request, ) -> web.Response:
    """Get all instances

    Get all instances.


    """
    return web.Response(status=200)
