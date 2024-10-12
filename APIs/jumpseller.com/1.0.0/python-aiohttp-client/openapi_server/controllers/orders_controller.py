from typing import List, Dict
from aiohttp import web

from openapi_server.models.count import Count
from openapi_server.models.not_found import NotFound
from openapi_server.models.order import Order
from openapi_server.models.order_create import OrderCreate
from openapi_server.models.order_edit import OrderEdit
from openapi_server.models.order_history import OrderHistory
from openapi_server.models.order_history_edit import OrderHistoryEdit
from openapi_server.models.status_invalid import StatusInvalid
from openapi_server import util


async def orders_after_id_json_get(request: web.Request, login, authtoken, id) -> web.Response:
    """Retrieve orders filtered by Order Id.

    For example the GET /orders/after/5000 will return Order 5001, 5002, 5003, etc.

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param id: Id of the Order
    :type id: int

    """
    return web.Response(status=200)


async def orders_count_json_get(request: web.Request, login, authtoken) -> web.Response:
    """Count all Orders.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str

    """
    return web.Response(status=200)


async def orders_id_history_json_get(request: web.Request, login, authtoken, id) -> web.Response:
    """Retrieve all Order History.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param id: Id of the Order
    :type id: int

    """
    return web.Response(status=200)


async def orders_id_history_json_post(request: web.Request, login, authtoken, id, body) -> web.Response:
    """Create a new Order History Entry.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param id: Id of the OrderHistory
    :type id: int
    :param body: Order History parameters.
    :type body: dict | bytes

    """
    body = OrderHistoryEdit.from_dict(body)
    return web.Response(status=200)


async def orders_id_json_get(request: web.Request, login, authtoken, id) -> web.Response:
    """Retrieve a single Order.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param id: Id of the Order
    :type id: int

    """
    return web.Response(status=200)


async def orders_id_json_put(request: web.Request, login, authtoken, id, body) -> web.Response:
    """Modify an existing Order.

    Only &#x60;status&#x60;, &#x60;shipment_status&#x60;, &#x60;tracking_number&#x60;, &#x60;tracking_company&#x60;, &#x60;tracking_url&#x60;, &#x60;additional_information&#x60; and &#x60;additional_fields&#x60; are available for update. An email is send if &#x60;shipment_status&#x60; changes.

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param id: Id of the Order
    :type id: int
    :param body: Order parameters to change
    :type body: dict | bytes

    """
    body = OrderEdit.from_dict(body)
    return web.Response(status=200)


async def orders_json_get(request: web.Request, login, authtoken, limit=None, page=None) -> web.Response:
    """Retrieve all Orders.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param limit: List restriction
    :type limit: int
    :param page: List page
    :type page: int

    """
    return web.Response(status=200)


async def orders_json_post(request: web.Request, login, authtoken, body) -> web.Response:
    """Create a new Order.

    Orders created externally keep the given order product&#39;s values (bypassing internal promotion or product amounts).

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param body: Order parameters.
    :type body: dict | bytes

    """
    body = OrderCreate.from_dict(body)
    return web.Response(status=200)


async def orders_status_status_json_get(request: web.Request, login, authtoken, status) -> web.Response:
    """Retrieve orders filtered by status.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param status: Status of the Order used as filter
    :type status: str

    """
    return web.Response(status=200)
