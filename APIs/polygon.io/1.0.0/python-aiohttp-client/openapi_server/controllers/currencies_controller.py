from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.v1_historic_forex_from_to_date_get200_response import V1HistoricForexFromToDateGet200Response
from openapi_server.models.v1_last_currencies_from_to_get200_response import V1LastCurrenciesFromToGet200Response
from openapi_server.models.v1_last_quote_currencies_from_to_get200_response import V1LastQuoteCurrenciesFromToGet200Response
from openapi_server import util


async def v1_currencies_get(request: web.Request, ) -> web.Response:
    """Available Currencies

    Get a list of the currencies that polygon.io streams. 


    """
    return web.Response(status=200)


async def v1_historic_forex_from_to_date_get(request: web.Request, _from, to, _date, offset=None, limit=None) -> web.Response:
    """Historic Forex Ticks

    Get historic ticks for a currency pair. Example for **USD/JPY** the from would be **USD** and to would be **JPY**. The date formatted like **2017-6-22** 

    :param _from: From Symbol of the currency pair
    :type _from: str
    :param to: To Symbol of the currency pair
    :type to: str
    :param _date: Date/Day of the historic ticks to retreive
    :type _date: str
    :param offset: Timestamp offset, used for pagination
    :type offset: int
    :param limit: Limit the size of response, max: 10000
    :type limit: int

    """
    _date = util.deserialize_date(_date)
    return web.Response(status=200)


async def v1_last_currencies_from_to_get(request: web.Request, _from, to) -> web.Response:
    """Last Trade for a Currency Pair

    Get Last Trade Tick for a Currency Pair. 

    :param _from: From Symbol of the pair
    :type _from: str
    :param to: To Symbol of the pair
    :type to: str

    """
    return web.Response(status=200)


async def v1_last_quote_currencies_from_to_get(request: web.Request, _from, to) -> web.Response:
    """Last Quote for a Currency Pair

    Get Last Quote Tick for a Currency Pair. 

    :param _from: From Symbol of the pair
    :type _from: str
    :param to: To Symbol of the pair
    :type to: str

    """
    return web.Response(status=200)
