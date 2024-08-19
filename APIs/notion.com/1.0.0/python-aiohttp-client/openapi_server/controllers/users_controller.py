from typing import List, Dict
from aiohttp import web

from openapi_server.models.retrieve_a_user200_response import RetrieveAUser200Response
from openapi_server import util


async def retrieve_a_user(request: web.Request, id, notion_version=None) -> web.Response:
    """Retrieve a user

    Retrieve a user object using the ID specified in the request path.

    :param id: 
    :type id: str
    :param notion_version: 
    :type notion_version: str

    """
    return web.Response(status=200)
