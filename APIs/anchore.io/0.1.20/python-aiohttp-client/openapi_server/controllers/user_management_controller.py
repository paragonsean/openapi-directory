from typing import List, Dict
from aiohttp import web

from openapi_server.models.access_credential import AccessCredential
from openapi_server.models.account import Account
from openapi_server.models.account_creation_request import AccountCreationRequest
from openapi_server.models.account_status import AccountStatus
from openapi_server.models.api_error_response import ApiErrorResponse
from openapi_server.models.user import User
from openapi_server.models.user_creation_request import UserCreationRequest
from openapi_server import util


async def create_account(request: web.Request, body) -> web.Response:
    """Create a new user. Only avaialble to admin user.

    

    :param body: 
    :type body: dict | bytes

    """
    body = AccountCreationRequest.from_dict(body)
    return web.Response(status=200)


async def create_user(request: web.Request, accountname, body) -> web.Response:
    """Create a new user

    

    :param accountname: 
    :type accountname: str
    :param body: 
    :type body: dict | bytes

    """
    body = UserCreationRequest.from_dict(body)
    return web.Response(status=200)


async def create_user_credential(request: web.Request, accountname, username, body) -> web.Response:
    """add/replace credential

    

    :param accountname: 
    :type accountname: str
    :param username: 
    :type username: str
    :param body: 
    :type body: dict | bytes

    """
    body = AccessCredential.from_dict(body)
    return web.Response(status=200)


async def delete_account(request: web.Request, accountname) -> web.Response:
    """Delete the specified account, only allowed if the account is in the disabled state. All users will be deleted along with the account and all resources will be garbage collected

    

    :param accountname: 
    :type accountname: str

    """
    return web.Response(status=200)


async def delete_user(request: web.Request, accountname, username) -> web.Response:
    """Delete a specific user credential by username of the credential. Cannot be the credential used to authenticate the request.

    

    :param accountname: 
    :type accountname: str
    :param username: 
    :type username: str

    """
    return web.Response(status=200)


async def delete_user_credential(request: web.Request, accountname, username, credential_type) -> web.Response:
    """Delete a credential by type

    

    :param accountname: 
    :type accountname: str
    :param username: 
    :type username: str
    :param credential_type: 
    :type credential_type: str

    """
    return web.Response(status=200)


async def get_account(request: web.Request, accountname) -> web.Response:
    """Get info about an user. Only available to admin user. Uses the main user Id, not a username.

    

    :param accountname: 
    :type accountname: str

    """
    return web.Response(status=200)


async def get_account_user(request: web.Request, accountname, username) -> web.Response:
    """Get a specific user in the specified account

    

    :param accountname: 
    :type accountname: str
    :param username: 
    :type username: str

    """
    return web.Response(status=200)


async def list_accounts(request: web.Request, state=None) -> web.Response:
    """List user summaries. Only available to the system admin user.

    

    :param state: Filter accounts by state
    :type state: str

    """
    return web.Response(status=200)


async def list_user_credentials(request: web.Request, accountname, username) -> web.Response:
    """Get current credential summary

    

    :param accountname: 
    :type accountname: str
    :param username: 
    :type username: str

    """
    return web.Response(status=200)


async def list_users(request: web.Request, accountname) -> web.Response:
    """List accounts for the user

    

    :param accountname: 
    :type accountname: str

    """
    return web.Response(status=200)


async def update_account_state(request: web.Request, accountname, body) -> web.Response:
    """Update the state of an account to either enabled or disabled. For deletion use the DELETE route

    

    :param accountname: 
    :type accountname: str
    :param body: 
    :type body: dict | bytes

    """
    body = AccountStatus.from_dict(body)
    return web.Response(status=200)
