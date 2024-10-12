from typing import List, Dict
from aiohttp import web

from openapi_server.models.input_currency_conversion import InputCurrencyConversion
from openapi_server.models.input_currency_format import InputCurrencyFormat
from openapi_server.models.input_market_index import InputMarketIndex
from openapi_server.models.input_stock_prices import InputStockPrices
from openapi_server.models.output_market_index import OutputMarketIndex
from openapi_server.models.output_number import OutputNumber
from openapi_server.models.output_stock_price import OutputStockPrice
from openapi_server.models.output_string import OutputString
from openapi_server import util


async def convert_currency(request: web.Request, currency_conversion=None) -> web.Response:
    """Currency - Convert currency

    Calculate monetary value in a different currency

    :param currency_conversion: 
    :type currency_conversion: dict | bytes

    """
    currency_conversion = InputCurrencyConversion.from_dict(currency_conversion)
    return web.Response(status=200)


async def format_currency(request: web.Request, currency_format=None) -> web.Response:
    """Currency - Format currency

    Apply currency symbol to a numeric value

    :param currency_format: 
    :type currency_format: dict | bytes

    """
    currency_format = InputCurrencyFormat.from_dict(currency_format)
    return web.Response(status=200)


async def market_index(request: web.Request, market_index=None) -> web.Response:
    """Finance - Market index

    Get current and historical market index information

    :param market_index: 
    :type market_index: dict | bytes

    """
    market_index = InputMarketIndex.from_dict(market_index)
    return web.Response(status=200)


async def stock_prices(request: web.Request, stock_prices=None) -> web.Response:
    """Finance - Stock prices

    Get current and historical stock price information

    :param stock_prices: 
    :type stock_prices: dict | bytes

    """
    stock_prices = InputStockPrices.from_dict(stock_prices)
    return web.Response(status=200)
