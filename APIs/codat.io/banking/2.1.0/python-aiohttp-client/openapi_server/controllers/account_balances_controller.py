from typing import List, Dict
from aiohttp import web

from openapi_server.models.account_balances import AccountBalances
from openapi_server import util


async def list_account_balances(request: web.Request, company_id, connection_id, page, page_size=None, query=None, order_by=None) -> web.Response:
    """List account balances

    Gets a list of balances for a bank account including end-of-day batch balance or running balances per transaction.

    :param company_id: 
    :type company_id: str
    :type company_id: str
    :param connection_id: 
    :type connection_id: str
    :type connection_id: str
    :param page: Page number. [Read more](https://docs.codat.io/using-the-api/paging).
    :type page: int
    :param page_size: Number of records to return in a page. [Read more](https://docs.codat.io/using-the-api/paging).
    :type page_size: int
    :param query: Codat query string. [Read more](https://docs.codat.io/using-the-api/querying).
    :type query: str
    :param order_by: Field to order results by. [Read more](https://docs.codat.io/using-the-api/ordering-results).
    :type order_by: str

    """
    return web.Response(status=200)
