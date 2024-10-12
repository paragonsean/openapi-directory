from typing import List, Dict
from aiohttp import web

from openapi_server.models.authority import Authority
from openapi_server.models.credential import Credential
from openapi_server import util


async def credentials_get(request: web.Request, ) -> web.Response:
    """List the credentials associated with the authenticated user.

    


    """
    return web.Response(status=200)


async def scopes_get(request: web.Request, ) -> web.Response:
    """Scopes

    List available token scopes


    """
    return web.Response(status=200)


async def verify_post(request: web.Request, ) -> web.Response:
    """Verify token and return details of the owning user

    


    """
    return web.Response(status=200)
