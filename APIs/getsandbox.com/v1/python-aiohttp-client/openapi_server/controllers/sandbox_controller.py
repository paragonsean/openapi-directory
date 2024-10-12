from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_sandbox import CreateSandbox
from openapi_server.models.sandbox import Sandbox
from openapi_server import util


async def create_sandbox(request: web.Request, body) -> web.Response:
    """createSandbox

    

    :param body: Sandbox to be created
    :type body: dict | bytes

    """
    body = CreateSandbox.from_dict(body)
    return web.Response(status=200)


async def delete_sandbox(request: web.Request, sandbox_name) -> web.Response:
    """deleteSandbox

    

    :param sandbox_name: Name of the Sandbox
    :type sandbox_name: str

    """
    return web.Response(status=200)


async def delete_sandbox_state(request: web.Request, sandbox_name) -> web.Response:
    """deleteSandboxState

    

    :param sandbox_name: Name of the Sandbox
    :type sandbox_name: str

    """
    return web.Response(status=200)


async def fork_sandbox(request: web.Request, sandbox_name) -> web.Response:
    """forkSandbox

    

    :param sandbox_name: Name of the Sandbox
    :type sandbox_name: str

    """
    return web.Response(status=200)


async def get_sandbox(request: web.Request, sandbox_name) -> web.Response:
    """getSandbox

    

    :param sandbox_name: Name of the Sandbox
    :type sandbox_name: str

    """
    return web.Response(status=200)


async def get_sandbox_state(request: web.Request, sandbox_name) -> web.Response:
    """getSandboxState

    

    :param sandbox_name: Name of the Sandbox
    :type sandbox_name: str

    """
    return web.Response(status=200)


async def get_sandboxes(request: web.Request, filter_type=None) -> web.Response:
    """getSandboxes

    

    :param filter_type: 
    :type filter_type: str

    """
    return web.Response(status=200)


async def update_sandbox(request: web.Request, sandbox_name, body) -> web.Response:
    """updateSandbox

    

    :param sandbox_name: Name of the Sandbox
    :type sandbox_name: str
    :param body: Fields to updated on given Sandbox
    :type body: dict | bytes

    """
    body = Sandbox.from_dict(body)
    return web.Response(status=200)
