from typing import List, Dict
from aiohttp import web

from openapi_server.models.errors_response import ErrorsResponse
from openapi_server.models.token_reset_mobile_pin_request_schema import TokenResetMobilePinRequestSchema
from openapi_server.models.token_reset_mobile_pin_response_schema import TokenResetMobilePinResponseSchema
from openapi_server import util


async def token_resetmobilepin_post(request: web.Request, token_reset_mobile_pin_request_schema=None) -> web.Response:
    """token_resetmobilepin_post

    Used to request that the Mobile PIN for a Mastercard Cloud-Based Payment token in a single issuer wallet is reset. The request is passed to the Credential Management System for processing. When the Mobile PIN is a token-level PIN (as opposed to a wallet-level PIN), the cardholder must choose a new PIN within 10 minutes of a Reset Mobile PIN action. Otherwise, the reset will need to be re-requested. 

    :param token_reset_mobile_pin_request_schema: Contains the details of the request message.
    :type token_reset_mobile_pin_request_schema: dict | bytes

    """
    token_reset_mobile_pin_request_schema = TokenResetMobilePinRequestSchema.from_dict(token_reset_mobile_pin_request_schema)
    return web.Response(status=200)
