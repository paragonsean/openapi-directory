# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_correlation(client):
    """Test case for correlation

    Correlation
    """
    params = [('tokens', '3375, 3306'),
                    ('limit', '1000')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v1/correlation',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_indices(client):
    """Test case for indices

    Indices
    """
    params = [('exchanges', 'binance'),
                    ('timeHorizon', 'daily'),
                    ('lowCap', 'true'),
                    ('startDate', '2023-01-10'),
                    ('endDate', '2023-01-11'),
                    ('limit', '1000')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v1/indices',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_investor_grades(client):
    """Test case for investor_grades

    Investor Grades
    """
    params = [('tokens', '3375, 3306'),
                    ('startDate', '2023-01-10'),
                    ('endDate', '2023-01-11'),
                    ('limit', '1000')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v1/investor-grades',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_market_indicator(client):
    """Test case for market_indicator

    Market Indicator
    """
    params = [('startDate', '2023-01-10'),
                    ('endDate', '2023-01-11'),
                    ('limit', '1000')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v1/market-indicator',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_price(client):
    """Test case for price

    Price
    """
    params = [('tokens', '3375, 3306'),
                    ('startDate', '2023-01-10'),
                    ('endDate', '2023-01-11'),
                    ('limit', '1000'),
                    ('page', '1')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v1/price',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_price_prediction(client):
    """Test case for price_prediction

    Price Prediction
    """
    params = [('tokens', '3375, 3306'),
                    ('date', '2023-02-01'),
                    ('limit', '1000')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v1/price-prediction',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_quantmetrics_tier1(client):
    """Test case for quantmetrics_tier1

    Quantmetrics Tier 1
    """
    params = [('tokens', '3375, 3306'),
                    ('date', '2023-02-01'),
                    ('limit', '1000')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v1/quantmetrics-tier-1',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_quantmetrics_tier2(client):
    """Test case for quantmetrics_tier2

    Quantmetrics Tier 2
    """
    params = [('tokens', '3375, 3306'),
                    ('date', '2023-02-01'),
                    ('limit', '1000')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v1/quantmetrics-tier-2',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_resistance_support(client):
    """Test case for resistance_support

    Resistance & Support
    """
    params = [('tokens', '3375, 3306'),
                    ('startDate', '2023-01-10'),
                    ('endDate', '2023-01-11'),
                    ('limit', '1000')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v1/resistance-support',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_scenario_analysis(client):
    """Test case for scenario_analysis

    Scenario Analysis
    """
    params = [('tokens', '3375, 3306'),
                    ('limit', '1000')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v1/scenario-analysis',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sentiments(client):
    """Test case for sentiments

    Sentiments
    """
    params = [('tokens', '3375, 3306'),
                    ('startDate', '2023-01-10'),
                    ('endDate', '2023-01-11'),
                    ('limit', '1000')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v1/sentiments',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tokens(client):
    """Test case for tokens

    Tokens
    """
    params = [('token_ids', '3375, 3306'),
                    ('token_names', 'Hivemapper, Sei_Network, Layer_Zero, Lyra Huobi'),
                    ('token_symbols', 'bds, bds, btc')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v1/tokens',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_trader_grades(client):
    """Test case for trader_grades

    Trader Grades
    """
    params = [('tokens', '3375, 3306'),
                    ('startDate', '2023-01-10'),
                    ('endDate', '2023-01-11'),
                    ('limit', '1000')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v1/trader-grades',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_trading_indicator(client):
    """Test case for trading_indicator

    Trading Indicator
    """
    params = [('tokens', '3375, 3306'),
                    ('limit', '1000')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v1/trading-indicator',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

