from typing import List, Dict
from aiohttp import web

from openapi_server.models.payee_bank_accounts import PayeeBankAccounts
from openapi_server import util


async def get_payees(request: web.Request, ) -> web.Response:
    """List all Payee Bank Accounts

    Returns all your payee bank accounts.   Ordered by payee name ascending.   Can be paginated. 


    """
    return web.Response(status=200)
