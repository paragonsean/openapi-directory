from typing import List, Dict
from aiohttp import web

from openapi_server.models.complete_source_oauth_request import CompleteSourceOauthRequest
from openapi_server.models.invalid_input_exception_info import InvalidInputExceptionInfo
from openapi_server.models.known_exception_info import KnownExceptionInfo
from openapi_server.models.not_found_known_exception_info import NotFoundKnownExceptionInfo
from openapi_server.models.o_auth_consent_read import OAuthConsentRead
from openapi_server.models.set_instancewide_source_oauth_params_request_body import SetInstancewideSourceOauthParamsRequestBody
from openapi_server.models.source_oauth_consent_request import SourceOauthConsentRequest
from openapi_server import util


async def complete_source_o_auth(request: web.Request, body) -> web.Response:
    """Given a source def ID generate an access/refresh token etc.

    

    :param body: 
    :type body: dict | bytes

    """
    body = CompleteSourceOauthRequest.from_dict(body)
    return web.Response(status=200)


async def get_source_o_auth_consent(request: web.Request, body) -> web.Response:
    """Given a source connector definition ID, return the URL to the consent screen where to redirect the user to.

    

    :param body: 
    :type body: dict | bytes

    """
    body = SourceOauthConsentRequest.from_dict(body)
    return web.Response(status=200)


async def set_instancewide_source_oauth_params(request: web.Request, body) -> web.Response:
    """Sets instancewide variables to be used for the oauth flow when creating this source. When set, these variables will be injected into a connector&#39;s configuration before any interaction with the connector image itself. This enables running oauth flows with consistent variables e.g: the company&#39;s Google Ads developer_token, client_id, and client_secret without the user having to know about these variables. 

    

    :param body: 
    :type body: dict | bytes

    """
    body = SetInstancewideSourceOauthParamsRequestBody.from_dict(body)
    return web.Response(status=200)
