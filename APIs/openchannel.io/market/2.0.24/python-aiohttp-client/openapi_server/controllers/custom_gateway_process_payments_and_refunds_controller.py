from typing import List, Dict
from aiohttp import web

from openapi_server.models.transaction import Transaction
from openapi_server import util


async def custom_gateway_payment_ownership_id_post(request: web.Request, ownership_id, amount, _date=None, fee_amount=None, marketplace_amount=None, developer_amount=None, custom_data=None) -> web.Response:
    """Adds a payment for an app on behalf of a user

    - Results are returned for the market provided within the basic authentication credentials  - Payments must be enabled and &#39;Custom&#39; must be selected as the gateway in order to use this API endpoint 

    :param ownership_id: The id of the ownership record involved in this transaction
    :type ownership_id: str
    :param amount: The total amount paid in cents
    :type amount: int
    :param _date: The date (in milliseconds) of when this payment was made
    :type _date: int
    :param fee_amount: The fee (in cents) paid to a payment processors or third parties to process this payment. Default is 0.
    :type fee_amount: int
    :param marketplace_amount: The amount (in cents) paid to the marketplace owner as a commission for the purchase of this app. Defaults based on the commission amount configured for this marketplace.
    :type marketplace_amount: int
    :param developer_amount: The amount (in cents) paid to the owner of the app. Defaults based on the commission amount configured for this marketplace.
    :type developer_amount: int
    :param custom_data: A custom JSON object to attach to this transaction
    :type custom_data: str

    """
    return web.Response(status=200)


async def custom_gateway_refund_ownership_id_post(request: web.Request, ownership_id, amount, _date=None, fee_amount=None, marketplace_amount=None, developer_amount=None, custom_data=None) -> web.Response:
    """Fully or partially refund payment for an app on behalf of a user

    - Results are returned for the market provided within the basic authentication credentials - Payments must be enabled and &#39;Custom&#39; must be selected as the gateway in order to use this API endpoint 

    :param ownership_id: The id of the ownership record involved in this transaction
    :type ownership_id: str
    :param amount: The total amount refunded in cents
    :type amount: int
    :param _date: The date (in milliseconds) of when this refund was made
    :type _date: int
    :param fee_amount: The fee (in cents) recovered from a payment processor or third party to process this payment. The default value is 0
    :type fee_amount: int
    :param marketplace_amount: The amount (in cents) recovered from the marketplace owner as a commission refund for the purchase of this app
    :type marketplace_amount: int
    :param developer_amount: The amount (in cents) recovered from the owner of the app
    :type developer_amount: int
    :param custom_data: A custom JSON object to attach to this transaction
    :type custom_data: str

    """
    return web.Response(status=200)
