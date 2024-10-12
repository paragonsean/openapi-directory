from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.request_access_token_request import RequestAccessTokenRequest
from openapi_server.models.token_details import TokenDetails
from openapi_server import util


async def request_access_token(request: web.Request, key_name, x_ably_version=None, format=None, body=None) -> web.Response:
    """Request an access token

    This is the means by which clients obtain access tokens to use the service. You can see how to construct an Ably TokenRequest in the [Ably TokenRequest spec](https://www.ably.io/documentation/rest-api/token-request-spec) documentation, although we recommend you use an Ably SDK rather to create a TokenRequest, as the construction of a TokenRequest is complex. The resulting token response object contains the token properties as defined in Ably TokenRequest spec. Authentication is not required if using a Signed TokenRequest.

    :param key_name: The [key name](https://www.ably.io/documentation/rest-api/token-request-spec#api-key-format) comprises of the app ID and key ID of an API key.
    :type key_name: str
    :param x_ably_version: The version of the API you wish to use.
    :type x_ably_version: str
    :param format: The response format you would like
    :type format: str
    :param body: 
    :type body: dict | bytes

    """
    body = RequestAccessTokenRequest.from_dict(body)
    return web.Response(status=200)
