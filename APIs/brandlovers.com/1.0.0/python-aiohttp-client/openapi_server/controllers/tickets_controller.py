from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_ticket_messages import GetTicketMessages
from openapi_server.models.get_tickets import GetTickets
from openapi_server.models.new_ticket import NewTicket
from openapi_server.models.new_ticket_message import NewTicketMessage
from openapi_server.models.ticket_status import TicketStatus
from openapi_server import util


async def ticket_post(request: web.Request, authorization, new_ticket) -> web.Response:
    """Creates a new trouble ticket

    Use this service to create a new trouble ticket. Use this to include relevant information about the order, comunicate with the customer or marketplace team. Whenever possible message will be pushed to Mobile first. This is the primary mean of comunicaiton with the customer regarding orders, shippments, shippments status. New tickets will be automatically be set to &#39;OPEN&#39;. Trouble tickets need to be associated with a orderId or customer. New tickets can optionally include a new message.

    :param authorization: Authorization token. The Authorization token can be found in your Admin console.
    :type authorization: str
    :param new_ticket: JSON object with new trouble ticket
    :type new_ticket: dict | bytes

    """
    new_ticket = NewTicket.from_dict(new_ticket)
    return web.Response(status=200)


async def ticket_ticket_id_message_post(request: web.Request, authorization, ticket_id, message) -> web.Response:
    """Add new message to trouble ticket

    Add a new message to this trouble ticket. Messages can be &#x60;CUSTOMER&#x60; (customer will be able to see it) or &#x60;INTERNAL&#x60;.

    :param authorization: Authorization token. The Authorization token can be found in your Admin console.
    :type authorization: str
    :param ticket_id: Trouble ticket ID.
    :type ticket_id: str
    :param message: New message object to append to trouble ticket.
    :type message: dict | bytes

    """
    message = NewTicketMessage.from_dict(message)
    return web.Response(status=200)


async def ticket_ticket_id_messages_get(request: web.Request, authorization, ticket_id, offset=None, limit=None) -> web.Response:
    """Get trouble ticket messages

    Returns trouble ticket history with all messages exchanged. Only tickets related to your seller will be returned. Attempt to read other tickets will return 403 (acess denied).

    :param authorization: Authorization token. The Authorization token can be found in your Admin console.
    :type authorization: str
    :param ticket_id: Trouble ticket ID.
    :type ticket_id: str
    :param offset: Number or items to skip when executing query. List starts at zero. If omitted will default to zero. Use this conjuction with &#x60;limit&#x60; to paginate across the results.
    :type offset: int
    :param limit: Number or items to return when executing query. Defaults to 10. Use this conjuction with &#x60;offset&#x60; to paginate across the results.
    :type limit: int

    """
    return web.Response(status=200)


async def ticket_ticket_id_status_put(request: web.Request, authorization, ticket_id, body) -> web.Response:
    """Update trouble ticket status

    Alows the seller to update the status of a trouble ticket

    :param authorization: Authorization token. The Authorization token can be found in your Admin console.
    :type authorization: str
    :param ticket_id: Trouble ticket unique identification
    :type ticket_id: str
    :param body: New trouble ticket status
    :type body: dict | bytes

    """
    body = TicketStatus.from_dict(body)
    return web.Response(status=200)


async def tickets_get(request: web.Request, authorization, status=None, offset=None, limit=None) -> web.Response:
    """Get customers trouble tickets

    Allows seller to receive and status, queries, requests and complaints from customers. As well related messages

    :param authorization: Authorization token. The Authorization token can be found in your Admin console.
    :type authorization: str
    :param status: Query by trouble ticket status
    :type status: str
    :param offset: Number or items to skip when executing query. List starts at zero. If omitted will default to zero. Use this conjuction with &#x60;limit&#x60; to paginate across the results.
    :type offset: int
    :param limit: Number or items to return when executing query. Defaults to 10. Use this conjuction with &#x60;offset&#x60; to paginate across the results.
    :type limit: int

    """
    return web.Response(status=200)
