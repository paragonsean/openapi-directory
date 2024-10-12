from typing import List, Dict
from aiohttp import web

from openapi_server.models.access_token import AccessToken
from openapi_server.models.error import Error
from openapi_server import util


async def exchange_ticket(request: web.Request, ticket_id) -> web.Response:
    """exchange_ticket

    

    :param ticket_id: 
    :type ticket_id: str

    """
    return web.Response(status=200)
