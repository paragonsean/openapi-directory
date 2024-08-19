from typing import List, Dict
from aiohttp import web

from openapi_server.models.order_information_class import OrderInformationClass
from openapi_server import util


async def create_order(request: web.Request, api_id, merchant_id, pay_currency, receive_currency, sign, callback_url=None, culture=None, description=None, failure_url=None, order_id=None, pay_amount=None, payer_email=None, payer_name=None, payer_surname=None, receive_amount=None, success_url=None) -> web.Response:
    """Create merchant order

    

    :param api_id: API ID of specific API you have configured on your merchant account
    :type api_id: int
    :param merchant_id: Merchant ID assigned to your account
    :type merchant_id: int
    :param pay_currency: Currency of pay amount
    :type pay_currency: str
    :param receive_currency: Currency of receive amount
    :type receive_currency: str
    :param sign: Signature required for signing create order request
    :type sign: str
    :param callback_url: Url of merchant endpoint callback about order status to be returned
    :type callback_url: str
    :param culture: Merchant customer culture payment window to be presented
    :type culture: str
    :param description: Order description. Will be presented for merchant customer at payment window
    :type description: str
    :param failure_url: Url of merchant page customer should be redirected after unsuccessful payment
    :type failure_url: str
    :param order_id: Custom order ID. Must be unique per API. If not provided it will be generated.
    :type order_id: str
    :param pay_amount: Pay amount in pay currency of value which should be paid by merchant customer. If not provided receive amount will be used to calculate pay amount
    :type pay_amount: 
    :param payer_email: Specified payer email.
    :type payer_email: str
    :param payer_name: Specified payer name.
    :type payer_name: str
    :param payer_surname: Specified payer surname.
    :type payer_surname: str
    :param receive_amount: Receive amount in receive currency of value that merchant will be funded after merchant customers payment approval. If not provided pay amount will be used to calculate receive amount
    :type receive_amount: 
    :param success_url: Url of merchant page customer should be redirected after successful payment
    :type success_url: str

    """
    return web.Response(status=200)
