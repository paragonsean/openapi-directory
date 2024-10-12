from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.patch import Patch
from openapi_server.models.reservation_list import ReservationList
from openapi_server.models.reservation_order_list import ReservationOrderList
from openapi_server.models.reservation_order_response import ReservationOrderResponse
from openapi_server.models.reservation_response import ReservationResponse
from openapi_server import util


async def reservation_get(request: web.Request, reservation_id, reservation_order_id, api_version, expand=None) -> web.Response:
    """Get &#x60;Reservation&#x60; details.

    Get specific &#x60;Reservation&#x60; details.

    :param reservation_id: Id of the Reservation Item
    :type reservation_id: str
    :param reservation_order_id: Order Id of the reservation
    :type reservation_order_id: str
    :param api_version: Supported version for this document is 2019-04-01
    :type api_version: str
    :param expand: Supported value of this query is renewProperties
    :type expand: str

    """
    return web.Response(status=200)


async def reservation_list(request: web.Request, reservation_order_id, api_version) -> web.Response:
    """Get &#x60;Reservation&#x60;s in a given reservation Order

    List &#x60;Reservation&#x60;s within a single &#x60;ReservationOrder&#x60;.

    :param reservation_order_id: Order Id of the reservation
    :type reservation_order_id: str
    :param api_version: Supported version for this document is 2019-04-01
    :type api_version: str

    """
    return web.Response(status=200)


async def reservation_list_revisions(request: web.Request, reservation_id, reservation_order_id, api_version) -> web.Response:
    """Get &#x60;Reservation&#x60; revisions.

    List of all the revisions for the &#x60;Reservation&#x60;.

    :param reservation_id: Id of the Reservation Item
    :type reservation_id: str
    :param reservation_order_id: Order Id of the reservation
    :type reservation_order_id: str
    :param api_version: Supported version for this document is 2019-04-01
    :type api_version: str

    """
    return web.Response(status=200)


async def reservation_order_get(request: web.Request, reservation_order_id, api_version, expand=None) -> web.Response:
    """Get a specific &#x60;ReservationOrder&#x60;.

    Get the details of the &#x60;ReservationOrder&#x60;.

    :param reservation_order_id: Order Id of the reservation
    :type reservation_order_id: str
    :param api_version: Supported version for this document is 2019-04-01
    :type api_version: str
    :param expand: May be used to expand the planInformation.
    :type expand: str

    """
    return web.Response(status=200)


async def reservation_order_list(request: web.Request, api_version) -> web.Response:
    """Get all &#x60;ReservationOrder&#x60;s.

    List of all the &#x60;ReservationOrder&#x60;s that the user has access to in the current tenant.

    :param api_version: Supported version for this document is 2019-04-01
    :type api_version: str

    """
    return web.Response(status=200)


async def reservation_update(request: web.Request, reservation_order_id, reservation_id, api_version, parameters) -> web.Response:
    """Updates a &#x60;Reservation&#x60;.

    Updates the applied scopes of the &#x60;Reservation&#x60;.

    :param reservation_order_id: Order Id of the reservation
    :type reservation_order_id: str
    :param reservation_id: Id of the Reservation Item
    :type reservation_id: str
    :param api_version: Supported version for this document is 2019-04-01
    :type api_version: str
    :param parameters: Information needed to patch a reservation item
    :type parameters: dict | bytes

    """
    parameters = Patch.from_dict(parameters)
    return web.Response(status=200)
