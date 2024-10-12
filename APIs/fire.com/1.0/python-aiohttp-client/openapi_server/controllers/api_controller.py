from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_application import ApiApplication
from openapi_server.models.new_api_application import NewApiApplication
from openapi_server import util


async def create_api_application(request: web.Request, body) -> web.Response:
    """Create a new API Application

    Create a new API Application with specified permissions

    :param body: Details of the new API Application
    :type body: dict | bytes

    """
    body = NewApiApplication.from_dict(body)
    return web.Response(status=200)
