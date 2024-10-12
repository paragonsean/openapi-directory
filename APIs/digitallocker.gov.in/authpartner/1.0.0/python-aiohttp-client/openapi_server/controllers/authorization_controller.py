from typing import List, Dict
from aiohttp import web

from openapi_server.models.access_response import AccessResponse
from openapi_server.models.getaccesstoken_id_request import GetaccesstokenIdRequest
from openapi_server.models.sample import Sample
from openapi_server import util


async def get_authorization_code_id(request: web.Request, response_type, redirect_uri, state, client_id=None, code_challenge=None, code_challenge_method=None, dl_flow=None, verified_mobile=None) -> web.Response:
    """Get Authorization Code

    Call to this API starts authorization flow using OAuth 2.0 protocol. This isn&#39;t an API call—it&#39;s a DigiLocker web page that lets the user sign in to DigiLocker and authorize your application to access user’s data. After the user decides whether or not to authorize your app, they will be redirected to the redirect link provided by your application.

    :param response_type: Provide the grant type requested, either token or code.
    :type response_type: str
    :param redirect_uri: The URI to redirect the user after authorization has completed.
    :type redirect_uri: str
    :param state: This is your application specific data that will be passed back to your application through redirect_uri.
    :type state: str
    :param client_id: Provide the client id that was created during the application registration process on Partners Portal.
    :type client_id: str
    :param code_challenge: A unique random string called code verifier (code_verifier) is created by the client application for every authorization request. The code_challenge sent as this parameter is the Base64URL (with no padding) encoded SHA256 hash of the code verifier.         Code block:         &#x60;&#x60;&#x60;        string base64_url_encode_without_padding(string arg)        {            string s &#x3D; base64encode(arg); //Regular base64encoder with padding           s &#x3D; s.replace(’&#x3D;’,’’); //Remove any trailing ’&#x3D;’           s &#x3D; s.replace(’+’, ’-’); //Replace ’+’ with ’-’           s &#x3D; s.replace(’/’, ’_’); //Replace ’/’ with ’_’ return s;         }         &#x60;&#x60;&#x60; 
    :type code_challenge: dict | bytes
    :param code_challenge_method: Specifies what method was used to encode a code_verifier to generate code_challenge parameter above. This parameter must be used with the code_challenge parameter. The only supported values for this parameter is S256.
    :type code_challenge_method: dict | bytes
    :param dl_flow: If this parameter is provided its value will always be signup. This parameter indicates that the user does not have a DigiLocker account and will be directed to the signup flow directly. After the account is created, the user will be directed to the authorization flow. If this parameter is not sent, the user will be redirected to the sign in flow.
    :type dl_flow: str
    :param verified_mobile: Verified mobile number of the user. If this parameter is passed, DigiLocker will skip the mobile OTP verification step during sign up. DigiLocker will treat the mobile number passed in this parameter as a verified mobile number by the trusted client application. This parameter will be used only if dl_flow parameter mentioned above is set to signup and will be ignored otherwise.
    :type verified_mobile: int

    """
    code_challenge = .from_dict(code_challenge)
    code_challenge_method = .from_dict(code_challenge_method)
    return web.Response(status=200)


async def getaccesstoken_id(request: web.Request, body) -> web.Response:
    """Get Access Token

    This endpoint only applies to apps using the authorization code flow. An app calls this endpoint to acquire a bearer token once the user has authorized the app. Calls to /oauth2/1/token need to be authenticated using the app&#39;s key and secret. These can either be passed as application/x-www-form-urlencoded POST parameters (see parameters below) or via HTTP basic authentication. If basic authentication is used, the app key should be provided as the username, and the app secret should be provided as the password.

    :param body: Details of documents being created.
    :type body: dict | bytes

    """
    body = GetaccesstokenIdRequest.from_dict(body)
    return web.Response(status=200)
