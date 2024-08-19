from typing import List, Dict
from aiohttp import web

from openapi_server.models.errors_response import ErrorsResponse
from openapi_server.models.token_activation_methods_request_schema import TokenActivationMethodsRequestSchema
from openapi_server.models.token_activation_methods_response_schema import TokenActivationMethodsResponseSchema
from openapi_server import util


async def token_activationmethods_post(request: web.Request, token_activation_methods_request_schema=None) -> web.Response:
    """token_activationmethods_post

    Used to retrieve the available Activation Methods for a token that is awaiting activation. Activation Methods are the means by which a cardholder may complete cardholder authentication with the issuer beyond the scope of MDES. It is possible that there are no Activation Methods for a token when an issuer did not provide any cardholder-specific information with the Tokenization Authorization Request (TAR) pre-digitization network message response. 

    :param token_activation_methods_request_schema: Contains the details of the request message.
    :type token_activation_methods_request_schema: dict | bytes

    """
    token_activation_methods_request_schema = TokenActivationMethodsRequestSchema.from_dict(token_activation_methods_request_schema)
    return web.Response(status=200)
