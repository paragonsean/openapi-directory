from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def retrieve_account_transactions_v2(request: web.Request, id, country=None, date_from=None, date_to=None) -> web.Response:
    """retrieve_account_transactions_v2

    Access account premium transactions.

    :param id: 
    :type id: str
    :type id: str
    :param country: ISO 3166 two-character country code
    :type country: str
    :param date_from: 
    :type date_from: str
    :param date_to: 
    :type date_to: str

    """
    date_from = util.deserialize_date(date_from)
    date_to = util.deserialize_date(date_to)
    return web.Response(status=200)
