from typing import List, Dict
from aiohttp import web

from openapi_server.models.bank_account_dto import BankAccountDto
from openapi_server.models.batch_item_bank_account_dto import BatchItemBankAccountDto
from openapi_server.models.page_result_bank_account_query_dto import PageResultBankAccountQueryDto
from openapi_server import util


async def bank_accounts_delete(request: web.Request, id, timestamp) -> web.Response:
    """Removes an existing Bank Account.

    

    :param id: Id of Bank Account to remove.
    :type id: int
    :param timestamp: Timestamp of Bank Account to remove. Should be encoded in Base64.
    :type timestamp: str

    """
    return web.Response(status=200)


async def bank_accounts_get(request: web.Request, ) -> web.Response:
    """Returns a list of company&#39;s Bank Account. Supports OData querying protocol.  Filtering is forbidden.  Ordering is allowed by \&quot;id\&quot; and \&quot;acCode\&quot; fields.

    


    """
    return web.Response(status=200)


async def bank_accounts_post(request: web.Request, body) -> web.Response:
    """Creates a new Bank Account.

    

    :param body: Information of Bank Account to create.
    :type body: dict | bytes

    """
    body = BankAccountDto.from_dict(body)
    return web.Response(status=200)


async def bank_accounts_process_batch(request: web.Request, body) -> web.Response:
    """Processes a batch of Bank Accounts.

    

    :param body: Batch of Bank Accounts to process.
    :type body: list | bytes

    """
    body = [BatchItemBankAccountDto.from_dict(d) for d in body]
    return web.Response(status=200)


async def bank_accounts_put(request: web.Request, id, body) -> web.Response:
    """Updates an existing Bank Account.

    

    :param id: Id of Bank Account to update.
    :type id: int
    :param body: Information of Bank Account to update.
    :type body: dict | bytes

    """
    body = BankAccountDto.from_dict(body)
    return web.Response(status=200)


async def v1_bank_accounts_id_get(request: web.Request, id) -> web.Response:
    """Returns information about a single Bank Account.

    

    :param id: Id of Bank Account to return.
    :type id: int

    """
    return web.Response(status=200)
