from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.service_instance import ServiceInstance
from openapi_server import util


async def create_service_instance(request: web.Request, site_id, addon, config) -> web.Response:
    """create_service_instance

    

    :param site_id: 
    :type site_id: str
    :param addon: 
    :type addon: str
    :param config: 
    :type config: 

    """
    return web.Response(status=200)


async def delete_service_instance(request: web.Request, site_id, addon, instance_id) -> web.Response:
    """delete_service_instance

    

    :param site_id: 
    :type site_id: str
    :param addon: 
    :type addon: str
    :param instance_id: 
    :type instance_id: str

    """
    return web.Response(status=200)


async def list_service_instances_for_site(request: web.Request, site_id) -> web.Response:
    """list_service_instances_for_site

    

    :param site_id: 
    :type site_id: str

    """
    return web.Response(status=200)


async def show_service_instance(request: web.Request, site_id, addon, instance_id) -> web.Response:
    """show_service_instance

    

    :param site_id: 
    :type site_id: str
    :param addon: 
    :type addon: str
    :param instance_id: 
    :type instance_id: str

    """
    return web.Response(status=200)


async def update_service_instance(request: web.Request, site_id, addon, instance_id, config) -> web.Response:
    """update_service_instance

    

    :param site_id: 
    :type site_id: str
    :param addon: 
    :type addon: str
    :param instance_id: 
    :type instance_id: str
    :param config: 
    :type config: 

    """
    return web.Response(status=200)
