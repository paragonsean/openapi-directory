from typing import List, Dict
from aiohttp import web

from openapi_server.models.errors_response import ErrorsResponse
from openapi_server.models.update_token_assurance_request_schema import UpdateTokenAssuranceRequestSchema
from openapi_server.models.update_token_assurance_response_schema import UpdateTokenAssuranceResponseSchema
from openapi_server import util


async def updatetokenassurance_post(request: web.Request, update_token_assurance_request_schema=None) -> web.Response:
    """updatetokenassurance_post

    Used after an issuer has performed additional cardholder authentication to indicate an increased level of token assurance. It will only be applied to tokens that actually have a Token Assurance Level, and those that are in ACTIVE or SUSPENDED state. 

    :param update_token_assurance_request_schema: Contains the details of the request message.
    :type update_token_assurance_request_schema: dict | bytes

    """
    update_token_assurance_request_schema = UpdateTokenAssuranceRequestSchema.from_dict(update_token_assurance_request_schema)
    return web.Response(status=200)
