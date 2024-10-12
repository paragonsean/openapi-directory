from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.sales_data_creditmemo_interface import SalesDataCreditmemoInterface
from openapi_server import util


async def sales_creditmemo_management_v1_cancel_put(request: web.Request, id) -> web.Response:
    """creditmemo/{id}

    Cancels a specified credit memo.

    :param id: The credit memo ID.
    :type id: int

    """
    return web.Response(status=200)


async def sales_creditmemo_repository_v1_get_get(request: web.Request, id) -> web.Response:
    """creditmemo/{id}

    Loads a specified credit memo.

    :param id: The credit memo ID.
    :type id: int

    """
    return web.Response(status=200)
