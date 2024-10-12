from typing import List, Dict
from aiohttp import web

from openapi_server.models.billing_details_model import BillingDetailsModel
from openapi_server.models.message_model import MessageModel
from openapi_server import util


async def get_billing_details(request: web.Request, api_key) -> web.Response:
    """Retrieves the Billing Details

    Retrieves the Billing Details.

    :param api_key: apiKey
    :type api_key: str

    """
    return web.Response(status=200)


async def put_billing_details(request: web.Request, api_key, body) -> web.Response:
    """Updates the Billing Details

    Updates the Billing Details.

    :param api_key: apiKey
    :type api_key: str
    :param body: billingDetails
    :type body: dict | bytes

    """
    body = BillingDetailsModel.from_dict(body)
    return web.Response(status=200)
