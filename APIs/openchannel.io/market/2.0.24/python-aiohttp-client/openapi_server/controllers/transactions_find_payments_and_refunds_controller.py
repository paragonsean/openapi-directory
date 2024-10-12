from typing import List, Dict
from aiohttp import web

from openapi_server.models.transaction import Transaction
from openapi_server.models.transaction_pages import TransactionPages
from openapi_server import util


async def transactions_get(request: web.Request, query=None, sort=None, page_number=None, limit=None) -> web.Response:
    """Returns a paginated list of transactions

    - Results are paginated and the default is value is 100 if no limit is provided 

    :param query: A query document. Example: {&#39;userId&#39;:&#39;1&#39;} matches all the transactions that have the userId &#39;1&#39;.
    :type query: str
    :param sort: A sort document. Example: {&#39;date&#39;:1} sorts the results by total in ascending order
    :type sort: str
    :param page_number: The result set page number to be returned
    :type page_number: int
    :param limit: The maximum number of results to return per page
    :type limit: int

    """
    return web.Response(status=200)


async def transactions_transaction_id_delete(request: web.Request, transaction_id) -> web.Response:
    """Deleted a transaction

    - Results are returned for the market provided within the basic authentication credentials 

    :param transaction_id: The id of the transaction to be deleted
    :type transaction_id: str

    """
    return web.Response(status=200)


async def transactions_transaction_id_get(request: web.Request, transaction_id) -> web.Response:
    """Returns a transaction

    - Results are returned for the market provided within the basic authentication credentials 

    :param transaction_id: The id of the transaction to return
    :type transaction_id: str

    """
    return web.Response(status=200)


async def transactions_transaction_id_post(request: web.Request, transaction_id, custom_data=None) -> web.Response:
    """Updates a transaction

    - Results are returned for the market provided within the basic authentication credentials 

    :param transaction_id: The id of the transaction to be updated
    :type transaction_id: str
    :param custom_data: A custom JSON object that you can create and attach to this record
    :type custom_data: str

    """
    return web.Response(status=200)
