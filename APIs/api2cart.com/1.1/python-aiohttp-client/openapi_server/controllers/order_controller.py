from typing import List, Dict
from aiohttp import web

from openapi_server.models.account_config_update200_response import AccountConfigUpdate200Response
from openapi_server.models.model_response_order_abandoned_list import ModelResponseOrderAbandonedList
from openapi_server.models.model_response_order_list import ModelResponseOrderList
from openapi_server.models.model_response_order_preestimate_shipping_list import ModelResponseOrderPreestimateShippingList
from openapi_server.models.model_response_order_shipment_list import ModelResponseOrderShipmentList
from openapi_server.models.model_response_order_transaction_list import ModelResponseOrderTransactionList
from openapi_server.models.order_add import OrderAdd
from openapi_server.models.order_add200_response import OrderAdd200Response
from openapi_server.models.order_count200_response import OrderCount200Response
from openapi_server.models.order_financial_status_list200_response import OrderFinancialStatusList200Response
from openapi_server.models.order_find200_response import OrderFind200Response
from openapi_server.models.order_fulfillment_status_list200_response import OrderFulfillmentStatusList200Response
from openapi_server.models.order_info200_response import OrderInfo200Response
from openapi_server.models.order_preestimate_shipping_list import OrderPreestimateShippingList
from openapi_server.models.order_refund_add import OrderRefundAdd
from openapi_server.models.order_refund_add200_response import OrderRefundAdd200Response
from openapi_server.models.order_shipment_add import OrderShipmentAdd
from openapi_server.models.order_shipment_add200_response import OrderShipmentAdd200Response
from openapi_server.models.order_shipment_delete200_response import OrderShipmentDelete200Response
from openapi_server.models.order_shipment_tracking_add import OrderShipmentTrackingAdd
from openapi_server.models.order_shipment_tracking_add200_response import OrderShipmentTrackingAdd200Response
from openapi_server.models.order_shipment_update import OrderShipmentUpdate
from openapi_server.models.order_status_list200_response import OrderStatusList200Response
from openapi_server import util


async def order_abandoned_list(request: web.Request, customer_id=None, customer_email=None, created_to=None, created_from=None, modified_to=None, modified_from=None, skip_empty_email=None, store_id=None, page_cursor=None, count=None, start=None, params=None, response_fields=None, exclude=None) -> web.Response:
    """order_abandoned_list

    Get list of orders that were left by customers before completing the order.

    :param customer_id: Retrieves orders specified by customer id
    :type customer_id: str
    :param customer_email: Retrieves orders specified by customer email
    :type customer_email: str
    :param created_to: Retrieve entities to their creation date
    :type created_to: str
    :param created_from: Retrieve entities from their creation date
    :type created_from: str
    :param modified_to: Retrieve entities to their modification date
    :type modified_to: str
    :param modified_from: Retrieve entities from their modification date
    :type modified_from: str
    :param skip_empty_email: Filter empty emails
    :type skip_empty_email: bool
    :param store_id: Store Id
    :type store_id: str
    :param page_cursor: Used to retrieve entities via cursor-based pagination (it can&#39;t be used with any other filtering parameter)
    :type page_cursor: str
    :param count: This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250
    :type count: int
    :param start: This parameter sets the number from which you want to get entities
    :type start: int
    :param params: Set this parameter in order to choose which entity fields you want to retrieve
    :type params: str
    :param response_fields: Set this parameter in order to choose which entity fields you want to retrieve
    :type response_fields: str
    :param exclude: Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all
    :type exclude: str

    """
    return web.Response(status=200)


async def order_add(request: web.Request, body) -> web.Response:
    """order_add

    Add a new order to the cart.

    :param body: 
    :type body: dict | bytes

    """
    body = OrderAdd.from_dict(body)
    return web.Response(status=200)


async def order_count(request: web.Request, customer_id=None, customer_email=None, order_status=None, order_status_ids=None, created_to=None, created_from=None, modified_to=None, modified_from=None, store_id=None, ids=None, order_ids=None, ebay_order_status=None, financial_status=None, fulfillment_status=None, shipping_method=None, delivery_method=None, ship_node_type=None) -> web.Response:
    """order_count

    Count orders in store

    :param customer_id: Counts orders quantity specified by customer id
    :type customer_id: str
    :param customer_email: Counts orders quantity specified by customer email
    :type customer_email: str
    :param order_status: Counts orders quantity specified by order status
    :type order_status: str
    :param order_status_ids: Retrieves orders specified by order statuses
    :type order_status_ids: List[str]
    :param created_to: Retrieve entities to their creation date
    :type created_to: str
    :param created_from: Retrieve entities from their creation date
    :type created_from: str
    :param modified_to: Retrieve entities to their modification date
    :type modified_to: str
    :param modified_from: Retrieve entities from their modification date
    :type modified_from: str
    :param store_id: Counts orders quantity specified by store id
    :type store_id: str
    :param ids: Counts orders specified by ids
    :type ids: str
    :param order_ids: Counts orders specified by order ids
    :type order_ids: str
    :param ebay_order_status: Counts orders quantity specified by order status
    :type ebay_order_status: str
    :param financial_status: Counts orders quantity specified by financial status
    :type financial_status: str
    :param fulfillment_status: Create order with fulfillment status
    :type fulfillment_status: str
    :param shipping_method: Retrieve entities according to shipping method
    :type shipping_method: str
    :param delivery_method: Retrieves order with delivery method
    :type delivery_method: str
    :param ship_node_type: Retrieves order with ship node type
    :type ship_node_type: str

    """
    return web.Response(status=200)


async def order_financial_status_list(request: web.Request, ) -> web.Response:
    """order_financial_status_list

    Retrieve list of financial statuses


    """
    return web.Response(status=200)


async def order_find(request: web.Request, customer_id=None, customer_email=None, order_status=None, start=None, count=None, params=None, exclude=None, created_to=None, created_from=None, modified_to=None, modified_from=None, financial_status=None) -> web.Response:
    """order_find

    This method is deprecated and won&#39;t be supported in the future. Please use \&quot;order.list\&quot; instead.

    :param customer_id: Retrieves orders specified by customer id
    :type customer_id: str
    :param customer_email: Retrieves orders specified by customer email
    :type customer_email: str
    :param order_status: Retrieves orders specified by order status
    :type order_status: str
    :param start: This parameter sets the number from which you want to get entities
    :type start: int
    :param count: This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250
    :type count: int
    :param params: Set this parameter in order to choose which entity fields you want to retrieve
    :type params: str
    :param exclude: Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all
    :type exclude: str
    :param created_to: Retrieve entities to their creation date
    :type created_to: str
    :param created_from: Retrieve entities from their creation date
    :type created_from: str
    :param modified_to: Retrieve entities to their modification date
    :type modified_to: str
    :param modified_from: Retrieve entities from their modification date
    :type modified_from: str
    :param financial_status: Retrieves orders specified by financial status
    :type financial_status: str

    """
    return web.Response(status=200)


async def order_fulfillment_status_list(request: web.Request, ) -> web.Response:
    """order_fulfillment_status_list

    Retrieve list of fulfillment statuses


    """
    return web.Response(status=200)


async def order_info(request: web.Request, order_id=None, id=None, params=None, response_fields=None, exclude=None, store_id=None, enable_cache=None) -> web.Response:
    """order_info

    Info about a specific order by ID

    :param order_id: Retrieves order’s info specified by order id
    :type order_id: str
    :param id: Retrieves order info specified by id
    :type id: str
    :param params: Set this parameter in order to choose which entity fields you want to retrieve
    :type params: str
    :param response_fields: Set this parameter in order to choose which entity fields you want to retrieve
    :type response_fields: str
    :param exclude: Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all
    :type exclude: str
    :param store_id: Defines store id where the order should be found
    :type store_id: str
    :param enable_cache: If the value is &#39;true&#39; and order exist in our cache, we will return order.info response from cache
    :type enable_cache: bool

    """
    return web.Response(status=200)


async def order_list(request: web.Request, customer_id=None, customer_email=None, phone=None, order_status=None, order_status_ids=None, start=None, count=None, page_cursor=None, sort_by=None, sort_direction=None, params=None, response_fields=None, exclude=None, created_to=None, created_from=None, modified_to=None, modified_from=None, store_id=None, ids=None, order_ids=None, ebay_order_status=None, basket_id=None, financial_status=None, fulfillment_status=None, shipping_method=None, skip_order_ids=None, since_id=None, is_deleted=None, shipping_country_iso3=None, enable_cache=None, delivery_method=None, ship_node_type=None, currency_id=None) -> web.Response:
    """order_list

    Get list of orders from store.

    :param customer_id: Retrieves orders specified by customer id
    :type customer_id: str
    :param customer_email: Retrieves orders specified by customer email
    :type customer_email: str
    :param phone: Filter orders by customer&#39;s phone number
    :type phone: str
    :param order_status: Retrieves orders specified by order status
    :type order_status: str
    :param order_status_ids: Retrieves orders specified by order statuses
    :type order_status_ids: List[str]
    :param start: This parameter sets the number from which you want to get entities
    :type start: int
    :param count: This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250
    :type count: int
    :param page_cursor: Used to retrieve orders via cursor-based pagination (it can&#39;t be used with any other filtering parameter)
    :type page_cursor: str
    :param sort_by: Set field to sort by
    :type sort_by: str
    :param sort_direction: Set sorting direction
    :type sort_direction: str
    :param params: Set this parameter in order to choose which entity fields you want to retrieve
    :type params: str
    :param response_fields: Set this parameter in order to choose which entity fields you want to retrieve
    :type response_fields: str
    :param exclude: Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all
    :type exclude: str
    :param created_to: Retrieve entities to their creation date
    :type created_to: str
    :param created_from: Retrieve entities from their creation date
    :type created_from: str
    :param modified_to: Retrieve entities to their modification date
    :type modified_to: str
    :param modified_from: Retrieve entities from their modification date
    :type modified_from: str
    :param store_id: Store Id
    :type store_id: str
    :param ids: Retrieves orders specified by ids
    :type ids: str
    :param order_ids: Retrieves orders specified by order ids
    :type order_ids: str
    :param ebay_order_status: Retrieves orders specified by order status
    :type ebay_order_status: str
    :param basket_id: Retrieves order’s info specified by basket id.
    :type basket_id: str
    :param financial_status: Retrieves orders specified by financial status
    :type financial_status: str
    :param fulfillment_status: Create order with fulfillment status
    :type fulfillment_status: str
    :param shipping_method: Retrieve entities according to shipping method
    :type shipping_method: str
    :param skip_order_ids: Skipped orders by ids
    :type skip_order_ids: str
    :param since_id: Retrieve entities starting from the specified id.
    :type since_id: int
    :param is_deleted: Filter deleted orders
    :type is_deleted: bool
    :param shipping_country_iso3: Retrieve entities according to shipping country
    :type shipping_country_iso3: str
    :param enable_cache: If the value is &#39;true&#39;, we will cache orders for a 15 minutes in order to increase speed and reduce requests throttling for some methods and shoping platforms (for example order.shipment.add)
    :type enable_cache: bool
    :param delivery_method: Retrieves order with delivery method
    :type delivery_method: str
    :param ship_node_type: Retrieves order with ship node type
    :type ship_node_type: str
    :param currency_id: Currency Id
    :type currency_id: str

    """
    return web.Response(status=200)


async def order_preestimate_shipping_list(request: web.Request, body) -> web.Response:
    """order_preestimate_shipping_list

    Retrieve list of order preestimated shipping methods

    :param body: 
    :type body: dict | bytes

    """
    body = OrderPreestimateShippingList.from_dict(body)
    return web.Response(status=200)


async def order_refund_add(request: web.Request, body) -> web.Response:
    """order_refund_add

    Add a refund to the order.

    :param body: 
    :type body: dict | bytes

    """
    body = OrderRefundAdd.from_dict(body)
    return web.Response(status=200)


async def order_shipment_add(request: web.Request, body) -> web.Response:
    """order_shipment_add

    Add a shipment to the order.

    :param body: 
    :type body: dict | bytes

    """
    body = OrderShipmentAdd.from_dict(body)
    return web.Response(status=200)


async def order_shipment_delete(request: web.Request, shipment_id, order_id, store_id=None) -> web.Response:
    """order_shipment_delete

    Delete order&#39;s shipment.

    :param shipment_id: Shipment id indicates the number of delivery
    :type shipment_id: str
    :param order_id: Defines the order for which the shipment will be deleted
    :type order_id: str
    :param store_id: Store Id
    :type store_id: str

    """
    return web.Response(status=200)


async def order_shipment_info(request: web.Request, id, order_id, start=None, params=None, response_fields=None, exclude=None, store_id=None) -> web.Response:
    """order_shipment_info

    Get information of shipment.

    :param id: Entity id
    :type id: str
    :param order_id: Defines the order id
    :type order_id: str
    :param start: This parameter sets the number from which you want to get entities
    :type start: int
    :param params: Set this parameter in order to choose which entity fields you want to retrieve
    :type params: str
    :param response_fields: Set this parameter in order to choose which entity fields you want to retrieve
    :type response_fields: str
    :param exclude: Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all
    :type exclude: str
    :param store_id: Store Id
    :type store_id: str

    """
    return web.Response(status=200)


async def order_shipment_list(request: web.Request, order_id, page_cursor=None, start=None, count=None, params=None, response_fields=None, exclude=None, created_from=None, created_to=None, modified_from=None, modified_to=None, store_id=None) -> web.Response:
    """order_shipment_list

    Get list of shipments by orders.

    :param order_id: Retrieves shipments specified by order id
    :type order_id: str
    :param page_cursor: Used to retrieve entities via cursor-based pagination (it can&#39;t be used with any other filtering parameter)
    :type page_cursor: str
    :param start: This parameter sets the number from which you want to get entities
    :type start: int
    :param count: This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250
    :type count: int
    :param params: Set this parameter in order to choose which entity fields you want to retrieve
    :type params: str
    :param response_fields: Set this parameter in order to choose which entity fields you want to retrieve
    :type response_fields: str
    :param exclude: Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all
    :type exclude: str
    :param created_from: Retrieve entities from their creation date
    :type created_from: str
    :param created_to: Retrieve entities to their creation date
    :type created_to: str
    :param modified_from: Retrieve entities from their modification date
    :type modified_from: str
    :param modified_to: Retrieve entities to their modification date
    :type modified_to: str
    :param store_id: Store Id
    :type store_id: str

    """
    return web.Response(status=200)


async def order_shipment_tracking_add(request: web.Request, body) -> web.Response:
    """order_shipment_tracking_add

    Add order shipment&#39;s tracking info.

    :param body: 
    :type body: dict | bytes

    """
    body = OrderShipmentTrackingAdd.from_dict(body)
    return web.Response(status=200)


async def order_shipment_update(request: web.Request, body) -> web.Response:
    """order_shipment_update

    Update order&#39;s shipment information.

    :param body: 
    :type body: dict | bytes

    """
    body = OrderShipmentUpdate.from_dict(body)
    return web.Response(status=200)


async def order_status_list(request: web.Request, store_id=None, response_fields=None) -> web.Response:
    """order_status_list

    Retrieve list of statuses

    :param store_id: Store Id
    :type store_id: str
    :param response_fields: Set this parameter in order to choose which entity fields you want to retrieve
    :type response_fields: str

    """
    return web.Response(status=200)


async def order_transaction_list(request: web.Request, order_ids, count=None, store_id=None, params=None, response_fields=None, exclude=None, page_cursor=None) -> web.Response:
    """order_transaction_list

    Retrieve list of order transaction

    :param order_ids: Retrieves order transactions specified by order ids
    :type order_ids: str
    :param count: This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250
    :type count: int
    :param store_id: Store Id
    :type store_id: str
    :param params: Set this parameter in order to choose which entity fields you want to retrieve
    :type params: str
    :param response_fields: Set this parameter in order to choose which entity fields you want to retrieve
    :type response_fields: str
    :param exclude: Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all
    :type exclude: str
    :param page_cursor: Used to retrieve entities via cursor-based pagination (it can&#39;t be used with any other filtering parameter)
    :type page_cursor: str

    """
    return web.Response(status=200)


async def order_update(request: web.Request, order_id, store_id=None, order_status=None, comment=None, admin_comment=None, admin_private_comment=None, date_modified=None, date_finished=None, financial_status=None, fulfillment_status=None, order_payment_method=None, send_notifications=None) -> web.Response:
    """order_update

    Update existing order.

    :param order_id: Defines the orders specified by order id
    :type order_id: str
    :param store_id: Defines store id where the order should be found
    :type store_id: str
    :param order_status: Defines new order&#39;s status
    :type order_status: str
    :param comment: Specifies order comment
    :type comment: str
    :param admin_comment: Specifies admin&#39;s order comment
    :type admin_comment: str
    :param admin_private_comment: Specifies private admin&#39;s order comment
    :type admin_private_comment: str
    :param date_modified: Specifies order&#39;s  modification date
    :type date_modified: str
    :param date_finished: Specifies order&#39;s  finished date
    :type date_finished: str
    :param financial_status: Update order financial status to specified
    :type financial_status: str
    :param fulfillment_status: Create order with fulfillment status
    :type fulfillment_status: str
    :param order_payment_method: Defines order payment method.&lt;br/&gt;Setting order_payment_method on Shopify will also change financial_status field value to &#39;paid&#39;
    :type order_payment_method: str
    :param send_notifications: Send notifications to customer after order was created
    :type send_notifications: bool

    """
    return web.Response(status=200)
