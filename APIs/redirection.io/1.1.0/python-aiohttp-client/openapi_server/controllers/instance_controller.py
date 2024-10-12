from typing import List, Dict
from aiohttp import web

from openapi_server.models.instance_read import InstanceRead
from openapi_server.models.instance_write import InstanceWrite
from openapi_server import util


async def get_instance_collection(request: web.Request, project_id) -> web.Response:
    """Retrieves the collection of Instance resources.

    

    :param project_id: 
    :type project_id: str

    """
    return web.Response(status=200)


async def get_instance_item(request: web.Request, id) -> web.Response:
    """Retrieves a Instance resource.

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def live_instance_item(request: web.Request, id, instance=None) -> web.Response:
    """Replaces the Instance resource.

    

    :param id: 
    :type id: str
    :param instance: The updated Instance resource
    :type instance: dict | bytes

    """
    instance = InstanceWrite.from_dict(instance)
    return web.Response(status=200)


async def logging_instance_item(request: web.Request, id, instance=None) -> web.Response:
    """Replaces the Instance resource.

    

    :param id: 
    :type id: str
    :param instance: The updated Instance resource
    :type instance: dict | bytes

    """
    instance = InstanceWrite.from_dict(instance)
    return web.Response(status=200)


async def post_instance_collection(request: web.Request, instance=None) -> web.Response:
    """Creates a Instance resource.

    

    :param instance: The new Instance resource
    :type instance: dict | bytes

    """
    instance = InstanceWrite.from_dict(instance)
    return web.Response(status=200)


async def put_instance_item(request: web.Request, id, instance=None) -> web.Response:
    """Replaces the Instance resource.

    

    :param id: 
    :type id: str
    :param instance: The updated Instance resource
    :type instance: dict | bytes

    """
    instance = InstanceWrite.from_dict(instance)
    return web.Response(status=200)
