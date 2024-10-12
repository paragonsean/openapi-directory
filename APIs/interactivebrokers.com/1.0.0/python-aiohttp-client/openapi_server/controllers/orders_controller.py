from typing import List, Dict
from aiohttp import web

from openapi_server.models.accounts_account_orders_customer_order_id_put200_response_inner import AccountsAccountOrdersCustomerOrderIdPut200ResponseInner
from openapi_server.models.accounts_account_orders_customer_order_id_put_request import AccountsAccountOrdersCustomerOrderIdPutRequest
from openapi_server.models.accounts_account_orders_post_request import AccountsAccountOrdersPostRequest
from openapi_server.models.order_state import OrderState
from openapi_server import util


async def accounts_account_orders_customer_order_id_delete(request: web.Request, account, customer_order_id) -> web.Response:
    """Cancel Order

    Cancels the order with the referenced Customer Order ID for the account passed in the URL.

    :param account: Account Number
    :type account: str
    :param customer_order_id: Customer Order ID
    :type customer_order_id: str

    """
    return web.Response(status=200)


async def accounts_account_orders_customer_order_id_get(request: web.Request, account, customer_order_id) -> web.Response:
    """Return specific order info

    Returns the order with the referenced Customer Order ID for the account passed in the URL.

    :param account: Account Number
    :type account: str
    :param customer_order_id: Customer Order ID
    :type customer_order_id: str

    """
    return web.Response(status=200)


async def accounts_account_orders_customer_order_id_put(request: web.Request, account, customer_order_id, body) -> web.Response:
    """Modify Order

    Allows the caller to modify the order with the referenced Customer Order ID specified in the URL. A separate Customer Order ID must be provided in the request body for the modification.

    :param account: Account Number
    :type account: str
    :param customer_order_id: Customer Order ID
    :type customer_order_id: str
    :param body: Order Parameters
    :type body: dict | bytes

    """
    body = AccountsAccountOrdersCustomerOrderIdPutRequest.from_dict(body)
    return web.Response(status=200)


async def accounts_account_orders_get(request: web.Request, account) -> web.Response:
    """Open Orders

    Returns a list of orders for the account passed in the URL

    :param account: Account Number
    :type account: str

    """
    return web.Response(status=200)


async def accounts_account_orders_post(request: web.Request, account, body) -> web.Response:
    """Place Order

    Places order

    :param account: Account Number
    :type account: str
    :param body: Order Parameters
    :type body: dict | bytes

    """
    body = AccountsAccountOrdersPostRequest.from_dict(body)
    return web.Response(status=200)
