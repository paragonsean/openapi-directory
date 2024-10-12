from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.hook import Hook
from openapi_server import util


async def create_hook_by_site_id(request: web.Request, site_id, hook) -> web.Response:
    """create_hook_by_site_id

    

    :param site_id: 
    :type site_id: str
    :param hook: 
    :type hook: dict | bytes

    """
    hook = Hook.from_dict(hook)
    return web.Response(status=200)


async def delete_hook(request: web.Request, hook_id) -> web.Response:
    """delete_hook

    

    :param hook_id: 
    :type hook_id: str

    """
    return web.Response(status=200)


async def enable_hook(request: web.Request, hook_id) -> web.Response:
    """enable_hook

    

    :param hook_id: 
    :type hook_id: str

    """
    return web.Response(status=200)


async def get_hook(request: web.Request, hook_id) -> web.Response:
    """get_hook

    

    :param hook_id: 
    :type hook_id: str

    """
    return web.Response(status=200)


async def list_hooks_by_site_id(request: web.Request, site_id) -> web.Response:
    """list_hooks_by_site_id

    

    :param site_id: 
    :type site_id: str

    """
    return web.Response(status=200)


async def update_hook(request: web.Request, hook_id, hook) -> web.Response:
    """update_hook

    

    :param hook_id: 
    :type hook_id: str
    :param hook: 
    :type hook: dict | bytes

    """
    hook = Hook.from_dict(hook)
    return web.Response(status=200)
