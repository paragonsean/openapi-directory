from typing import List, Dict
from aiohttp import web

from openapi_server.models.allowed_origin import AllowedOrigin
from openapi_server.models.allowed_origins_response import AllowedOriginsResponse
from openapi_server.models.create_allowed_origin_request import CreateAllowedOriginRequest
from openapi_server.models.generate_client_key_response import GenerateClientKeyResponse
from openapi_server.models.me_api_credential import MeApiCredential
from openapi_server.models.rest_service_error import RestServiceError
from openapi_server import util


async def delete_me_allowed_origins_origin_id(request: web.Request, origin_id) -> web.Response:
    """Remove allowed origin

    Removes the [allowed origin](https://docs.adyen.com/development-resources/client-side-authentication#allowed-origins) specified in the path. The API key from the request is used to identify the [API credential](https://docs.adyen.com/development-resources/api-credentials).  You can make this request with any of the Management API roles.

    :param origin_id: Unique identifier of the allowed origin.
    :type origin_id: str

    """
    return web.Response(status=200)


async def get_me(request: web.Request, ) -> web.Response:
    """Get API credential details

    Returns your [API credential](https://docs.adyen.com/development-resources/api-credentials) details based on the API Key you used in the request.  You can make this request with any of the Management API roles.


    """
    return web.Response(status=200)


async def get_me_allowed_origins(request: web.Request, ) -> web.Response:
    """Get allowed origins

    Returns the list of [allowed origins](https://docs.adyen.com/development-resources/client-side-authentication#allowed-origins) of your [API credential](https://docs.adyen.com/development-resources/api-credentials) based on the API key you used in the request.  You can make this request with any of the Management API roles.


    """
    return web.Response(status=200)


async def get_me_allowed_origins_origin_id(request: web.Request, origin_id) -> web.Response:
    """Get allowed origin details

    Returns the details of the [allowed origin](https://docs.adyen.com/development-resources/client-side-authentication#allowed-origins) specified in the path. The API key from the request is used to identify the [API credential](https://docs.adyen.com/development-resources/api-credentials).  You can make this request with any of the Management API roles.

    :param origin_id: Unique identifier of the allowed origin.
    :type origin_id: str

    """
    return web.Response(status=200)


async def post_me_allowed_origins(request: web.Request, body=None) -> web.Response:
    """Add allowed origin

    Adds an allowed origin to the list of [allowed origins](https://docs.adyen.com/development-resources/client-side-authentication#allowed-origins) of your API credential. The API key from the request is used to identify the [API credential](https://docs.adyen.com/development-resources/api-credentials).  You can make this request with any of the Management API roles.

    :param body: 
    :type body: dict | bytes

    """
    body = CreateAllowedOriginRequest.from_dict(body)
    return web.Response(status=200)


async def post_me_generate_client_key(request: web.Request, ) -> web.Response:
    """Generate a client key

    Generates a new [client key](https://docs.adyen.com/development-resources/client-side-authentication/) used to authenticate requests from your payment environment. You can use the new client key a few minutes after generating it. The old client key stops working 24 hours after generating a new one.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—API credentials read and write


    """
    return web.Response(status=200)
