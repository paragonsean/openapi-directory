from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_bank_account_by_v1_id_response import GetBankAccountByV1IdResponse
from openapi_server.models.get_bank_account_response import GetBankAccountResponse
from openapi_server.models.list_bank_accounts_response import ListBankAccountsResponse
from openapi_server import util


async def get_bank_account(request: web.Request, bank_account_id) -> web.Response:
    """GetBankAccount

    Returns details of a [BankAccount](https://developer.squareup.com/reference/square_2021-08-18/objects/BankAccount) linked to a Square account.

    :param bank_account_id: Square-issued ID of the desired &#x60;BankAccount&#x60;.
    :type bank_account_id: str

    """
    return web.Response(status=200)


async def get_bank_account_by_v1_id(request: web.Request, v1_bank_account_id) -> web.Response:
    """GetBankAccountByV1Id

    Returns details of a [BankAccount](https://developer.squareup.com/reference/square_2021-08-18/objects/BankAccount) identified by V1 bank account ID.

    :param v1_bank_account_id: Connect V1 ID of the desired &#x60;BankAccount&#x60;. For more information, see  [Retrieve a bank account by using an ID issued by V1 Bank Accounts API](https://developer.squareup.com/docs/bank-accounts-api#retrieve-a-bank-account-by-using-an-id-issued-by-v1-bank-accounts-api).
    :type v1_bank_account_id: str

    """
    return web.Response(status=200)


async def list_bank_accounts(request: web.Request, cursor=None, limit=None, location_id=None) -> web.Response:
    """ListBankAccounts

    Returns a list of [BankAccount](https://developer.squareup.com/reference/square_2021-08-18/objects/BankAccount) objects linked to a Square account.

    :param cursor: The pagination cursor returned by a previous call to this endpoint. Use it in the next &#x60;ListBankAccounts&#x60; request to retrieve the next set  of results.  See the [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination) guide for more information.
    :type cursor: str
    :param limit: Upper limit on the number of bank accounts to return in the response.  Currently, 1000 is the largest supported limit. You can specify a limit  of up to 1000 bank accounts. This is also the default limit.
    :type limit: int
    :param location_id: Location ID. You can specify this optional filter  to retrieve only the linked bank accounts belonging to a specific location.
    :type location_id: str

    """
    return web.Response(status=200)
