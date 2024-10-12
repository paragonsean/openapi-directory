from typing import List, Dict
from aiohttp import web

from openapi_server.models.default_payload import DefaultPayload
from openapi_server.models.get_user_projects200_response import GetUserProjects200Response
from openapi_server import util


async def get_user_projects(request: web.Request, username, page=None, size=None) -> web.Response:
    """List all active projects for the user

    List all active projects for the user

    :param username: User&#39;s identifier
    :type username: str
    :param page: Page Number
    :type page: int
    :param size: Page Size
    :type size: int

    """
    return web.Response(status=200)
