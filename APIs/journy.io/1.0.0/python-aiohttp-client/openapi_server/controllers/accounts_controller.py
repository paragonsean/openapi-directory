from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_user_to_account_request import AddUserToAccountRequest
from openapi_server.models.delete_account202_response import DeleteAccount202Response
from openapi_server.models.delete_account400_response import DeleteAccount400Response
from openapi_server.models.delete_account_request import DeleteAccountRequest
from openapi_server.models.upsert_account201_response import UpsertAccount201Response
from openapi_server.models.upsert_account_request import UpsertAccountRequest
from openapi_server import util


async def add_user_to_account(request: web.Request, body) -> web.Response:
    """Add users to an account

    You can add up to 100 users to an account.

    :param body: 
    :type body: dict | bytes

    """
    body = AddUserToAccountRequest.from_dict(body)
    return web.Response(status=200)


async def delete_account(request: web.Request, body) -> web.Response:
    """Delete account

    Endpoint used to delete an account.

    :param body: 
    :type body: dict | bytes

    """
    body = DeleteAccountRequest.from_dict(body)
    return web.Response(status=200)


async def remove_user_from_account(request: web.Request, body) -> web.Response:
    """Remove user from account

    You can remove up to 100 users from an account.  When removing a user, the user will still be stored in journy.io, but marked as \&quot;removed\&quot;. 

    :param body: 
    :type body: dict | bytes

    """
    body = AddUserToAccountRequest.from_dict(body)
    return web.Response(status=200)


async def upsert_account(request: web.Request, body) -> web.Response:
    """Create or update account

    Endpoint used to create or update an account.

    :param body: 
    :type body: dict | bytes

    """
    body = UpsertAccountRequest.from_dict(body)
    return web.Response(status=200)
