from typing import List, Dict
from aiohttp import web

from openapi_server.models.access_token_response import AccessTokenResponse
from openapi_server.models.access_token_validation_request import AccessTokenValidationRequest
from openapi_server.models.auth_response import AuthResponse
from openapi_server.models.inline_response400 import InlineResponse400
from openapi_server.models.inline_response401 import InlineResponse401
from openapi_server.models.inline_response403 import InlineResponse403
from openapi_server.models.reset_password_request import ResetPasswordRequest
from openapi_server import util


async def logout(request: web.Request, ) -> web.Response:
    """Logout

    &lt;p&gt;Given a valid access token in the header then log out the authenticated user or client &lt;/p&gt; &lt;p&gt;Will revoke the token&lt;/p&gt; 


    """
    return web.Response(status=200)


async def reset_password(request: web.Request, body) -> web.Response:
    """Reset password

    &lt;p&gt;Reset password &lt;/p&gt; &lt;p&gt;An email with an embedded link will be sent to the receipient of the email address &lt;/p&gt; &lt;p&gt;The link will contain a token to be used for resetting the password &lt;/p&gt; 

    :param body: An Email address to send the reset password link to
    :type body: dict | bytes

    """
    body = ResetPasswordRequest.from_dict(body)
    return web.Response(status=200)


async def validate_access_token(request: web.Request, body, authorization=None) -> web.Response:
    """validate

    &lt;p&gt;The second part of login involves validating using an MFA device&lt;/p&gt; &lt;p&gt;An access token with PRE_AUTH authorities is required&lt;/p&gt; 

    :param body: An OTP from the user&#39;s registered MFA Device 
    :type body: dict | bytes
    :param authorization: Bearer token authorization leg of validate
    :type authorization: str

    """
    body = AccessTokenValidationRequest.from_dict(body)
    return web.Response(status=200)


async def velo_auth(request: web.Request, grant_type=None) -> web.Response:
    """Authentication endpoint

    &lt;p&gt;Use this endpoint to obtain an access token for calling Velo Payments APIs. &lt;/p&gt; &lt;p&gt;You need your API key and API secret issued by Velo&lt;/p&gt; &lt;p&gt;To login and get an access token the API key and API secret must be Base64 encoded by concatenating them with a colon between them&lt;/p&gt; &lt;p&gt;e.g. Given an ApiKey: 44a9537d-d55d-4b47-8082-14061c2bcdd8 and ApiSecret: c396b26b-137a-44fd-87f5-34631f8fd529&lt;/p&gt; &lt;p&gt;Using a Base64 encode function Base64Encoder().encode(\&quot;44a9537d-d55d-4b47-8082-14061c2bcdd8:c396b26b-137a-44fd-87f5-34631f8fd529\&quot;)&lt;/p&gt; &lt;p&gt;Included as a Basic Authorization header: -H \&quot;Authorization: Basic NDRhOTUzN2QtZDU1ZC00YjQ3LTgwODItMTQwNjFjMmJjZGQ4OmMzOTZiMjZiLTEzN2EtNDRmZC04N2Y1LTM0NjMxZjhmZDUyOQ&#x3D;&#x3D;\&quot; &lt;/p&gt; 

    :param grant_type: OAuth grant type. Should use &#39;client_credentials&#39;
    :type grant_type: str

    """
    return web.Response(status=200)
