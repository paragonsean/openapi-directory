from typing import List, Dict
from aiohttp import web

from openapi_server.models.card_transactionsv1 import CardTransactionsv1
from openapi_server.models.card_transactionsv3 import CardTransactionsv3
from openapi_server import util


async def get_transactions_by_account_id_filtered(request: web.Request, ican, date_range_from, date_range_to, search_keyword, transaction_types, offset) -> web.Response:
    """Filtered list of transactions for an account (v1)

    Retrieve a filtered list of transactions against an account. Recommended to use the v3 endpoint instead. * &#x60;dateRangeFrom&#x60; - A millisecond epoch time specifying the date range start date. * &#x60;dateRangeTo&#x60; - A millisecond epoch time specifying the date range end date. * &#x60;searchKeyword&#x60; - Search term to filter by from the reference field (&#x60;myRef&#x60;). * &#x60;transactionTypes&#x60; - One or more of the transaction types above. This field can be repeated multiple times to allow for multiple transaction types. * &#x60;offset&#x60; - The page offset. Defaults to 0. This is the record number that the returned list will start at. E.g. offset &#x3D; 40 and limit &#x3D; 20 will return records 40 to 59. 

    :param ican: 
    :type ican: int
    :param date_range_from: 
    :type date_range_from: int
    :param date_range_to: 
    :type date_range_to: int
    :param search_keyword: 
    :type search_keyword: str
    :param transaction_types: 
    :type transaction_types: List[str]
    :param offset: 
    :type offset: int

    """
    return web.Response(status=200)


async def get_transactions_by_account_idv1(request: web.Request, ican, limit, offset) -> web.Response:
    """List transactions for an account (v1)

    Retrieve a list of transactions against an account. Recommended to use the v3 endpoint instead.

    :param ican: 
    :type ican: int
    :param limit: 
    :type limit: int
    :param offset: 
    :type offset: int

    """
    return web.Response(status=200)


async def get_transactions_by_account_idv3(request: web.Request, ican, limit=None, date_range_from=None, date_range_to=None, start_after=None) -> web.Response:
    """List transactions for an account (v3)

    Retrieve a list of transactions against an account. Initially, use the optional &#x60;limit&#x60;, &#x60;dateRangeFrom&#x60; and &#x60;dateRangeTo&#x60; query params to limit your query, then use the embedded &#x60;next&#x60; or &#x60;prev&#x60; links in the response to get newer or older pages. 

    :param ican: 
    :type ican: int
    :param limit: 
    :type limit: int
    :param date_range_from: 
    :type date_range_from: int
    :param date_range_to: 
    :type date_range_to: int
    :param start_after: 
    :type start_after: str

    """
    return web.Response(status=200)
