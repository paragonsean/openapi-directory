from typing import List, Dict
from aiohttp import web

from openapi_server.models.merchant_transfer14_wrapper import MerchantTransfer14Wrapper
from openapi_server.models.merchant_transfer1_wrapper import MerchantTransfer1Wrapper
from openapi_server import util


async def create_merchant_transfer(request: web.Request, partner_id, merchant_transfer) -> web.Response:
    """Initiates a Mastercard Merchant Presented QR purchase transaction by securing funds from a consumer’s account with a Funding Transaction and pushing funds to a merchant account with a Payment Transaction.

    Initiates a Mastercard Merchant Presented QR purchase transaction by securing funds from a consumer’s account with a Funding Transaction and pushing funds to a merchant account with a Payment Transaction.

    :param partner_id: Path Param - Provider assigned partner id.   Type: Alphanumeric Special  [a-zA-Z0-9_-], Length: 32
    :type partner_id: str
    :param merchant_transfer: Contains the details of the request message.
    :type merchant_transfer: dict | bytes

    """
    merchant_transfer = MerchantTransfer1Wrapper.from_dict(merchant_transfer)
    return web.Response(status=200)
