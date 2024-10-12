# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.v1_historic_forex_from_to_date_get200_response import V1HistoricForexFromToDateGet200Response
from openapi_server.models.v1_last_currencies_from_to_get200_response import V1LastCurrenciesFromToGet200Response
from openapi_server.models.v1_last_quote_currencies_from_to_get200_response import V1LastQuoteCurrenciesFromToGet200Response


pytestmark = pytest.mark.asyncio

async def test_v1_currencies_get(client):
    """Test case for v1_currencies_get

    Available Currencies
    """
    headers = { 
        'Accept': 'application/json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/currencies',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v1_historic_forex_from_to_date_get(client):
    """Test case for v1_historic_forex_from_to_date_get

    Historic Forex Ticks
    """
    params = [('offset', 56),
                    ('limit', 100)]
    headers = { 
        'Accept': 'application/json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/historic/forex/{_from}/{to}/{_date}'.format(_from='_from_example', to='to_example', _date='2013-10-20'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v1_last_currencies_from_to_get(client):
    """Test case for v1_last_currencies_from_to_get

    Last Trade for a Currency Pair
    """
    headers = { 
        'Accept': 'application/json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/last/currencies/{_from}/{to}'.format(_from='_from_example', to='to_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v1_last_quote_currencies_from_to_get(client):
    """Test case for v1_last_quote_currencies_from_to_get

    Last Quote for a Currency Pair
    """
    headers = { 
        'Accept': 'application/json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/last_quote/currencies/{_from}/{to}'.format(_from='_from_example', to='to_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

