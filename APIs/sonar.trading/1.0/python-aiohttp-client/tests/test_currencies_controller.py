# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_convert_get(client):
    """Test case for convert_get

    Convert a currency amount to multiple other currencies
    """
    params = [('from', '_from_example'),
                    ('to', 'to_example'),
                    ('amount', 'amount_example'),
                    ('decimal_places', 'decimal_places_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v1/convert',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_country_currencies_get(client):
    """Test case for country_currencies_get

    Return a list of all currencies of countries, available via service
    """
    params = [('language', 'language_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v1/country/currencies',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_digital_currencies_get(client):
    """Test case for digital_currencies_get

    Return a list of all digital currencies, available via service
    """
    params = [('language', 'language_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v1/digital/currencies',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_history_get(client):
    """Test case for history_get

    Return a historic rate for a currencies
    """
    params = [('from', '_from_example'),
                    ('to', 'to_example'),
                    ('date', '_date_example'),
                    ('amount', 'amount_example'),
                    ('decimal_places', 'decimal_places_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v1/history',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

