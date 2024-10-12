from typing import List, Dict
from aiohttp import web

from openapi_server.models.admin_settings_post_request import AdminSettingsPostRequest
from openapi_server import util


async def admin_reset_post(request: web.Request, ) -> web.Response:
    """Reset mappings and request journal

    Reset mappings to the default state and reset the request journal


    """
    return web.Response(status=200)


async def admin_settings_post(request: web.Request, body) -> web.Response:
    """Update global settings

    

    :param body: 
    :type body: dict | bytes

    """
    body = AdminSettingsPostRequest.from_dict(body)
    return web.Response(status=200)


async def admin_shutdown_post(request: web.Request, ) -> web.Response:
    """admin_shutdown_post

    Shutdown the WireMock server


    """
    return web.Response(status=200)
