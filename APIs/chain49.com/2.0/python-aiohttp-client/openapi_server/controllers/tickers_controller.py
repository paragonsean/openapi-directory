from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_tickers_list_v2200_response import GetTickersListV2200Response
from openapi_server.models.get_tickers_v2200_response import GetTickersV2200Response
from openapi_server import util


async def get_tickers_list_v2(request: web.Request, blockchain, timestamp=None) -> web.Response:
    """Get Tickers list V2

    Returns a list of available currency rate tickers (secondary currencies) for the specified date, along with an actual data timestamp.  Trailing slash &#39;/&#39; is mandatory

    :param blockchain: Blockchain name
    :type blockchain: str
    :param timestamp: specifies a Unix timestamp to (/tickers-list) return available tickers for or (/tickers) that specifies a date to return currency rates for. If not specified, the last available rate will be returned.
    :type timestamp: str

    """
    return web.Response(status=200)


async def get_tickers_v2(request: web.Request, blockchain, timestamp=None, currency=None) -> web.Response:
    """Get Tickers V2

    Returns currency rate for the specified currency and date. If the currency is not available for that specific timestamp, the next closest rate will be returned. All responses contain an actual rate timestamp.

    :param blockchain: Blockchain name
    :type blockchain: str
    :param timestamp: specifies a Unix timestamp to (/tickers-list) return available tickers for or (/tickers) that specifies a date to return currency rates for. If not specified, the last available rate will be returned.
    :type timestamp: str
    :param currency: specifies a currency of returned rate (\&quot;usd\&quot;, \&quot;eur\&quot;, \&quot;eth\&quot;...). If not specified, all available currencies will be returned
    :type currency: str

    """
    return web.Response(status=200)
