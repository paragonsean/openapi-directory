from typing import List, Dict
from aiohttp import web

from openapi_server.models.errors_response import ErrorsResponse
from openapi_server.models.token_update_request_schema import TokenUpdateRequestSchema
from openapi_server.models.token_update_response_schema import TokenUpdateResponseSchema
from openapi_server import util


async def token_update_post(request: web.Request, token_update_request_schema=None) -> web.Response:
    """token_update_post

    Used to update Account PAN Mapping Information or Issuer Product Configuration ID associated to a provisioned token. To update a specific token, the API should be requested using the Token Unique Reference. To update all tokens mapped to a specific Account PAN, the API should be requested using the Account PAN. In either case, updates will only be applied to tokens in ACTIVE or SUSPENDED state, not those in IN PROGRESS or DELETED state. When updating Account PAN Mapping Information, the Account PAN, Expiration Date and Sequence Number, may be updated individually or in any combination. Only information provided will be updated. The account mapping will only update an Account PAN for a new Account PAN when they are both in the same Account Range. 

    :param token_update_request_schema: Contains the details of the request message.
    :type token_update_request_schema: dict | bytes

    """
    token_update_request_schema = TokenUpdateRequestSchema.from_dict(token_update_request_schema)
    return web.Response(status=200)
