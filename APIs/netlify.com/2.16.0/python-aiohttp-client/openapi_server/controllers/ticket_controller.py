from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.ticket import Ticket
from openapi_server import util


async def create_ticket(request: web.Request, client_id) -> web.Response:
    """create_ticket

    

    :param client_id: 
    :type client_id: str

    """
    return web.Response(status=200)


async def show_ticket(request: web.Request, ticket_id) -> web.Response:
    """show_ticket

    

    :param ticket_id: 
    :type ticket_id: str

    """
    return web.Response(status=200)
