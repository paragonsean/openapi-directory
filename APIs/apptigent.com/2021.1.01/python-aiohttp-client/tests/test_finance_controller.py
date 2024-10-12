# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.input_currency_conversion import InputCurrencyConversion
from openapi_server.models.input_currency_format import InputCurrencyFormat
from openapi_server.models.input_market_index import InputMarketIndex
from openapi_server.models.input_stock_prices import InputStockPrices
from openapi_server.models.output_market_index import OutputMarketIndex
from openapi_server.models.output_number import OutputNumber
from openapi_server.models.output_stock_price import OutputStockPrice
from openapi_server.models.output_string import OutputString


pytestmark = pytest.mark.asyncio

async def test_convert_currency(client):
    """Test case for convert_currency

    Currency - Convert currency
    """
    currency_conversion = openapi_server.InputCurrencyConversion()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/utilities/ConvertCurrency',
        headers=headers,
        json=currency_conversion,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_format_currency(client):
    """Test case for format_currency

    Currency - Format currency
    """
    currency_format = openapi_server.InputCurrencyFormat()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/utilities/FormatCurrency',
        headers=headers,
        json=currency_format,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_market_index(client):
    """Test case for market_index

    Finance - Market index
    """
    market_index = openapi_server.InputMarketIndex()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/utilities/MarketIndex',
        headers=headers,
        json=market_index,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stock_prices(client):
    """Test case for stock_prices

    Finance - Stock prices
    """
    stock_prices = openapi_server.InputStockPrices()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/utilities/StockPrices',
        headers=headers,
        json=stock_prices,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

