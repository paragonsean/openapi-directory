from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_order_request import CreateOrderRequest
from openapi_server.models.customer_token_creation_request import CustomerTokenCreationRequest
from openapi_server.models.customer_token_creation_response import CustomerTokenCreationResponse
from openapi_server.models.error_v2 import ErrorV2
from openapi_server.models.order import Order
from openapi_server import util


async def cancel_authorization(request: web.Request, authorization_token) -> web.Response:
    """Cancel an existing authorization

    Use this API call to cancel/release an authorization. If the &#x60;authorization_token&#x60; received during a Klarna Payments won’t be used to place an order immediately you could release the authorization. Read more on **[Cancel an existing authorization](https://docs.klarna.com/klarna-payments/other-actions/cancel-an-authorization/)**.

    :param authorization_token: 
    :type authorization_token: str

    """
    return web.Response(status=200)


async def create_order(request: web.Request, authorization_token, body=None) -> web.Response:
    """Create a new order

    Use this API call to create a new order. Placing an order towards Klarna means that the Klarna Payments session will be closed and that an order will be created in Klarna&#39;s system.&lt;br/&gt;When you have received the &#x60;authorization_token&#x60; for a successful authorization you can place the order. Among the other order details in this request, you include a URL to the confirmation page for the customer.&lt;br/&gt;When the Order has been successfully placed at Klarna, you need to handle it either through the Merchant Portal or using [Klarna’s Order Management API](#order-management-api). Read more on **[Create a new order](https://docs.klarna.com/klarna-payments/integrate-with-klarna-payments/step-3-create-an-order/)**.

    :param authorization_token: 
    :type authorization_token: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateOrderRequest.from_dict(body)
    return web.Response(status=200)


async def purchase_token(request: web.Request, authorization_token, body=None) -> web.Response:
    """Generate a consumer token

    Use this API call to create a Klarna Customer Token.&lt;br/&gt;After having obtained an &#x60;authorization_token&#x60; for a successful authorization, this can be used to create a purchase token instead of placing the order. Creating a Klarna Customer Token results in Klarna storing customer and payment method details. Read more on **[Generate a consumer token](https://docs.klarna.com/klarna-payments/in-depth-knowledge/customer-token/)**.

    :param authorization_token: 
    :type authorization_token: str
    :param body: 
    :type body: dict | bytes

    """
    body = CustomerTokenCreationRequest.from_dict(body)
    return web.Response(status=200)
