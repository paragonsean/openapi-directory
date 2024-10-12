from typing import List, Dict
from aiohttp import web

from openapi_server.models.subscription_cycle_response import SubscriptionCycleResponse
from openapi_server import util


async def api_rns_pub_cycles_cycle_id_get(request: web.Request, cycle_id, content_type, accept) -> web.Response:
    """Get cycle details

    Retrieve a specific cycle by its ID.

    :param cycle_id: ID from the desired cycle.
    :type cycle_id: str
    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str

    """
    return web.Response(status=200)


async def api_rns_pub_cycles_cycle_id_retry_post(request: web.Request, cycle_id, content_type, accept) -> web.Response:
    """Retry cycle

    Every subscription order has an execution count called cycle, which determines the position of an order counting from when the shopper subscribed. This endpoint reruns a cycle that is currently in error state.

    :param cycle_id: Id from the cycle that will be retried
    :type cycle_id: str
    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str

    """
    return web.Response(status=200)


async def api_rns_pub_cycles_get(request: web.Request, content_type, accept, begin_date=None, end_date=None, subscription_id=None, customer_email=None, status=None, page=None, size=None) -> web.Response:
    """List cycles

    List cycles filtering by some arguments.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param begin_date: Lower limit for the date of creation of the cycle
    :type begin_date: str
    :param end_date: Upper limit for the date of creation of the cycle
    :type end_date: str
    :param subscription_id: Id from the subscription that generated the cycle
    :type subscription_id: str
    :param customer_email: Customer that owns the subscription. Defaults to the current logged user
    :type customer_email: str
    :param status: Current cycle status
    :type status: str
    :param page: Page used for pagination
    :type page: int
    :param size: Page size used for pagination
    :type size: int

    """
    return web.Response(status=200)
