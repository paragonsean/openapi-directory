from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_conversation import GetConversation
from openapi_server import util


async def get_conversation(request: web.Request, accept, content_type, order_id, reason=None) -> web.Response:
    """Retrieve order conversation

    List all order conversations of an order by its order ID.

    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param content_type: Type of the content being sent.
    :type content_type: str
    :param order_id: Order ID is a unique code that identifies an order.
    :type order_id: str
    :param reason: Reason for requesting unmasked data. Relevant only for PII platform version.
    :type reason: str

    """
    return web.Response(status=200)
