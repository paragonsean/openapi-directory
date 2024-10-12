from typing import List, Dict
from aiohttp import web

from openapi_server.models.authentication_options import AuthenticationOptions
from openapi_server.models.authentication_token import AuthenticationToken
from openapi_server.models.credential import Credential
from openapi_server.models.customer_jwt import CustomerJWT
from openapi_server.models.error import Error
from openapi_server.models.invalid_error import InvalidError
from openapi_server.models.reset_password_token import ResetPasswordToken
from openapi_server import util


async def delete_authentication_token(request: web.Request, token, organization_id=None) -> web.Response:
    """Logout a customer

    Logout a customer. 

    :param token: The token identifier string.
    :type token: str
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    return web.Response(status=200)


async def delete_credential(request: web.Request, id, organization_id=None) -> web.Response:
    """Delete a credential

    Delete a credential with predefined identifier string. 

    :param id: The resource identifier string.
    :type id: str
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    return web.Response(status=200)


async def delete_password_token(request: web.Request, id, organization_id=None) -> web.Response:
    """Delete a Reset Password Token

    Delete a Reset Password Token with predefined identifier string. 

    :param id: The resource identifier string.
    :type id: str
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    return web.Response(status=200)


async def get_authentication_option(request: web.Request, organization_id=None) -> web.Response:
    """Read current authentication options

    Read current authentication options. 

    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    return web.Response(status=200)


async def get_authentication_token_collection(request: web.Request, organization_id=None, limit=None, offset=None) -> web.Response:
    """Retrieve a list of auth tokens

    Retrieve a list of auth tokens. 

    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str
    :param limit: The collection items limit.
    :type limit: int
    :param offset: The collection items offset.
    :type offset: int

    """
    return web.Response(status=200)


async def get_authentication_token_verification(request: web.Request, token, organization_id=None) -> web.Response:
    """Verify

    Verify an authentication token. 

    :param token: The token identifier string.
    :type token: str
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    return web.Response(status=200)


async def get_credential(request: web.Request, id, organization_id=None) -> web.Response:
    """Retrieve a credential

    Retrieve a credential with specified identifier string. 

    :param id: The resource identifier string.
    :type id: str
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    return web.Response(status=200)


async def get_credential_collection(request: web.Request, organization_id=None, limit=None, offset=None) -> web.Response:
    """Retrieve a list of credentials

    Retrieve a list of credentials. 

    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str
    :param limit: The collection items limit.
    :type limit: int
    :param offset: The collection items offset.
    :type offset: int

    """
    return web.Response(status=200)


async def get_password_token(request: web.Request, id, organization_id=None) -> web.Response:
    """Retrieve a Reset Password Token

    Retrieve a Reset Password Token with specified identifier string. 

    :param id: The resource identifier string.
    :type id: str
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    return web.Response(status=200)


async def get_password_token_collection(request: web.Request, organization_id=None, limit=None, offset=None) -> web.Response:
    """Retrieve a list of tokens

    Retrieve a list of tokens. 

    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str
    :param limit: The collection items limit.
    :type limit: int
    :param offset: The collection items offset.
    :type offset: int

    """
    return web.Response(status=200)


async def post_authentication_token(request: web.Request, body, organization_id=None) -> web.Response:
    """Login

    Login a customer. 

    :param body: AuthenticationToken resource.
    :type body: dict | bytes
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    body = AuthenticationToken.from_dict(body)
    return web.Response(status=200)


async def post_authentication_token_exchange(request: web.Request, token, body, organization_id=None) -> web.Response:
    """Exchange

    Exchange Authentication Token for JWT.  It will also invalidate an Authentication Token by default (so it can only be exchanged once). 

    :param token: The token identifier string.
    :type token: str
    :param body: 
    :type body: dict | bytes
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    body = CustomerJWT.from_dict(body)
    return web.Response(status=200)


async def post_credential(request: web.Request, body, organization_id=None) -> web.Response:
    """Create a credential

    Create a credential. 

    :param body: Credential resource.
    :type body: dict | bytes
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    body = Credential.from_dict(body)
    return web.Response(status=200)


async def post_password_token(request: web.Request, body, organization_id=None) -> web.Response:
    """Create a Reset Password Token

    Create a Reset Password Token. 

    :param body: ResetPasswordToken resource.
    :type body: dict | bytes
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    body = ResetPasswordToken.from_dict(body)
    return web.Response(status=200)


async def put_authentication_option(request: web.Request, body, organization_id=None) -> web.Response:
    """Change authentication options

    Change options. 

    :param body: Authentication Options resource.
    :type body: dict | bytes
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    body = AuthenticationOptions.from_dict(body)
    return web.Response(status=200)


async def put_credential(request: web.Request, id, body, organization_id=None) -> web.Response:
    """Create or update a credential with predefined ID

    Create or update a credential with predefined identifier string. 

    :param id: The resource identifier string.
    :type id: str
    :param body: Credential resource.
    :type body: dict | bytes
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    body = Credential.from_dict(body)
    return web.Response(status=200)
