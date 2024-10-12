from typing import List, Dict
from aiohttp import web

from openapi_server.models.deleted import Deleted
from openapi_server.models.find_all_global_auth_modules200_response_inner import FindAllGlobalAuthModules200ResponseInner
from openapi_server.models.patch_inner import PatchInner
from openapi_server import util


async def create_global_auth_module(request: web.Request, body=None) -> web.Response:
    """Create one global auth. module config

    Create one global auth. module config

    :param body: 
    :type body: dict | bytes

    """
    body = FindAllGlobalAuthModules200ResponseInner.from_dict(body)
    return web.Response(status=200)


async def delete_global_auth_module(request: web.Request, id) -> web.Response:
    """Delete one global auth. module config

    Delete one global auth. module config

    :param id: The auth. config id id
    :type id: str

    """
    return web.Response(status=200)


async def find_all_global_auth_modules(request: web.Request, ) -> web.Response:
    """Get all global auth. module configs

    Get all global auth. module configs


    """
    return web.Response(status=200)


async def find_global_auth_module_by_id(request: web.Request, id) -> web.Response:
    """Get one global auth. module configs

    Get one global auth. module configs

    :param id: The auth. config id
    :type id: str

    """
    return web.Response(status=200)


async def patch_global_auth_module(request: web.Request, id, body=None) -> web.Response:
    """Update one global auth. module config

    Update one global auth. module config

    :param id: The auth. config id
    :type id: str
    :param body: 
    :type body: list | bytes

    """
    body = [PatchInner.from_dict(d) for d in body]
    return web.Response(status=200)


async def update_global_auth_module(request: web.Request, id, body=None) -> web.Response:
    """Update one global auth. module config

    Update one global auth. module config

    :param id: The auth. config id
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = FindAllGlobalAuthModules200ResponseInner.from_dict(body)
    return web.Response(status=200)
