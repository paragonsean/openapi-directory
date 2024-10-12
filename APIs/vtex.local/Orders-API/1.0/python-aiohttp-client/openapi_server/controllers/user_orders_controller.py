from typing import List, Dict
from aiohttp import web

from openapi_server.models.userorderdetails import Userorderdetails
from openapi_server.models.userorderslist import Userorderslist
from openapi_server import util


async def userorderdetails(request: web.Request, client_email, content_type, accept, order_id) -> web.Response:
    """Retrieve user order details

    Lists all details from a user&#39;s order, through client&#39;s perspective.     &gt; Note that these requests are meant to be made by **Call center operator** profiles. Otherwise, they will return only orders from the same email making the request.

    :param client_email: Customer email.
    :type client_email: str
    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param order_id: Order ID is a unique code that identifies an order.
    :type order_id: str

    """
    return web.Response(status=200)


async def userorderslist(request: web.Request, client_email, page, per_page, content_type, accept) -> web.Response:
    """Retrieve user&#39;s orders

    Lists all orders from a given client, filtering by their email.     &gt; Note that these requests are meant to be made by **Call center operator** profiles. Otherwise, they will return only orders from the same email making the request.

    :param client_email: Customer email.
    :type client_email: str
    :param page: Page number for result pagination.
    :type page: str
    :param per_page: Page quantity for result pagination.
    :type per_page: str
    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str

    """
    return web.Response(status=200)
