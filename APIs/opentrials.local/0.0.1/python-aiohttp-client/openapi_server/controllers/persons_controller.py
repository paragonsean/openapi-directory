from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.person import Person
from openapi_server import util


async def get_person(request: web.Request, id) -> web.Response:
    """get_person

    Returns person details

    :param id: ID of the person
    :type id: str

    """
    return web.Response(status=200)
