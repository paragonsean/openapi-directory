from typing import List, Dict
from aiohttp import web

from openapi_server.models.service_error import ServiceError
from openapi_server.models.store_detail_and_submit_request import StoreDetailAndSubmitRequest
from openapi_server.models.store_detail_and_submit_response import StoreDetailAndSubmitResponse
from openapi_server.models.store_detail_request import StoreDetailRequest
from openapi_server.models.store_detail_response import StoreDetailResponse
from openapi_server.models.submit_request import SubmitRequest
from openapi_server.models.submit_response import SubmitResponse
from openapi_server import util


async def post_store_detail(request: web.Request, body=None) -> web.Response:
    """Store payout details

    Stores payment details under the &#x60;PAYOUT&#x60; recurring contract. These payment details can be used later to submit a payout via the &#x60;/submitThirdParty&#x60; call.

    :param body: 
    :type body: dict | bytes

    """
    body = StoreDetailRequest.from_dict(body)
    return web.Response(status=200)


async def post_store_detail_and_submit_third_party(request: web.Request, body=None) -> web.Response:
    """Store details and submit a payout

    Submits a payout and stores its details for subsequent payouts.  The submitted payout must be confirmed or declined either by a reviewer or via &#x60;/confirmThirdParty&#x60; or &#x60;/declineThirdParty&#x60; calls.

    :param body: 
    :type body: dict | bytes

    """
    body = StoreDetailAndSubmitRequest.from_dict(body)
    return web.Response(status=200)


async def post_submit_third_party(request: web.Request, body=None) -> web.Response:
    """Submit a payout

    Submits a payout using the previously stored payment details. To store payment details, use the &#x60;/storeDetail&#x60; API call.  The submitted payout must be confirmed or declined either by a reviewer or via &#x60;/confirmThirdParty&#x60; or &#x60;/declineThirdParty&#x60; calls.

    :param body: 
    :type body: dict | bytes

    """
    body = SubmitRequest.from_dict(body)
    return web.Response(status=200)
