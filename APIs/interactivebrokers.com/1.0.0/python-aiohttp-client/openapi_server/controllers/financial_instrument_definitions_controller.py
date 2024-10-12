from typing import List, Dict
from aiohttp import web

from openapi_server.models.marketdata_snapshot_get_request_inner import MarketdataSnapshotGetRequestInner
from openapi_server.models.secdef_get200_response_inner import SecdefGet200ResponseInner
from openapi_server import util


async def secdef_get(request: web.Request, body) -> web.Response:
    """Get security definition

    Fields that compose security definition. Allowed combinations, (1) type and symbol and currency, or (2) type, symbol, exchange, and currency, or (3) conid 

    :param body: Order Parameters
    :type body: dict | bytes

    """
    body = MarketdataSnapshotGetRequestInner.from_dict(body)
    return web.Response(status=200)
