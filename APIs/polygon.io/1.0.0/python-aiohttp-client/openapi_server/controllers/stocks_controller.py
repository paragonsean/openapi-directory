from typing import List, Dict
from aiohttp import web

from openapi_server.models.company import Company
from openapi_server.models.error import Error
from openapi_server.models.v1_historic_agg_size_symbol_date_get200_response import V1HistoricAggSizeSymbolDateGet200Response
from openapi_server.models.v1_historic_quotes_symbol_date_get200_response import V1HistoricQuotesSymbolDateGet200Response
from openapi_server.models.v1_historic_trades_symbol_date_get200_response import V1HistoricTradesSymbolDateGet200Response
from openapi_server.models.v1_last_quote_stocks_symbol_get200_response import V1LastQuoteStocksSymbolGet200Response
from openapi_server.models.v1_last_stocks_symbol_get200_response import V1LastStocksSymbolGet200Response
from openapi_server import util


async def v1_companies_get(request: web.Request, sort=None, perpage=None, page=None) -> web.Response:
    """Available Companies

    Get a list of the traded companies that polygon.io streams. Company includes some details about the company which we hope to add more to soon. 

    :param sort: Which field to sort by. For desc place a &#x60;-&#x60; in front of the field name. eg &#x60;?sort&#x3D;-marketcap&#x60;
    :type sort: str
    :param perpage: How many items to be on each page during pagination
    :type perpage: 
    :param page: Which page of results to return
    :type page: 

    """
    return web.Response(status=200)


async def v1_historic_agg_size_symbol_date_get(request: web.Request, size, symbol, _date, offset=None, limit=None) -> web.Response:
    """Historic Aggregates

    Get historic aggregations for a symbol. 

    :param size: Size of the aggregation. &#x60;second&#x60; or &#x60;minute&#x60;
    :type size: str
    :param symbol: Symbol of the company to retrieve
    :type symbol: str
    :param _date: Date/Day of the historic ticks to retreive
    :type _date: str
    :param offset: Timestamp offset, used for pagination
    :type offset: int
    :param limit: Limit the size of response, max: 10000
    :type limit: int

    """
    _date = util.deserialize_date(_date)
    return web.Response(status=200)


async def v1_historic_quotes_symbol_date_get(request: web.Request, symbol, _date, offset=None, limit=None) -> web.Response:
    """Historic Quotes

    Get historic quotes for a symbol. 

    :param symbol: Symbol of the company to retrieve
    :type symbol: str
    :param _date: Date/Day of the historic ticks to retreive
    :type _date: str
    :param offset: Timestamp offset, used for pagination
    :type offset: int
    :param limit: Limit the size of response, max: 10000
    :type limit: int

    """
    _date = util.deserialize_date(_date)
    return web.Response(status=200)


async def v1_historic_trades_symbol_date_get(request: web.Request, symbol, _date, offset=None, limit=None) -> web.Response:
    """Historic Trades

    Get historic trades for a symbol. 

    :param symbol: Symbol of the company to retrieve
    :type symbol: str
    :param _date: Date/Day of the historic ticks to retreive
    :type _date: str
    :param offset: Timestamp offset, used for pagination
    :type offset: int
    :param limit: Limit the size of response, max: 10000
    :type limit: int

    """
    _date = util.deserialize_date(_date)
    return web.Response(status=200)


async def v1_last_quote_stocks_symbol_get(request: web.Request, symbol) -> web.Response:
    """Last Quote for a Symbol

    Get the last quote tick for a given stock. 

    :param symbol: Symbol of the stock to get
    :type symbol: str

    """
    return web.Response(status=200)


async def v1_last_stocks_symbol_get(request: web.Request, symbol) -> web.Response:
    """Last Trade for a Symbol

    Get the last trade for a given stock. 

    :param symbol: Symbol of the stock to get
    :type symbol: str

    """
    return web.Response(status=200)
