from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.sandbox import Sandbox
from openapi_server.models.sandbox_request import SandboxRequest
from openapi_server import util


async def sandbox_post(request: web.Request, body=None) -> web.Response:
    """Create Sandbox

    Create Sandbox

    :param body: SandboxRequest
    :type body: dict | bytes

    """
    body = SandboxRequest.from_dict(body)
    return web.Response(status=200)


async def sandbox_put(request: web.Request, body=None) -> web.Response:
    """Import Sandbox

    Import Sandbox

    :param body: Sandbox
    :type body: dict | bytes

    """
    body = Sandbox.from_dict(body)
    return web.Response(status=200)


async def sandbox_sandbox_id_delete(request: web.Request, sandbox_id) -> web.Response:
    """Delete Sandbox

    Delete Sandbox

    :param sandbox_id: Sandbox Id
    :type sandbox_id: str

    """
    return web.Response(status=200)


async def sandbox_sandbox_id_get(request: web.Request, sandbox_id) -> web.Response:
    """Export Sandbox

    Export Sandbox

    :param sandbox_id: Sandbox Id
    :type sandbox_id: str

    """
    return web.Response(status=200)
