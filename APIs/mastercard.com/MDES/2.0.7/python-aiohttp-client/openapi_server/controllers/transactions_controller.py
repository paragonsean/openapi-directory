from typing import List, Dict
from aiohttp import web

from openapi_server.models.errors_response import ErrorsResponse
from openapi_server.models.transactions_request_schema import TransactionsRequestSchema
from openapi_server.models.transactions_response_schema import TransactionsResponseSchema
from openapi_server import util


async def transactions_post(request: web.Request, transactions_request_schema=None) -> web.Response:
    """transactions_post

    Used to retrieve transactions performed by a token. It only returns transactions performed within the last 30 days, to help identify a particular token, or to identify a particular recent transaction. It is not intended to provide the full transaction history of a token or Account PAN.&lt;br&gt;&lt;br&gt;_Notes:_ The Transaction History API response is not supported for static Card on File (CoF) tokens.&lt;br&gt;If a set of tokens has been re-mapped to a new FPAN, all digital transactions will be made available before or after the FPAN has been updated. MDES does not return the value of the FPAN which was mapped to the particular token at the time of the transaction. However, MDES will return the history of all transactions performed on that particular token in the last 30 days, based on old and/or new FPAN. 

    :param transactions_request_schema: Contains the details of the request message.
    :type transactions_request_schema: dict | bytes

    """
    transactions_request_schema = TransactionsRequestSchema.from_dict(transactions_request_schema)
    return web.Response(status=200)
