from typing import List, Dict
from aiohttp import web

from openapi_server.models.global_config import GlobalConfig
from openapi_server.models.patch_inner import PatchInner
from openapi_server import util


async def global_config(request: web.Request, ) -> web.Response:
    """Get the full configuration of Otoroshi

    Get the full configuration of Otoroshi


    """
    return web.Response(status=200)


async def patch_global_config(request: web.Request, body=None) -> web.Response:
    """Update the global configuration with a diff

    Update the global configuration with a diff

    :param body: 
    :type body: list | bytes

    """
    body = [PatchInner.from_dict(d) for d in body]
    return web.Response(status=200)


async def put_global_config(request: web.Request, body=None) -> web.Response:
    """Update the global configuration

    Update the global configuration

    :param body: 
    :type body: dict | bytes

    """
    body = GlobalConfig.from_dict(body)
    return web.Response(status=200)
