from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_error import ApiError
from openapi_server.models.who_is_response import WhoIsResponse
from openapi_server import util


async def resolve_who_is_entry_0(request: web.Request, id4n) -> web.Response:
    """Resolve owner of id4n

    

    :param id4n: id4n
    :type id4n: str

    """
    return web.Response(status=200)
