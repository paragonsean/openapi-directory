from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.sales_data_transaction_interface import SalesDataTransactionInterface
from openapi_server import util


async def sales_transaction_repository_v1_get_get(request: web.Request, id) -> web.Response:
    """transactions/{id}

    Loads a specified transaction.

    :param id: The transaction ID.
    :type id: int

    """
    return web.Response(status=200)
