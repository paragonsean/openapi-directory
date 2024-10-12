from typing import List, Dict
from aiohttp import web

from openapi_server.models.account_tran_dto import AccountTranDto
from openapi_server.models.batch_item_supplier_dto import BatchItemSupplierDto
from openapi_server.models.owner_opening_balance_dto import OwnerOpeningBalanceDto
from openapi_server.models.owner_opening_balance_in_periods_dto import OwnerOpeningBalanceInPeriodsDto
from openapi_server.models.page_result_supplier_query_dto import PageResultSupplierQueryDto
from openapi_server.models.supplier_dto import SupplierDto
from openapi_server import util


async def suppliers_delete(request: web.Request, id, timestamp) -> web.Response:
    """Removes an existing Supplier.

    

    :param id: Id of Supplier to remove.
    :type id: int
    :param timestamp: Timestamp of Supplier to remove. Should be encoded in Base64.
    :type timestamp: str

    """
    return web.Response(status=200)


async def suppliers_get(request: web.Request, ) -> web.Response:
    """Returns a list of company&#39;s Suppliers. Supports OData querying protocol.  Filtering is forbidden.  Ordering is allowed by \&quot;id\&quot; and \&quot;code\&quot; fields.

    


    """
    return web.Response(status=200)


async def suppliers_get_account_trans(request: web.Request, item_id) -> web.Response:
    """Returns a list of Supplier&#39;s account transactions.

    

    :param item_id: Id of Supplier to return account transaction.
    :type item_id: int

    """
    return web.Response(status=200)


async def suppliers_get_opening_balance(request: web.Request, item_id) -> web.Response:
    """Returns a Supplier&#39;s opening balances, calculated for the next periods: current month, one month old, two months old, three and more months old.

    

    :param item_id: Id of Supplier to return opening balances.
    :type item_id: int

    """
    return web.Response(status=200)


async def suppliers_get_opening_balance_list(request: web.Request, item_id) -> web.Response:
    """Returns a list of Supplier&#39;s opening balance transactions.

    

    :param item_id: Id of Supplier to return opening balances transaction.
    :type item_id: int

    """
    return web.Response(status=200)


async def suppliers_post(request: web.Request, body) -> web.Response:
    """Creates a new Supplier.

    

    :param body: Information of Supplier to create.
    :type body: dict | bytes

    """
    body = SupplierDto.from_dict(body)
    return web.Response(status=200)


async def suppliers_process_batch(request: web.Request, body) -> web.Response:
    """Processes a batch of Suppliers.

    

    :param body: Batch of Suppliers to process.
    :type body: list | bytes

    """
    body = [BatchItemSupplierDto.from_dict(d) for d in body]
    return web.Response(status=200)


async def suppliers_put(request: web.Request, id, body) -> web.Response:
    """Updates an existing Supplier.

    

    :param id: Id of Supplier to update.
    :type id: int
    :param body: Information of Supplier to update.
    :type body: dict | bytes

    """
    body = SupplierDto.from_dict(body)
    return web.Response(status=200)


async def v1_suppliers_id_get(request: web.Request, id, need_balance=None) -> web.Response:
    """Returns information about a single Supplier. You may specify that Supplier&#39;s ledger balance should be calculated.

    

    :param id: Id of Supplier to return.
    :type id: int
    :param need_balance: If \&quot;true\&quot; then Supplier&#39;s ledger balance will be calculated; otherwise balance will be returned as 0.
    :type need_balance: bool

    """
    return web.Response(status=200)
