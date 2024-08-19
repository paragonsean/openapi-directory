from typing import List, Dict
from aiohttp import web

from openapi_server.models.merchant_refund_transfer93_wrapper import MerchantRefundTransfer93Wrapper
from openapi_server.models.merchant_transfer104_wrapper import MerchantTransfer104Wrapper
from openapi_server import util


async def create_merchant_refund(request: web.Request, partner_id, merchant_refund_transfer=None) -> web.Response:
    """Initiates a Mastercard Merchant Presented QR Refund transaction by pushing funds from a merchant account back to the customer&#39;s account.

    Initiates a Mastercard Merchant Presented QR Refund transaction by pushing funds from a merchant account back to the customer&#39;s account.

    :param partner_id: Path Param - Provider assigned partner id. Details - string, 32
    :type partner_id: str
    :param merchant_refund_transfer: Contains the details of the request message.
    :type merchant_refund_transfer: dict | bytes

    """
    merchant_refund_transfer = MerchantRefundTransfer93Wrapper.from_dict(merchant_refund_transfer)
    return web.Response(status=200)
