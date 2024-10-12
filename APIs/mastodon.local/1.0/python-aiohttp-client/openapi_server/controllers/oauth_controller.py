from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.oauth_revoke_post_request import OauthRevokePostRequest
from openapi_server.models.oauth_token_post200_response import OauthTokenPost200Response
from openapi_server.models.oauth_token_post_request import OauthTokenPostRequest
from openapi_server import util


async def oauth_authorize_get(request: web.Request, response_type, client_id, redirect_uri, scope=None, force_login=None) -> web.Response:
    """oauth_authorize_get

    Displays an authorization form to the user. If approved, it will create and return an authorization code, then redirect to the desired redirect_uri, or show the authorization code if urn:ietf:wg:oauth:2.0:oob was requested. The authorization code can be used while requesting a token to obtain access to user-level methods.

    :param response_type: Should be set equal to code.
    :type response_type: str
    :param client_id: Client ID, obtained during app registration.
    :type client_id: str
    :param redirect_uri: Set a URI to redirect the user to. If this parameter is set to urn:ietf:wg:oauth:2.0:oob then the authorization code will be shown instead. Must match one of the redirect URIs declared during app registration.
    :type redirect_uri: str
    :param scope: List of requested OAuth scopes, separated by spaces (or by pluses, if using query parameters). Must be a subset of scopes declared during app registration. If not provided, defaults to read.
    :type scope: str
    :param force_login: Added in 2.6.0. Forces the user to re-login, which is necessary for authorizing with multiple accounts from the same instance.
    :type force_login: bool

    """
    return web.Response(status=200)


async def oauth_revoke_post(request: web.Request, body=None) -> web.Response:
    """oauth_revoke_post

    Revoke an access token to make it no longer valid for use.

    :param body: 
    :type body: dict | bytes

    """
    body = OauthRevokePostRequest.from_dict(body)
    return web.Response(status=200)


async def oauth_token_post(request: web.Request, body=None) -> web.Response:
    """oauth_token_post

    Returns an access token, to be used during API calls that are not public.

    :param body: 
    :type body: dict | bytes

    """
    body = OauthTokenPostRequest.from_dict(body)
    return web.Response(status=200)
