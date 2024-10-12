from typing import List, Dict
from aiohttp import web

from openapi_server.models.healthcheck200_response import Healthcheck200Response
from openapi_server.models.healthcheck400_response import Healthcheck400Response
from openapi_server.models.historical_exchange_rate200_response import HistoricalExchangeRate200Response
from openapi_server import util


async def healthcheck(request: web.Request, ) -> web.Response:
    """Healthcheck

    Check that the service is up. If everything is okay, you&#39;ll get a 200 OK response.  Otherwise, the request will fail with a 400 error, and a response listing the failed services.


    """
    return web.Response(status=200)


async def historical_exchange_rate(request: web.Request, apikey, base, target, _date) -> web.Response:
    """Historical Exchange Rate

    Get the exchange rate on a specific date

    :param apikey: Authentication key.
    :type apikey: str
    :param base: The source currency.
    :type base: str
    :param target: The target currency.
    :type target: str
    :param _date: The date to get the exchange rate.
    :type _date: str

    """
    return web.Response(status=200)


async def list_of_supported_currencies(request: web.Request, apikey) -> web.Response:
    """List of supported currencies

    Get the list of supported currencies, currently 220 currencies are supported.

    :param apikey: Authentication key.
    :type apikey: str

    """
    return web.Response(status=200)


async def live_currency_exchange_rate(request: web.Request, apikey, base, target, amount=None) -> web.Response:
    """Live currency exchange rate

    Get the exchange rate between two currencies.

    :param apikey: Authentication key.
    :type apikey: str
    :param base: The source currency.
    :type base: str
    :param target: The target currency.
    :type target: str
    :param amount: optional The amount to convert.
    :type amount: 

    """
    return web.Response(status=200)
