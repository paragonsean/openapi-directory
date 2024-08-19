from typing import List, Dict
from aiohttp import web

from openapi_server.models.settlement_rate_issued_request import SettlementRateIssuedRequest
from openapi_server import util


async def is_rate_issued_using_get(request: web.Request, _date=None) -> web.Response:
    """Determine if the settlement rate has been issued.

    Determine if the settlement rate has been issued.

    :param _date: The date by which the rate would have been issued.
    :type _date: str

    """
    return web.Response(status=200)
