# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.company import Company
from openapi_server.models.error import Error
from openapi_server.models.v1_historic_agg_size_symbol_date_get200_response import V1HistoricAggSizeSymbolDateGet200Response
from openapi_server.models.v1_historic_quotes_symbol_date_get200_response import V1HistoricQuotesSymbolDateGet200Response
from openapi_server.models.v1_historic_trades_symbol_date_get200_response import V1HistoricTradesSymbolDateGet200Response
from openapi_server.models.v1_last_quote_stocks_symbol_get200_response import V1LastQuoteStocksSymbolGet200Response
from openapi_server.models.v1_last_stocks_symbol_get200_response import V1LastStocksSymbolGet200Response


pytestmark = pytest.mark.asyncio

async def test_v1_companies_get(client):
    """Test case for v1_companies_get

    Available Companies
    """
    params = [('sort', 'sort_example'),
                    ('perpage', 3.4),
                    ('page', 1.0)]
    headers = { 
        'Accept': 'application/json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/companies',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v1_historic_agg_size_symbol_date_get(client):
    """Test case for v1_historic_agg_size_symbol_date_get

    Historic Aggregates
    """
    params = [('offset', 56),
                    ('limit', 100)]
    headers = { 
        'Accept': 'application/json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/historic/agg/{size}/{symbol}/{_date}'.format(size='size_example', symbol='symbol_example', _date='2013-10-20'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v1_historic_quotes_symbol_date_get(client):
    """Test case for v1_historic_quotes_symbol_date_get

    Historic Quotes
    """
    params = [('offset', 56),
                    ('limit', 100)]
    headers = { 
        'Accept': 'application/json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/historic/quotes/{symbol}/{_date}'.format(symbol='symbol_example', _date='2013-10-20'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v1_historic_trades_symbol_date_get(client):
    """Test case for v1_historic_trades_symbol_date_get

    Historic Trades
    """
    params = [('offset', 56),
                    ('limit', 100)]
    headers = { 
        'Accept': 'application/json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/historic/trades/{symbol}/{_date}'.format(symbol='symbol_example', _date='2013-10-20'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v1_last_quote_stocks_symbol_get(client):
    """Test case for v1_last_quote_stocks_symbol_get

    Last Quote for a Symbol
    """
    headers = { 
        'Accept': 'application/json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/last_quote/stocks/{symbol}'.format(symbol='symbol_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v1_last_stocks_symbol_get(client):
    """Test case for v1_last_stocks_symbol_get

    Last Trade for a Symbol
    """
    headers = { 
        'Accept': 'application/json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/last/stocks/{symbol}'.format(symbol='symbol_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

