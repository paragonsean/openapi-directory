from typing import List, Dict
from aiohttp import web

from openapi_server.models.update_user_request import UpdateUserRequest
from openapi_server.models.user_access_tokens_response import UserAccessTokensResponse
from openapi_server.models.user_detail_response import UserDetailResponse
from openapi_server.models.user_request import UserRequest
from openapi_server.models.user_response import UserResponse
from openapi_server.models.yodlee_error import YodleeError
from openapi_server import util


async def get_access_tokens(request: web.Request, app_ids) -> web.Response:
    """Get Access Tokens

    The Get Access Tokens service is used to retrieve the access tokens for the application id(s) provided.&lt;br&gt;URL in the response can be used to launch the application for which token is requested.&lt;br&gt;&lt;br&gt;&lt;b&gt;Note:&lt;/b&gt; &lt;li&gt;This endpoint is deprecated for customers using the API Key-based authentication and is applicable only to customers who use the SAML-based authentication.&lt;br&gt;

    :param app_ids: appIds
    :type app_ids: str

    """
    return web.Response(status=200)


async def get_user(request: web.Request, ) -> web.Response:
    """Get User Details

    The get user details service is used to get the user profile information and the application preferences set at the time of user registration.&lt;br&gt;


    """
    return web.Response(status=200)


async def register_user(request: web.Request, body) -> web.Response:
    """Register User

    The register user service is used to register a user in Yodlee.&lt;br&gt;The loginName cannot include spaces and must be between 3 and 150 characters.&lt;br&gt;locale passed must be one of the supported locales for the customer. &lt;br&gt;Currency provided in the input will be respected in the derived services and the amount fields in the response will be provided in the preferred currency.&lt;br&gt;userParam is accepted as a body parameter. &lt;br&gt;&lt;br&gt;&lt;b&gt;Note:&lt;/b&gt; &lt;li&gt;The content type has to be passed as application/json for the body parameter.&lt;/li&gt;

    :param body: userRequest
    :type body: dict | bytes

    """
    body = UserRequest.from_dict(body)
    return web.Response(status=200)


async def saml_login(request: web.Request, issuer, saml_response, source=None) -> web.Response:
    """Saml Login

    The SAML login service is used to authenticate system users with a SAML response.&lt;br&gt;A new user will be created with the input provided if that user isn&#39;t already in the system.&lt;br&gt;For existing users, the system will make updates based on changes or new information.&lt;br&gt;When authentication is successful, a user session token is returned.&lt;br&gt;&lt;br&gt;&lt;b&gt;Note:&lt;/b&gt; &lt;li&gt;The content type has to be passed as application/x-www-form-urlencoded. &lt;li&gt;issuer, source and samlResponse should be passed as body parameters.&lt;/li&gt;

    :param issuer: issuer
    :type issuer: str
    :param saml_response: samlResponse
    :type saml_response: str
    :param source: source
    :type source: str

    """
    return web.Response(status=200)


async def unregister(request: web.Request, ) -> web.Response:
    """Delete User

    The delete user service is used to delete or unregister a user from Yodlee. &lt;br&gt;Once deleted, the information related to the users cannot be retrieved. &lt;br&gt;The HTTP response code is 204 (Success without content)&lt;br&gt;


    """
    return web.Response(status=200)


async def update_user(request: web.Request, body) -> web.Response:
    """Update User Details

    The update user details service is used to update user details like name, address, currency preference, etc.&lt;br&gt;Currency provided in the input will be respected in the &lt;a href&#x3D;\&quot;https://developer.yodlee.com/api-reference#tag/Derived\&quot;&gt;derived&lt;/a&gt; services and the amount fields in the response will be provided in the preferred currency.&lt;br&gt;The HTTP response code is 204 (Success without content). &lt;br&gt;

    :param body: userRequest
    :type body: dict | bytes

    """
    body = UpdateUserRequest.from_dict(body)
    return web.Response(status=200)


async def user_logout(request: web.Request, ) -> web.Response:
    """User Logout

    &lt;b&gt;Deprecated&lt;/b&gt;: This endpoint is deprecated for API Key-based authentication. The user logout service allows the user to log out of the application.&lt;br&gt;The service does not return a response body. The HTTP response code is 204 (Success with no content).&lt;br&gt;


    """
    return web.Response(status=200)
