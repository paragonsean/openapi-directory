from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_transaction_response import GetTransactionResponse
from openapi_server.models.list_transactions_response import ListTransactionsResponse
from openapi_server.models.transaction_status_enum import TransactionStatusEnum
from openapi_server import util


async def accounts_account_id_transactions_get(request: web.Request, account_id, page_size=None, filter_status=None, filter_since=None, filter_until=None, filter_category=None, filter_tag=None) -> web.Response:
    """List transactions by account

    Retrieve a list of all transactions for a specific account. The returned list is [paginated](#pagination) and can be scrolled by following the &#x60;next&#x60; and &#x60;prev&#x60; links where present. To narrow the results to a specific date range pass one or both of &#x60;filter[since]&#x60; and &#x60;filter[until]&#x60; in the query string. These filter parameters **should not** be used for pagination. Results are ordered newest first to oldest last. 

    :param account_id: The unique identifier for the account. 
    :type account_id: str
    :param page_size: The number of records to return in each page. 
    :type page_size: int
    :param filter_status: The transaction status for which to return records. This can be used to filter &#x60;HELD&#x60; transactions from those that are &#x60;SETTLED&#x60;. 
    :type filter_status: dict | bytes
    :param filter_since: The start date-time from which to return records, formatted according to rfc-3339. Not to be used for pagination purposes. 
    :type filter_since: str
    :param filter_until: The end date-time up to which to return records, formatted according to rfc-3339. Not to be used for pagination purposes. 
    :type filter_until: str
    :param filter_category: The category identifier for which to filter transactions. Both parent and child categories can be filtered through this parameter. Providing an invalid category identifier results in a &#x60;404&#x60; response. 
    :type filter_category: str
    :param filter_tag: A transaction tag to filter for which to return records. If the tag does not exist, zero records are returned and a success response is given. 
    :type filter_tag: str

    """
    filter_status = .from_dict(filter_status)
    filter_since = util.deserialize_datetime(filter_since)
    filter_until = util.deserialize_datetime(filter_until)
    return web.Response(status=200)


async def transactions_get(request: web.Request, page_size=None, filter_status=None, filter_since=None, filter_until=None, filter_category=None, filter_tag=None) -> web.Response:
    """List transactions

    Retrieve a list of all transactions across all accounts for the currently authenticated user. The returned list is [paginated](#pagination) and can be scrolled by following the &#x60;next&#x60; and &#x60;prev&#x60; links where present. To narrow the results to a specific date range pass one or both of &#x60;filter[since]&#x60; and &#x60;filter[until]&#x60; in the query string. These filter parameters **should not** be used for pagination. Results are ordered newest first to oldest last. 

    :param page_size: The number of records to return in each page. 
    :type page_size: int
    :param filter_status: The transaction status for which to return records. This can be used to filter &#x60;HELD&#x60; transactions from those that are &#x60;SETTLED&#x60;. 
    :type filter_status: dict | bytes
    :param filter_since: The start date-time from which to return records, formatted according to rfc-3339. Not to be used for pagination purposes. 
    :type filter_since: str
    :param filter_until: The end date-time up to which to return records, formatted according to rfc-3339. Not to be used for pagination purposes. 
    :type filter_until: str
    :param filter_category: The category identifier for which to filter transactions. Both parent and child categories can be filtered through this parameter. Providing an invalid category identifier results in a &#x60;404&#x60; response. 
    :type filter_category: str
    :param filter_tag: A transaction tag to filter for which to return records. If the tag does not exist, zero records are returned and a success response is given. 
    :type filter_tag: str

    """
    filter_status = .from_dict(filter_status)
    filter_since = util.deserialize_datetime(filter_since)
    filter_until = util.deserialize_datetime(filter_until)
    return web.Response(status=200)


async def transactions_id_get(request: web.Request, id) -> web.Response:
    """Retrieve transaction

    Retrieve a specific transaction by providing its unique identifier. 

    :param id: The unique identifier for the transaction. 
    :type id: str

    """
    return web.Response(status=200)
