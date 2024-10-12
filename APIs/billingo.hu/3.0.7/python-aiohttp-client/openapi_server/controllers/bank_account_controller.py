from typing import List, Dict
from aiohttp import web

from openapi_server.models.bank_account import BankAccount
from openapi_server.models.bank_account_list import BankAccountList
from openapi_server.models.client_error_response import ClientErrorResponse
from openapi_server.models.server_error_response import ServerErrorResponse
from openapi_server.models.validation_error_response import ValidationErrorResponse
from openapi_server import util


async def create_bank_account(request: web.Request, body) -> web.Response:
    """Create a bank account

    Create a new bank account. Returns a bank account object if the create is succeded.

    :param body: BankAccount object that you would like to store.
    :type body: dict | bytes

    """
    body = BankAccount.from_dict(body)
    return web.Response(status=200)


async def delete_bank_account(request: web.Request, id) -> web.Response:
    """Delete a bank account

    Delete an existing bank account.

    :param id: 
    :type id: int

    """
    return web.Response(status=200)


async def get_bank_account(request: web.Request, id) -> web.Response:
    """Retrieve a bank account

    Retrieves the details of an existing bank account.

    :param id: 
    :type id: int

    """
    return web.Response(status=200)


async def list_bank_account(request: web.Request, page=None, per_page=None) -> web.Response:
    """List all bank account

    Returns a list of your bank accounts. The bank accounts are returned sorted by creation date, with the most recent bank account appearing first.

    :param page: 
    :type page: int
    :param per_page: 
    :type per_page: int

    """
    return web.Response(status=200)


async def update_bank_account(request: web.Request, id, body) -> web.Response:
    """Update a bank account

    Update an existing bank accounts. Returns a bank account object if the update is succeded.

    :param id: 
    :type id: int
    :param body: Bank account object that you would like to update.
    :type body: dict | bytes

    """
    body = BankAccount.from_dict(body)
    return web.Response(status=200)
