from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_refund_in import CreateRefundIn
from openapi_server.models.create_refund_out import CreateRefundOut
from openapi_server.models.list_refunds_out import ListRefundsOut
from openapi_server import util


async def create_refund(request: web.Request, key, input) -> web.Response:
    """Create a refund

    

    :param key: Transaction key.
    :type key: str
    :param input: Input
    :type input: dict | bytes

    """
    input = CreateRefundIn.from_dict(input)
    return web.Response(status=200)


async def list_refunds(request: web.Request, key) -> web.Response:
    """Get transaction refunds

    

    :param key: Transaction key.
    :type key: str

    """
    return web.Response(status=200)
