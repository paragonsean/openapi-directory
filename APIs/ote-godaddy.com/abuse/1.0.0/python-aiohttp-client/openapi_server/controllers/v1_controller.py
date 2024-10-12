from typing import List, Dict
from aiohttp import web

from openapi_server.models.abuse_ticket import AbuseTicket
from openapi_server.models.abuse_ticket_create import AbuseTicketCreate
from openapi_server.models.abuse_ticket_id import AbuseTicketId
from openapi_server.models.abuse_ticket_list import AbuseTicketList
from openapi_server.models.error import Error
from openapi_server import util


async def create_ticket(request: web.Request, body) -> web.Response:
    """Create a new abuse ticket

    

    :param body: The endpoint which allows the Reporter to create a new abuse ticket
    :type body: dict | bytes

    """
    body = AbuseTicketCreate.from_dict(body)
    return web.Response(status=200)


async def get_ticket_info(request: web.Request, ticket_id) -> web.Response:
    """Return the abuse ticket data for a given ticket id

    

    :param ticket_id: A unique abuse ticket identifier
    :type ticket_id: str

    """
    return web.Response(status=200)


async def get_tickets(request: web.Request, type=None, closed=None, source_domain_or_ip=None, target=None, created_start=None, created_end=None, limit=None, offset=None) -> web.Response:
    """List all abuse tickets ids that match user provided filters

    

    :param type: The type of abuse.
    :type type: str
    :param closed: Is this abuse ticket closed?
    :type closed: bool
    :param source_domain_or_ip: The domain name or ip address the abuse originated from
    :type source_domain_or_ip: str
    :param target: The brand/company the abuse is targeting. ie: brand name/bank name
    :type target: str
    :param created_start: The earliest abuse ticket creation date to pull abuse tickets for
    :type created_start: str
    :param created_end: The latest abuse ticket creation date to pull abuse tickets for
    :type created_end: str
    :param limit: Number of abuse ticket numbers to return.
    :type limit: int
    :param offset: The earliest result set record number to pull abuse tickets for
    :type offset: int

    """
    return web.Response(status=200)
