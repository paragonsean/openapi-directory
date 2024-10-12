from typing import List, Dict
from aiohttp import web

from openapi_server.models.hook import Hook
from openapi_server.models.post_v3_hooks_request import PostV3HooksRequest
from openapi_server import util


async def delete_v3_hooks_id(request: web.Request, id) -> web.Response:
    """Delete a hook

    Delete a hook

    :param id: The ID of the system hook
    :type id: int

    """
    return web.Response(status=200)


async def get_v3_hooks(request: web.Request, ) -> web.Response:
    """Get the list of system hooks

    Get the list of system hooks


    """
    return web.Response(status=200)


async def get_v3_hooks_id(request: web.Request, id) -> web.Response:
    """Test a hook

    Test a hook

    :param id: The ID of the system hook
    :type id: int

    """
    return web.Response(status=200)


async def post_v3_hooks(request: web.Request, body) -> web.Response:
    """Create a new system hook

    Create a new system hook

    :param body: 
    :type body: dict | bytes

    """
    body = PostV3HooksRequest.from_dict(body)
    return web.Response(status=200)
