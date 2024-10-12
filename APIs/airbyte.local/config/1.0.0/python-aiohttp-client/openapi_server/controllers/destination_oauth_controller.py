from typing import List, Dict
from aiohttp import web

from openapi_server.models.complete_destination_o_auth_request import CompleteDestinationOAuthRequest
from openapi_server.models.destination_oauth_consent_request import DestinationOauthConsentRequest
from openapi_server.models.invalid_input_exception_info import InvalidInputExceptionInfo
from openapi_server.models.known_exception_info import KnownExceptionInfo
from openapi_server.models.not_found_known_exception_info import NotFoundKnownExceptionInfo
from openapi_server.models.o_auth_consent_read import OAuthConsentRead
from openapi_server.models.set_instancewide_destination_oauth_params_request_body import SetInstancewideDestinationOauthParamsRequestBody
from openapi_server import util


async def complete_destination_o_auth(request: web.Request, body) -> web.Response:
    """Given a destination def ID generate an access/refresh token etc.

    

    :param body: 
    :type body: dict | bytes

    """
    body = CompleteDestinationOAuthRequest.from_dict(body)
    return web.Response(status=200)


async def get_destination_o_auth_consent(request: web.Request, body) -> web.Response:
    """Given a destination connector definition ID, return the URL to the consent screen where to redirect the user to.

    

    :param body: 
    :type body: dict | bytes

    """
    body = DestinationOauthConsentRequest.from_dict(body)
    return web.Response(status=200)


async def set_instancewide_destination_oauth_params(request: web.Request, body) -> web.Response:
    """Sets instancewide variables to be used for the oauth flow when creating this destination. When set, these variables will be injected into a connector&#39;s configuration before any interaction with the connector image itself. This enables running oauth flows with consistent variables e.g: the company&#39;s Google Ads developer_token, client_id, and client_secret without the user having to know about these variables. 

    

    :param body: 
    :type body: dict | bytes

    """
    body = SetInstancewideDestinationOauthParamsRequestBody.from_dict(body)
    return web.Response(status=200)
