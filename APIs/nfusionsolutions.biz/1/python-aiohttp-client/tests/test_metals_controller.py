# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.interval_collection_response import IntervalCollectionResponse
from openapi_server.models.summary_response import SummaryResponse


pytestmark = pytest.mark.asyncio

async def test_metals_benchmark_history_get(client):
    """Test case for metals_benchmark_history_get

    Get historical benchmark prices for requested metals
    """
    params = [('metals', 'metals_example'),
                    ('start', '2013-10-20T19:20:30+01:00'),
                    ('end', '2013-10-20T19:20:30+01:00'),
                    ('interval', 'interval_example'),
                    ('historicalfx', True),
                    ('currency', 'currency_example'),
                    ('unitofmeasure', 'unitofmeasure_example'),
                    ('format', 'format_example')]
    headers = { 
        'Accept': 'application/json',
        'token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/Metals/benchmark/history',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_metals_benchmark_summary_get(client):
    """Test case for metals_benchmark_summary_get

    Get latest Benchmark prices for requested metals
    """
    params = [('metals', 'metals_example'),
                    ('currency', 'currency_example'),
                    ('unitofmeasure', 'unitofmeasure_example'),
                    ('format', 'format_example')]
    headers = { 
        'Accept': 'application/json',
        'token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/Metals/benchmark/summary',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_metals_benchmark_supported_metals_get(client):
    """Test case for metals_benchmark_supported_metals_get

    Get list of symbols supported by the benchmark endpoints
    """
    params = [('format', 'format_example')]
    headers = { 
        'Accept': 'application/json',
        'token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/Metals/benchmark/supported',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_metals_spot_annual_historical_performance_get(client):
    """Test case for metals_spot_annual_historical_performance_get

    Get Historical Annual Performance for requested metals
    """
    params = [('metals', 'metals_example'),
                    ('currency', 'currency_example'),
                    ('unitofmeasure', 'unitofmeasure_example'),
                    ('format', 'format_example'),
                    ('years', 56)]
    headers = { 
        'Accept': 'application/json',
        'token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/Metals/spot/performance/annual',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_metals_spot_historical_performance_get(client):
    """Test case for metals_spot_historical_performance_get

    Get Historical Performance for requested metals
    """
    params = [('metals', 'metals_example'),
                    ('currency', 'currency_example'),
                    ('unitofmeasure', 'unitofmeasure_example'),
                    ('format', 'format_example')]
    headers = { 
        'Accept': 'application/json',
        'token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/Metals/spot/performance',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_metals_spot_history_get(client):
    """Test case for metals_spot_history_get

    Get historical Spot prices for requested metals
    """
    params = [('metals', 'metals_example'),
                    ('start', '2013-10-20T19:20:30+01:00'),
                    ('end', '2013-10-20T19:20:30+01:00'),
                    ('interval', 'interval_example'),
                    ('historicalfx', True),
                    ('currency', 'currency_example'),
                    ('unitofmeasure', 'unitofmeasure_example'),
                    ('format', 'format_example')]
    headers = { 
        'Accept': 'application/json',
        'token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/Metals/spot/history',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_metals_spot_ratio_history_get(client):
    """Test case for metals_spot_ratio_history_get

    Get historical Spot Ratio prices for requested metals
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
        path='/api/v1/Metals/spot/ratio/history',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_metals_spot_ratio_summary_get(client):
    """Test case for metals_spot_ratio_summary_get

    Get latest Spot Summary for requested metal ratios
    """
    params = [('pairs', 'pairs_example'),
                    ('format', 'format_example')]
    headers = { 
        'Accept': 'application/json',
        'token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/Metals/spot/ratio/summary',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_metals_spot_summary_get(client):
    """Test case for metals_spot_summary_get

    Get latest Spot Summary for requested metals
    """
    params = [('metals', 'metals_example'),
                    ('currency', 'currency_example'),
                    ('unitofmeasure', 'unitofmeasure_example'),
                    ('format', 'format_example')]
    headers = { 
        'Accept': 'application/json',
        'token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/Metals/spot/summary',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_metals_spot_supported_metals_get(client):
    """Test case for metals_spot_supported_metals_get

    Get list of symbols supported by the spot endpoints
    """
    params = [('format', 'format_example')]
    headers = { 
        'Accept': 'application/json',
        'token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/Metals/spot/supported',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_metals_supported_currencies_metals_get(client):
    """Test case for metals_supported_currencies_metals_get

    Get list of currencies supported by metals endpoints for currency conversion
    """
    params = [('format', 'format_example')]
    headers = { 
        'Accept': 'application/json',
        'token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/Metals/supported/currency',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

