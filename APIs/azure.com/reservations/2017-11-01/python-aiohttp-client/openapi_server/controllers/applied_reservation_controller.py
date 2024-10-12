from typing import List, Dict
from aiohttp import web

from openapi_server.models.applied_reservations import AppliedReservations
from openapi_server.models.error import Error
from openapi_server import util


async def get_applied_reservation_list(request: web.Request, api_version, subscription_id) -> web.Response:
    """Get list of applicable &#x60;Reservation&#x60;s.

    Get applicable &#x60;Reservation&#x60;s that are applied to this subscription.

    :param api_version: Supported version.
    :type api_version: str
    :param subscription_id: Id of the subscription
    :type subscription_id: str

    """
    return web.Response(status=200)
