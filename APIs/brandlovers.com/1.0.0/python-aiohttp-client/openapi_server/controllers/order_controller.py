from typing import List, Dict
from aiohttp import web

from openapi_server.models.new_tracking_refund import NewTrackingRefund
from openapi_server.models.newshipmentstatus import Newshipmentstatus
from openapi_server.models.order import Order
from openapi_server import util


async def order_order_id_get(request: web.Request, authorization, order_id) -> web.Response:
    """Returns all details of a order

    Returns all details of a single order, including last status, items shipped or not.

    :param authorization: Authorization token. The Authorization token can be found in your Admin console.
    :type authorization: str
    :param order_id: Unique Id of this order.
    :type order_id: str

    """
    return web.Response(status=200)


async def order_order_id_shipment_cancel_post(request: web.Request, authorization, order_id, body) -> web.Response:
    """Confirm shipment canceletion (when requested by the customer) or failure to deliver

    Confirm shipment canceletion (when requested by the customer) or failure to deliver one shipment

    :param authorization: Authorization token. The Authorization token can be found in your Admin console.
    :type authorization: str
    :param order_id: Unique Order Id
    :type order_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = NewTrackingRefund.from_dict(body)
    return web.Response(status=200)


async def order_order_id_shipment_delivered_post(request: web.Request, authorization, order_id, body) -> web.Response:
    """Confirms that a shipment was delivered

    Confirms that a shipment was delivered. Must inform quantity of successfully deliverd items even if items deliverd was less than the original order

    :param authorization: Authorization token. The Authorization token can be found in your Admin console.
    :type authorization: str
    :param order_id: Unique Order Id
    :type order_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = Newshipmentstatus.from_dict(body)
    return web.Response(status=200)


async def order_order_id_shipment_exchange_post(request: web.Request, authorization, order_id, body) -> web.Response:
    """Confirm item exchange

    This enpoint to confirm item exchange when failure to deliver or requested by the customer. All customer requests are tracket via trouble tickets

    :param authorization: Authorization token. The Authorization token can be found in your Admin console.
    :type authorization: str
    :param order_id: Unique Order Id
    :type order_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = NewTrackingRefund.from_dict(body)
    return web.Response(status=200)


async def order_order_id_shipment_return_post(request: web.Request, authorization, order_id, body) -> web.Response:
    """Confirm order item return and refund

    Use this endpoint to return and refund items froma a order. In order to fully return an order list all items and applicate quantity.

    :param authorization: Authorization token. The Authorization token can be found in your Admin console.
    :type authorization: str
    :param order_id: Order unique Id
    :type order_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = NewTrackingRefund.from_dict(body)
    return web.Response(status=200)


async def order_order_id_shipment_sent_post(request: web.Request, authorization, order_id, body) -> web.Response:
    """Update new order to include shipment information

    Updates order to include shipment shiped information. This endpoint can be used to include a single or multiple shipments for any give order. In order to inform that all items of a order where shipped list all of them, including applicable quantities in the payload.

    :param authorization: Authorization token. The Authorization token can be found in your Admin console.
    :type authorization: str
    :param order_id: Unique Order Id
    :type order_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = Newshipmentstatus.from_dict(body)
    return web.Response(status=200)
