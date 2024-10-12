from typing import List, Dict
from aiohttp import web

from openapi_server.models.deleted import Deleted
from openapi_server.models.patch_inner import PatchInner
from openapi_server.models.script import Script
from openapi_server.models.script_compilation_result import ScriptCompilationResult
from openapi_server import util


async def compile_script(request: web.Request, body=None) -> web.Response:
    """Compile a script

    Compile a script

    :param body: 
    :type body: dict | bytes

    """
    body = Script.from_dict(body)
    return web.Response(status=200)


async def create_script(request: web.Request, body=None) -> web.Response:
    """Create a new script

    Create a new script

    :param body: 
    :type body: dict | bytes

    """
    body = Script.from_dict(body)
    return web.Response(status=200)


async def delete_script(request: web.Request, script_id) -> web.Response:
    """Delete a script

    Delete a script

    :param script_id: The script id
    :type script_id: str

    """
    return web.Response(status=200)


async def find_all_scripts(request: web.Request, ) -> web.Response:
    """Get all scripts

    Get all scripts


    """
    return web.Response(status=200)


async def find_script_by_id(request: web.Request, script_id) -> web.Response:
    """Get a script

    Get a script

    :param script_id: The script id
    :type script_id: str

    """
    return web.Response(status=200)


async def patch_script(request: web.Request, script_id, body=None) -> web.Response:
    """Update a script with a diff

    Update a script with a diff

    :param script_id: The script id
    :type script_id: str
    :param body: 
    :type body: list | bytes

    """
    body = [PatchInner.from_dict(d) for d in body]
    return web.Response(status=200)


async def update_script(request: web.Request, script_id, body=None) -> web.Response:
    """Update a script

    Update a script

    :param script_id: The script id
    :type script_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = Script.from_dict(body)
    return web.Response(status=200)
