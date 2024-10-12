from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def tickets_department_add_post(request: web.Request, department, subject, contents) -> web.Response:
    """Open ticket with desired department

    Available departments are support, billing, sales

    :param department: Department you want to open a ticket with
    :type department: str
    :param subject: Subject of the ticket you are opening
    :type subject: str
    :param contents: Message reply being sent
    :type contents: str

    """
    return web.Response(status=200)


async def tickets_get(request: web.Request, ) -> web.Response:
    """View all your tickets

    Shows all your tickets


    """
    return web.Response(status=200)


async def tickets_ticket_id_get(request: web.Request, ticket_id) -> web.Response:
    """View details on a specific ticket

    Shows all information of a specific ticketId

    :param ticket_id: TicketId you want to see
    :type ticket_id: 

    """
    return web.Response(status=200)


async def tickets_ticketid_update_post(request: web.Request, ticketid, contents) -> web.Response:
    """Post a reply to a ticket

    

    :param ticketid: TicketId of the ticket you want to post an update to
    :type ticketid: 
    :param contents: Message reply being sent
    :type contents: str

    """
    return web.Response(status=200)
