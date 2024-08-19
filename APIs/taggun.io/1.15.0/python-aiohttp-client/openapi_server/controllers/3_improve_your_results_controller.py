from typing import List, Dict
from aiohttp import web

from openapi_server.models.bad_request_error import BadRequestError
from openapi_server.models.merchant_name_add_payload import MerchantNameAddPayload
from openapi_server.models.receipt_feedback_add_payload import ReceiptFeedbackAddPayload
from openapi_server.models.result import Result
from openapi_server import util


async def post_api_account_v1_feedback(request: web.Request, apikey, body=None) -> web.Response:
    """Add manually verified receipt data to a given receipt for feedback and training purposes

    

    :param apikey: API authentication key.
    :type apikey: str
    :param body: 
    :type body: dict | bytes

    """
    body = ReceiptFeedbackAddPayload.from_dict(body)
    return web.Response(status=200)


async def post_api_account_v1_merchantname_add(request: web.Request, apikey, body=None) -> web.Response:
    """Add a keyword to your account&#39;s model to predict merchant name. Changes in your account&#39;s model are updated daily.

    

    :param apikey: API authentication key.
    :type apikey: str
    :param body: 
    :type body: dict | bytes

    """
    body = MerchantNameAddPayload.from_dict(body)
    return web.Response(status=200)
