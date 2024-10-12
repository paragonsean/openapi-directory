from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.integrations_token import IntegrationsToken
from openapi_server import util


async def get_integrations_token(request: web.Request, ) -> web.Response:
    """Generate a new access token for MotaWord&#39;s integrations service

    Generate a new access token for MotaWord&#39;s integrations service


    """
    return web.Response(status=200)
