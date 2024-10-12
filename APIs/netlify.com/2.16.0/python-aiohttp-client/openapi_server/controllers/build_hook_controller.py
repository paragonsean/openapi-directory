from typing import List, Dict
from aiohttp import web

from openapi_server.models.build_hook import BuildHook
from openapi_server.models.build_hook_setup import BuildHookSetup
from openapi_server.models.error import Error
from openapi_server import util


async def create_site_build_hook(request: web.Request, site_id, build_hook) -> web.Response:
    """create_site_build_hook

    

    :param site_id: 
    :type site_id: str
    :param build_hook: 
    :type build_hook: dict | bytes

    """
    build_hook = BuildHookSetup.from_dict(build_hook)
    return web.Response(status=200)


async def delete_site_build_hook(request: web.Request, site_id, id) -> web.Response:
    """delete_site_build_hook

    

    :param site_id: 
    :type site_id: str
    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def get_site_build_hook(request: web.Request, site_id, id) -> web.Response:
    """get_site_build_hook

    

    :param site_id: 
    :type site_id: str
    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def list_site_build_hooks(request: web.Request, site_id) -> web.Response:
    """list_site_build_hooks

    

    :param site_id: 
    :type site_id: str

    """
    return web.Response(status=200)


async def update_site_build_hook(request: web.Request, site_id, id, build_hook) -> web.Response:
    """update_site_build_hook

    

    :param site_id: 
    :type site_id: str
    :param id: 
    :type id: str
    :param build_hook: 
    :type build_hook: dict | bytes

    """
    build_hook = BuildHookSetup.from_dict(build_hook)
    return web.Response(status=200)
