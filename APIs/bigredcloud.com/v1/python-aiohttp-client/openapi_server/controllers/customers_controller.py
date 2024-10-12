from typing import List, Dict
from aiohttp import web

from openapi_server.models.account_tran_dto import AccountTranDto
from openapi_server.models.batch_item_customer_dto import BatchItemCustomerDto
from openapi_server.models.customer_dto import CustomerDto
from openapi_server.models.owner_opening_balance_dto import OwnerOpeningBalanceDto
from openapi_server.models.owner_opening_balance_in_periods_dto import OwnerOpeningBalanceInPeriodsDto
from openapi_server.models.page_result_customer_query_dto import PageResultCustomerQueryDto
from openapi_server.models.quote_dto import QuoteDto
from openapi_server import util


async def customers_delete(request: web.Request, id, timestamp) -> web.Response:
    """Removes an existing Customer.

    

    :param id: Id of Customer to remove.
    :type id: int
    :param timestamp: Timestamp of Customer to remove. Should be encoded in Base64.
    :type timestamp: str

    """
    return web.Response(status=200)


async def customers_get(request: web.Request, ) -> web.Response:
    """Returns a list of company&#39;s Customers. Supports OData querying protocol.  Filtering is forbidden.  Ordering is allowed by \&quot;id\&quot; and \&quot;code\&quot; fields.

    


    """
    return web.Response(status=200)


async def customers_get_account_trans(request: web.Request, item_id) -> web.Response:
    """Returns a list of Customer&#39;s account transactions.

    

    :param item_id: Id of Customer to return account transaction.
    :type item_id: int

    """
    return web.Response(status=200)


async def customers_get_opening_balance(request: web.Request, item_id) -> web.Response:
    """Returns a Customer&#39;s opening balances, calculated for the next periods: current month, one month old, two months old, three and more months old.

    

    :param item_id: Id of Customer to return opening balances.
    :type item_id: int

    """
    return web.Response(status=200)


async def customers_get_opening_balance_list(request: web.Request, item_id) -> web.Response:
    """Returns a list of Customer&#39;s opening balance transactions.

    

    :param item_id: Id of Customer to return opening balances transaction.
    :type item_id: int

    """
    return web.Response(status=200)


async def customers_get_quotes(request: web.Request, item_id) -> web.Response:
    """Returns a list of Customer&#39;s quotes.

    

    :param item_id: Id of Customer to return quotes.
    :type item_id: int

    """
    return web.Response(status=200)


async def customers_post(request: web.Request, body) -> web.Response:
    """Creates a new Customer.

    

    :param body: Information of Customer to create.
    :type body: dict | bytes

    """
    body = CustomerDto.from_dict(body)
    return web.Response(status=200)


async def customers_process_batch(request: web.Request, body) -> web.Response:
    """Processes a batch of Customers.

    

    :param body: Batch of Customers to process.
    :type body: list | bytes

    """
    body = [BatchItemCustomerDto.from_dict(d) for d in body]
    return web.Response(status=200)


async def customers_put(request: web.Request, id, body) -> web.Response:
    """Updates an existing Customer.

    

    :param id: Id of Customer to update.
    :type id: int
    :param body: Information of Customer to update.
    :type body: dict | bytes

    """
    body = CustomerDto.from_dict(body)
    return web.Response(status=200)


async def v1_customers_id_get(request: web.Request, id, need_balance=None) -> web.Response:
    """Returns information about a single Customer. You may specify that Customer&#39;s ledger balance should be calculated.

    

    :param id: Id of Customer to return.
    :type id: int
    :param need_balance: If \&quot;true\&quot; then Customer&#39;s ledger balance will be calculated; otherwise balance will be returned as 0.
    :type need_balance: bool

    """
    return web.Response(status=200)
