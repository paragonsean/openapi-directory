from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.market import Market
from openapi_server.models.marketdata_symbols_symbolid_histdata_get200_response import MarketdataSymbolsSymbolidHistdataGet200Response
from openapi_server import util


async def marketdata_markets_get(request: web.Request, ) -> web.Response:
    """Get markets list

    Get markets list


    """
    return web.Response(status=200)


async def marketdata_markets_marketid_get(request: web.Request, marketid) -> web.Response:
    """Get market by ID

    Get market by ID

    :param marketid: 
    :type marketid: int

    """
    return web.Response(status=200)


async def marketdata_symbols_get(request: web.Request, marketid, filter) -> web.Response:
    """Get symbols list

    Get symbols list

    :param marketid: 
    :type marketid: int
    :param filter: 
    :type filter: int

    """
    return web.Response(status=200)


async def marketdata_symbols_symbolid_get(request: web.Request, symbolid) -> web.Response:
    """Get symbol by ID

    Get symbol by ID

    :param symbolid: 
    :type symbolid: int

    """
    return web.Response(status=200)


async def marketdata_symbols_symbolid_histdata_get(request: web.Request, symbolid, tf, _from, to) -> web.Response:
    """Get historical data for instrument

    Get historical data for instrument

    :param symbolid: 
    :type symbolid: int
    :param tf: 
    :type tf: int
    :param _from: 
    :type _from: int
    :param to: 
    :type to: int

    """
    return web.Response(status=200)
