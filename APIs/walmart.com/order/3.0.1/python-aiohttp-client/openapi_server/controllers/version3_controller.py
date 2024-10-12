from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def acknowledge_orders(request: web.Request, purchase_order_id, content_type, accept, wm_consumer_channel_type, wm_consumer_id, wm_sec_timestamp, wm_sec_auth_signature, wm_svc_name, wm_qos_correlation_id, ship_node=None) -> web.Response:
    """Acknowledge orders

    You can acknowledge an entire order, including all of its order lines. Walmart business rules require to acknowledge orders within four hour of receipt of the order, except in extenuating circumstances.

    :param purchase_order_id: Purchase Order ID
    :type purchase_order_id: str
    :param content_type: application/xml, application/json
    :type content_type: str
    :param accept: application/xml, application/json
    :type accept: str
    :param wm_consumer_channel_type: Channel Type
    :type wm_consumer_channel_type: str
    :param wm_consumer_id: Your Consumer ID
    :type wm_consumer_id: str
    :param wm_sec_timestamp: Epoch timestamp
    :type wm_sec_timestamp: str
    :param wm_sec_auth_signature: Authentication signature
    :type wm_sec_auth_signature: str
    :param wm_svc_name: The Service name
    :type wm_svc_name: str
    :param wm_qos_correlation_id: A Transaction ID
    :type wm_qos_correlation_id: str
    :param ship_node: Ship Node
    :type ship_node: str

    """
    return web.Response(status=200)


async def cancel_order(request: web.Request, purchase_order_id, content_type, accept, wm_consumer_channel_type, wm_consumer_id, wm_sec_timestamp, wm_sec_auth_signature, wm_svc_name, wm_qos_correlation_id, request_body, ship_node=None) -> web.Response:
    """Cancel order lines

    You can cancel one or more order lines. You must include a purchaseOrderLineNumber when cancelling an order. After cancelling your order, update the inventory for the cancelled order and send it in the next inventory feed.

    :param purchase_order_id: Purchase Order ID
    :type purchase_order_id: str
    :param content_type: application/xml, application/json
    :type content_type: str
    :param accept: application/xml, application/json
    :type accept: str
    :param wm_consumer_channel_type: Channel Type
    :type wm_consumer_channel_type: str
    :param wm_consumer_id: Your Consumer ID
    :type wm_consumer_id: str
    :param wm_sec_timestamp: Epoch timestamp
    :type wm_sec_timestamp: str
    :param wm_sec_auth_signature: Authentication signature
    :type wm_sec_auth_signature: str
    :param wm_svc_name: The Service name
    :type wm_svc_name: str
    :param wm_qos_correlation_id: A Transaction ID
    :type wm_qos_correlation_id: str
    :param request_body: Request body
    :type request_body: str
    :param ship_node: Ship Node
    :type ship_node: str

    """
    return web.Response(status=200)


async def get_all_orders(request: web.Request, content_type, accept, wm_consumer_channel_type, wm_consumer_id, wm_sec_timestamp, wm_sec_auth_signature, wm_svc_name, wm_qos_correlation_id, ship_node=None, sku=None, customer_order_id=None, purchase_order_id=None, status=None, created_start_date=None, created_end_date=None, from_expected_ship_date=None, to_expected_ship_date=None, limit=None) -> web.Response:
    """Get all orders

    You can display a list of all orders with the query parameter filter criteria.

    :param content_type: application/xml, application/json
    :type content_type: str
    :param accept: application/xml, application/json
    :type accept: str
    :param wm_consumer_channel_type: Channel Type
    :type wm_consumer_channel_type: str
    :param wm_consumer_id: Your Consumer ID
    :type wm_consumer_id: str
    :param wm_sec_timestamp: Epoch timestamp
    :type wm_sec_timestamp: str
    :param wm_sec_auth_signature: Authentication signature
    :type wm_sec_auth_signature: str
    :param wm_svc_name: The Service name
    :type wm_svc_name: str
    :param wm_qos_correlation_id: A Transaction ID
    :type wm_qos_correlation_id: str
    :param ship_node: Ship Node
    :type ship_node: str
    :param sku: Retrieves all orders with the specified SKU.
    :type sku: str
    :param customer_order_id: Retrives the details of the specified customerOrderId.
    :type customer_order_id: str
    :param purchase_order_id: The purchase order ID associated with the order to retrieve. One customer order can have multiple purchase orders associated with it.
    :type purchase_order_id: str
    :param status: The list of orders corresponding to the requested status.
    :type status: str
    :param created_start_date: Limit orders to those created after this date or a timestamp.
    :type created_start_date: str
    :param created_end_date: Limit orders to those created before this date or timestamp.
    :type created_end_date: str
    :param from_expected_ship_date: Limit orders to those that have order lines with an expected ship date after this date.
    :type from_expected_ship_date: str
    :param to_expected_ship_date: Limit orders to those that have order lines with an expected ship date before this date. 
    :type to_expected_ship_date: str
    :param limit: The number of orders to be returned. Do not set this parameter to over 200 orders.
    :type limit: int

    """
    return web.Response(status=200)


async def get_all_orders_next(request: web.Request, next_cursor, content_type, accept, wm_consumer_channel_type, wm_consumer_id, wm_sec_timestamp, wm_sec_auth_signature, wm_svc_name, wm_qos_correlation_id) -> web.Response:
    """Get orders for next page

    You can display a list of all orders with nextCursor path parameter pagination criteria.

    :param next_cursor: Used for pagination when there are more than 200 orders to retrieve. The nextCursor value of the returned response includes a link to another GET call to retrieve the next page. Copy the link and paste it in the next call.
    :type next_cursor: str
    :param content_type: application/xml, application/json
    :type content_type: str
    :param accept: application/xml, application/json
    :type accept: str
    :param wm_consumer_channel_type: Channel Type
    :type wm_consumer_channel_type: str
    :param wm_consumer_id: Your Consumer ID
    :type wm_consumer_id: str
    :param wm_sec_timestamp: Epoch timestamp
    :type wm_sec_timestamp: str
    :param wm_sec_auth_signature: Authentication signature
    :type wm_sec_auth_signature: str
    :param wm_svc_name: The Service name
    :type wm_svc_name: str
    :param wm_qos_correlation_id: A Transaction ID
    :type wm_qos_correlation_id: str

    """
    return web.Response(status=200)


async def get_next_cursor_released_orders(request: web.Request, next_cursor, content_type, accept, wm_consumer_channel_type, wm_consumer_id, wm_sec_timestamp, wm_sec_auth_signature, wm_svc_name, wm_qos_correlation_id) -> web.Response:
    """Get released orders for next page

    You can display all released orders that have been created and are ready for fulfilment with nextCursor path parameter.

    :param next_cursor: Used for pagination when there are more than 200 orders to retrieve. The nextCursor value of the returned response includes a link to another GET call to retrieve the next page. Copy the link and paste it in the next call.
    :type next_cursor: str
    :param content_type: application/xml, application/json
    :type content_type: str
    :param accept: application/xml, application/json
    :type accept: str
    :param wm_consumer_channel_type: Channel Type
    :type wm_consumer_channel_type: str
    :param wm_consumer_id: Your Consumer ID
    :type wm_consumer_id: str
    :param wm_sec_timestamp: Epoch timestamp
    :type wm_sec_timestamp: str
    :param wm_sec_auth_signature: Authentication signature
    :type wm_sec_auth_signature: str
    :param wm_svc_name: The Service name
    :type wm_svc_name: str
    :param wm_qos_correlation_id: A Transaction ID
    :type wm_qos_correlation_id: str

    """
    return web.Response(status=200)


async def get_order_by_purchase_order_id(request: web.Request, purchase_order_id, content_type, accept, wm_consumer_channel_type, wm_consumer_id, wm_sec_timestamp, wm_sec_auth_signature, wm_svc_name, wm_qos_correlation_id, ship_node=None) -> web.Response:
    """Get an order

    You can display details of a specific order based on the purchaseOrderId.

    :param purchase_order_id: Purchase Order ID
    :type purchase_order_id: str
    :param content_type: application/xml, application/json
    :type content_type: str
    :param accept: application/xml, application/json
    :type accept: str
    :param wm_consumer_channel_type: Channel Type
    :type wm_consumer_channel_type: str
    :param wm_consumer_id: Your Consumer ID
    :type wm_consumer_id: str
    :param wm_sec_timestamp: Epoch timestamp
    :type wm_sec_timestamp: str
    :param wm_sec_auth_signature: Authentication signature
    :type wm_sec_auth_signature: str
    :param wm_svc_name: The Service name
    :type wm_svc_name: str
    :param wm_qos_correlation_id: A Transaction ID
    :type wm_qos_correlation_id: str
    :param ship_node: Ship Node
    :type ship_node: str

    """
    return web.Response(status=200)


async def get_released_orders(request: web.Request, created_start_date, content_type, accept, wm_consumer_channel_type, wm_consumer_id, wm_sec_timestamp, wm_sec_auth_signature, wm_svc_name, wm_qos_correlation_id, ship_node=None, limit=None) -> web.Response:
    """Get all released orders

    You can display all released orders that have been created and are ready for fulfilment.

    :param created_start_date: Limit orders to those created after this date or a timestamp.
    :type created_start_date: str
    :param content_type: application/xml, application/json
    :type content_type: str
    :param accept: application/xml, application/json
    :type accept: str
    :param wm_consumer_channel_type: Channel Type
    :type wm_consumer_channel_type: str
    :param wm_consumer_id: Your Consumer ID
    :type wm_consumer_id: str
    :param wm_sec_timestamp: Epoch timestamp
    :type wm_sec_timestamp: str
    :param wm_sec_auth_signature: Authentication signature
    :type wm_sec_auth_signature: str
    :param wm_svc_name: The Service name
    :type wm_svc_name: str
    :param wm_qos_correlation_id: A Transaction ID
    :type wm_qos_correlation_id: str
    :param ship_node: Ship Node
    :type ship_node: str
    :param limit: The number of orders to be returned. Do not set this parameter to over 200 orders.
    :type limit: int

    """
    return web.Response(status=200)


async def refund_order(request: web.Request, purchase_order_id, content_type, accept, wm_consumer_channel_type, wm_consumer_id, wm_sec_timestamp, wm_sec_auth_signature, wm_svc_name, wm_qos_correlation_id, request_body, ship_node=None) -> web.Response:
    """Refund order lines

    You can refund one or more order lines that have been shipped. The response to a successful call contains the order with the refunded line item.

    :param purchase_order_id: Purchase Order ID
    :type purchase_order_id: str
    :param content_type: application/xml, application/json
    :type content_type: str
    :param accept: application/xml, application/json
    :type accept: str
    :param wm_consumer_channel_type: Channel Type
    :type wm_consumer_channel_type: str
    :param wm_consumer_id: Your Consumer ID
    :type wm_consumer_id: str
    :param wm_sec_timestamp: Epoch timestamp
    :type wm_sec_timestamp: str
    :param wm_sec_auth_signature: Authentication signature
    :type wm_sec_auth_signature: str
    :param wm_svc_name: The Service name
    :type wm_svc_name: str
    :param wm_qos_correlation_id: A Transaction ID
    :type wm_qos_correlation_id: str
    :param request_body: Request body
    :type request_body: str
    :param ship_node: Ship Node
    :type ship_node: str

    """
    return web.Response(status=200)


async def shipping_order(request: web.Request, purchase_order_id, content_type, accept, wm_consumer_channel_type, wm_consumer_id, wm_sec_timestamp, wm_sec_auth_signature, wm_svc_name, wm_qos_correlation_id, request_body, ship_node=None) -> web.Response:
    """Shipping updates

    You can change the status of order lines to \&quot;Shipped\&quot; and trigger the charge to a customer. You must acknowledge your orders before sending a shipping update to avoid underselling. An order line, once marked as shipped, cannot be updated.

    :param purchase_order_id: Purchase Order ID
    :type purchase_order_id: str
    :param content_type: application/xml, application/json
    :type content_type: str
    :param accept: application/xml, application/json
    :type accept: str
    :param wm_consumer_channel_type: Channel Type
    :type wm_consumer_channel_type: str
    :param wm_consumer_id: Your Consumer ID
    :type wm_consumer_id: str
    :param wm_sec_timestamp: Epoch timestamp
    :type wm_sec_timestamp: str
    :param wm_sec_auth_signature: Authentication signature
    :type wm_sec_auth_signature: str
    :param wm_svc_name: The Service name
    :type wm_svc_name: str
    :param wm_qos_correlation_id: A Transaction ID
    :type wm_qos_correlation_id: str
    :param request_body: Request body
    :type request_body: str
    :param ship_node: Ship Node
    :type ship_node: str

    """
    return web.Response(status=200)
