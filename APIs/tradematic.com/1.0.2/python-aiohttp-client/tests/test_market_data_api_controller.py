# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.market import Market
from openapi_server.models.marketdata_symbols_symbolid_histdata_get200_response import MarketdataSymbolsSymbolidHistdataGet200Response


pytestmark = pytest.mark.asyncio

async def test_marketdata_markets_get(client):
    """Test case for marketdata_markets_get

    Get markets list
    """
    headers = { 
        'Accept': 'application/json',
        'Secured': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/marketdata/markets',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_marketdata_markets_marketid_get(client):
    """Test case for marketdata_markets_marketid_get

    Get market by ID
    """
    headers = { 
        'Accept': 'application/json',
        'Secured': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/marketdata/markets/{marketid}'.format(marketid=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_marketdata_symbols_get(client):
    """Test case for marketdata_symbols_get

    Get symbols list
    """
    params = [('marketid', 56),
                    ('filter', 56)]
    headers = { 
        'Accept': 'application/json',
        'Secured': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/marketdata/symbols',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_marketdata_symbols_symbolid_get(client):
    """Test case for marketdata_symbols_symbolid_get

    Get symbol by ID
    """
    headers = { 
        'Accept': 'application/json',
        'Secured': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/marketdata/symbols/{symbolid}'.format(symbolid=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_marketdata_symbols_symbolid_histdata_get(client):
    """Test case for marketdata_symbols_symbolid_histdata_get

    Get historical data for instrument
    """
    params = [('tf', 56),
                    ('from', 56),
                    ('to', 56)]
    headers = { 
        'Accept': 'application/json',
        'Secured': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/marketdata/symbols/{symbolid}/histdata'.format(symbolid=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

