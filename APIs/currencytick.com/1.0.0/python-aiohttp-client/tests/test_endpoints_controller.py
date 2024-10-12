# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.healthcheck200_response import Healthcheck200Response
from openapi_server.models.healthcheck400_response import Healthcheck400Response
from openapi_server.models.historical_exchange_rate200_response import HistoricalExchangeRate200Response


pytestmark = pytest.mark.asyncio

async def test_healthcheck(client):
    """Test case for healthcheck

    Healthcheck
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/healthcheck',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_historical_exchange_rate(client):
    """Test case for historical_exchange_rate

    Historical Exchange Rate
    """
    params = [('apikey', 'YOUR_API_KEY'),
                    ('base', 'USD'),
                    ('target', 'EUR'),
                    ('date', '2023-04-18')]
    headers = { 
        'Accept': 'application/json',
        'default': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/historical',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_of_supported_currencies(client):
    """Test case for list_of_supported_currencies

    List of supported currencies
    """
    params = [('apikey', 'YOUR_API_KEY')]
    headers = { 
        'Accept': 'text/plain',
        'default': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/supported_currencies',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_live_currency_exchange_rate(client):
    """Test case for live_currency_exchange_rate

    Live currency exchange rate
    """
    params = [('apikey', 'YOUR_API_KEY'),
                    ('base', 'USD'),
                    ('target', 'EUR'),
                    ('amount', 1)]
    headers = { 
        'Accept': 'application/json',
        'default': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/live',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

