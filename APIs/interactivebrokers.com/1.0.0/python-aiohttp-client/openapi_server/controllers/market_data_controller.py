from typing import List, Dict
from aiohttp import web

from openapi_server.models.marketdata_exchange_components_get200_response_inner import MarketdataExchangeComponentsGet200ResponseInner
from openapi_server.models.marketdata_snapshot_get200_response_inner import MarketdataSnapshotGet200ResponseInner
from openapi_server.models.marketdata_snapshot_get_request_inner import MarketdataSnapshotGetRequestInner
from openapi_server import util


async def marketdata_exchange_components_get(request: web.Request, ) -> web.Response:
    """Exchange Components

    This endpoint provides a bit mapping for the bid/ask/last &#39;market&#39; values in the snapshot response. 


    """
    return web.Response(status=200)


async def marketdata_snapshot_get(request: web.Request, body) -> web.Response:
    """Market Data Snapshot

    This endpoint allows the consumer to request a market data snapshot for one or more trading products.  Consumers need to provide unique identifiers (conids) for the products in the IB product database (retrievable using the /secdef endpoint). The &#39;market&#39; values are integers whose bits indicate the exchange(s) making up the quote.   The mapping of bit to exchange is obtained from the marketdata/exchange_component endpoint. For example, if a bid has a &#39;market&#39; value of 5 and the exchange_component result has the map  0 &#x3D;&gt; NYSE, 1 &#x3D;&gt; ISLAND, 2 &#x3D;&gt; ARCA then the exchanges contributing to the bid size are NYSE and ARCA.   Similarly, if market&#x3D;2, then only ISLAND is contributing. 

    :param body: Contract. Allowed combinations are [type and symbol and currency], or [type, symbol, exchange, and currency], or [conid].
    :type body: list | bytes

    """
    body = [MarketdataSnapshotGetRequestInner.from_dict(d) for d in body]
    return web.Response(status=200)
