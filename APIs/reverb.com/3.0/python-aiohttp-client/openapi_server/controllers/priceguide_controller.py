from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def priceguide_id_transactions_summary_get(request: web.Request, id, number_of_months=None, condition=None) -> web.Response:
    """Get a summary of transactions for a given price guide

    Get a summary of transactions for a given price guide

    :param id: 
    :type id: str
    :param number_of_months: 
    :type number_of_months: int
    :param condition: 
    :type condition: str

    """
    return web.Response(status=200)
