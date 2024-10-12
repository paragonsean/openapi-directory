from typing import List, Dict
from aiohttp import web

from openapi_server.models.allowed_origin import AllowedOrigin
from openapi_server.models.allowed_origins_response import AllowedOriginsResponse
from openapi_server.models.rest_service_error import RestServiceError
from openapi_server import util


async def delete_merchants_merchant_id_api_credentials_api_credential_id_allowed_origins_origin_id(request: web.Request, merchant_id, api_credential_id, origin_id) -> web.Response:
    """Delete an allowed origin

    Removes the [allowed origin](https://docs.adyen.com/development-resources/client-side-authentication#allowed-origins) identified in the path. As soon as an allowed origin is removed, we no longer accept client-side requests from that domain.  To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—API credentials read and write

    :param merchant_id: The unique identifier of the merchant account.
    :type merchant_id: str
    :param api_credential_id: Unique identifier of the API credential.
    :type api_credential_id: str
    :param origin_id: Unique identifier of the allowed origin.
    :type origin_id: str

    """
    return web.Response(status=200)


async def get_merchants_merchant_id_api_credentials_api_credential_id_allowed_origins(request: web.Request, merchant_id, api_credential_id) -> web.Response:
    """Get a list of allowed origins

    Returns the list of [allowed origins](https://docs.adyen.com/development-resources/client-side-authentication#allowed-origins) for the API credential identified in the path.  To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—API credentials read and write

    :param merchant_id: The unique identifier of the merchant account.
    :type merchant_id: str
    :param api_credential_id: Unique identifier of the API credential.
    :type api_credential_id: str

    """
    return web.Response(status=200)


async def get_merchants_merchant_id_api_credentials_api_credential_id_allowed_origins_origin_id(request: web.Request, merchant_id, api_credential_id, origin_id) -> web.Response:
    """Get an allowed origin

    Returns the [allowed origin](https://docs.adyen.com/development-resources/client-side-authentication#allowed-origins) identified in the path.  To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—API credentials read and write

    :param merchant_id: The unique identifier of the merchant account.
    :type merchant_id: str
    :param api_credential_id: Unique identifier of the API credential.
    :type api_credential_id: str
    :param origin_id: Unique identifier of the allowed origin.
    :type origin_id: str

    """
    return web.Response(status=200)


async def post_merchants_merchant_id_api_credentials_api_credential_id_allowed_origins(request: web.Request, merchant_id, api_credential_id, body=None) -> web.Response:
    """Create an allowed origin

    Adds a new [allowed origin](https://docs.adyen.com/development-resources/client-side-authentication#allowed-origins) to the API credential&#39;s list of allowed origins.  To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—API credentials read and write

    :param merchant_id: The unique identifier of the merchant account.
    :type merchant_id: str
    :param api_credential_id: Unique identifier of the API credential.
    :type api_credential_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = AllowedOrigin.from_dict(body)
    return web.Response(status=200)
