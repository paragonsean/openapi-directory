# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.interval_collection_response import IntervalCollectionResponse
from openapi_server.models.rate_response import RateResponse
from openapi_server.models.summary_response import SummaryResponse


pytestmark = pytest.mark.asyncio

async def test_currencies_history_get(client):
    """Test case for currencies_history_get

    Get historical prices for requested currency pairs
    """
    params = [('pairs', 'pairs_example'),
                    ('start', '2013-10-20T19:20:30+01:00'),
                    ('end', '2013-10-20T19:20:30+01:00'),
                    ('interval', 'interval_example'),
                    ('format', 'format_example')]
    headers = { 
        'Accept': 'application/json',
        'token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/Currencies/history',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_currencies_rate_get(client):
    """Test case for currencies_rate_get

    Get latest mid rate for requested currency pairs
    """
    params = [('pairs', 'pairs_example'),
                    ('format', 'format_example')]
    headers = { 
        'Accept': 'application/json',
        'token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/Currencies/rate',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_currencies_summary_get(client):
    """Test case for currencies_summary_get

    Get latest Summary for requested currency pairs
    """
    params = [('pairs', 'pairs_example'),
                    ('format', 'format_example')]
    headers = { 
        'Accept': 'application/json',
        'token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/Currencies/summary',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_currencies_supported_currencies_history_get(client):
    """Test case for currencies_supported_currencies_history_get

    Get list of currency pairs supported by the history endpoint
    """
    params = [('format', 'format_example')]
    headers = { 
        'Accept': 'application/json',
        'token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/Currencies/history/supported',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_currencies_supported_currencies_rate_get(client):
    """Test case for currencies_supported_currencies_rate_get

    Get list of currencies supported by the rate endpoint
    """
    params = [('format', 'format_example')]
    headers = { 
        'Accept': 'application/json',
        'token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/Currencies/rate/supported',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_currencies_supported_currencies_summary_get(client):
    """Test case for currencies_supported_currencies_summary_get

    Get list of currency pairs supported by the Summary endpoint
    """
    params = [('format', 'format_example')]
    headers = { 
        'Accept': 'application/json',
        'token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/Currencies/summary/supported',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

