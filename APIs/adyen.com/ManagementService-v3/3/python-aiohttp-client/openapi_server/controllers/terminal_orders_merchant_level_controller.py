from typing import List, Dict
from aiohttp import web

from openapi_server.models.billing_entities_response import BillingEntitiesResponse
from openapi_server.models.rest_service_error import RestServiceError
from openapi_server.models.shipping_location import ShippingLocation
from openapi_server.models.shipping_locations_response import ShippingLocationsResponse
from openapi_server.models.terminal_models_response import TerminalModelsResponse
from openapi_server.models.terminal_order import TerminalOrder
from openapi_server.models.terminal_order_request import TerminalOrderRequest
from openapi_server.models.terminal_orders_response import TerminalOrdersResponse
from openapi_server.models.terminal_products_response import TerminalProductsResponse
from openapi_server import util


async def get_merchants_merchant_id_billing_entities(request: web.Request, merchant_id, name=None) -> web.Response:
    """Get a list of billing entities

    Returns the billing entities of the merchant account identified in the path. A billing entity is a legal entity where we charge orders to. An order for terminal products must contain the ID of a billing entity.  To make this request, your API credential must have one of the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Terminal ordering read * Management API—Terminal ordering read and write

    :param merchant_id: The unique identifier of the merchant account.
    :type merchant_id: str
    :param name: The name of the billing entity.
    :type name: str

    """
    return web.Response(status=200)


async def get_merchants_merchant_id_shipping_locations(request: web.Request, merchant_id, name=None, offset=None, limit=None) -> web.Response:
    """Get a list of shipping locations

    Returns the shipping locations for the merchant account identified in the path. A shipping location includes the address where orders can be delivered, and an ID which you need to specify when ordering terminal products.  To make this request, your API credential must have one of the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Terminal ordering read * Management API—Terminal ordering read and write

    :param merchant_id: The unique identifier of the merchant account.
    :type merchant_id: str
    :param name: The name of the shipping location.
    :type name: str
    :param offset: The number of locations to skip.
    :type offset: int
    :param limit: The number of locations to return.
    :type limit: int

    """
    return web.Response(status=200)


async def get_merchants_merchant_id_terminal_models(request: web.Request, merchant_id) -> web.Response:
    """Get a list of terminal models

    Returns the payment terminal models that merchant account identified in the path has access to. The response includes the terminal model ID, which can be used as a query parameter when getting a list of terminals or a list of products for ordering.  To make this request, your API credential must have one of the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Terminal ordering read * Management API—Terminal ordering read and write

    :param merchant_id: The unique identifier of the merchant account.
    :type merchant_id: str

    """
    return web.Response(status=200)


async def get_merchants_merchant_id_terminal_orders(request: web.Request, merchant_id, customer_order_reference=None, status=None, offset=None, limit=None) -> web.Response:
    """Get a list of orders

    Returns a list of terminal products orders for the merchant account identified in the path.  To make this request, your API credential must have one of the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Terminal ordering read * Management API—Terminal ordering read and write

    :param merchant_id: 
    :type merchant_id: str
    :param customer_order_reference: Your purchase order number.
    :type customer_order_reference: str
    :param status: The order status. Possible values (not case-sensitive): Placed, Confirmed, Cancelled, Shipped, Delivered.
    :type status: str
    :param offset: The number of orders to skip.
    :type offset: int
    :param limit: The number of orders to return.
    :type limit: int

    """
    return web.Response(status=200)


async def get_merchants_merchant_id_terminal_orders_order_id(request: web.Request, merchant_id, order_id) -> web.Response:
    """Get an order

    Returns the details of the terminal products order identified in the path.  To make this request, your API credential must have one of the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Terminal ordering read * Management API—Terminal ordering read and write

    :param merchant_id: The unique identifier of the merchant account.
    :type merchant_id: str
    :param order_id: The unique identifier of the order.
    :type order_id: str

    """
    return web.Response(status=200)


async def get_merchants_merchant_id_terminal_products(request: web.Request, merchant_id, country, terminal_model_id=None, offset=None, limit=None) -> web.Response:
    """Get a list of terminal products

    Returns a country-specific list of payment terminal packages and parts that the merchant account identified in the path has access to.  To make this request, your API credential must have one of the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Terminal ordering read * Management API—Terminal ordering read and write

    :param merchant_id: The unique identifier of the merchant account.
    :type merchant_id: str
    :param country: The country to return products for, in [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) format. For example, **US**
    :type country: str
    :param terminal_model_id: The terminal model to return products for. Use the ID returned in the [GET &#x60;/terminalModels&#x60;](https://docs.adyen.com/api-explorer/#/ManagementService/latest/get/merchants/{merchantId}/terminalModels) response. For example, **Verifone.M400**
    :type terminal_model_id: str
    :param offset: The number of products to skip.
    :type offset: int
    :param limit: The number of products to return.
    :type limit: int

    """
    return web.Response(status=200)


async def patch_merchants_merchant_id_terminal_orders_order_id(request: web.Request, merchant_id, order_id, body=None) -> web.Response:
    """Update an order

    Updates the terminal products order identified in the path. Updating is only possible while the order has the status **Placed**.  The request body only needs to contain what you want to change.  However, to update the products in the &#x60;items&#x60; array, you must provide the entire array. For example, if the array has three items:  To remove one item, the array must include the remaining two items. Or to add one item, the array must include all four items.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Terminal ordering read and write

    :param merchant_id: The unique identifier of the merchant account.
    :type merchant_id: str
    :param order_id: The unique identifier of the order.
    :type order_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = TerminalOrderRequest.from_dict(body)
    return web.Response(status=200)


async def post_merchants_merchant_id_shipping_locations(request: web.Request, merchant_id, body=None) -> web.Response:
    """Create a shipping location

    Creates a shipping location for the merchant account identified in the path. A shipping location defines an address where orders can be shipped to.   To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Terminal ordering read and write

    :param merchant_id: The unique identifier of the merchant account.
    :type merchant_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ShippingLocation.from_dict(body)
    return web.Response(status=200)


async def post_merchants_merchant_id_terminal_orders(request: web.Request, merchant_id, body=None) -> web.Response:
    """Create an order

    Creates an order for payment terminal products for the merchant account identified in the path.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Terminal ordering read and write &gt;Requests to the Management API test endpoint do not create actual orders for test terminals. To order test terminals, you need to [submit a sales order](https://docs.adyen.com/point-of-sale/managing-terminals/order-terminals/#sales-order-steps) in your Customer Area.

    :param merchant_id: The unique identifier of the merchant account.
    :type merchant_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = TerminalOrderRequest.from_dict(body)
    return web.Response(status=200)


async def post_merchants_merchant_id_terminal_orders_order_id_cancel(request: web.Request, merchant_id, order_id) -> web.Response:
    """Cancel an order

    Cancels the terminal products order identified in the path. Cancelling is only possible while the order has the status **Placed**. To cancel an order, make a POST call without a request body. The response returns the full order details, but with the status changed to **Cancelled**.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Terminal ordering read and write

    :param merchant_id: The unique identifier of the merchant account.
    :type merchant_id: str
    :param order_id: The unique identifier of the order.
    :type order_id: str

    """
    return web.Response(status=200)
