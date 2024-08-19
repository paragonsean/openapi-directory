from typing import List, Dict
from aiohttp import web

from openapi_server.models.merchant_payment_transfer29_wrapper import MerchantPaymentTransfer29Wrapper
from openapi_server.models.merchant_transfer40_wrapper import MerchantTransfer40Wrapper
from openapi_server import util


async def create_merchant_payment(request: web.Request, partner_id, merchant_payment_transfer=None) -> web.Response:
    """Initiates a Mastercard Merchant Presented QR purchase transaction by pushing funds to a merchant account.

    Initiates a Mastercard Merchant Presented QR purchase transaction by pushing funds to a merchant account.

    :param partner_id: Path Param - Provider assigned partner id. Details - string, 32
    :type partner_id: str
    :param merchant_payment_transfer: Contains the details of the request message.
    :type merchant_payment_transfer: dict | bytes

    """
    merchant_payment_transfer = MerchantPaymentTransfer29Wrapper.from_dict(merchant_payment_transfer)
    return web.Response(status=200)
