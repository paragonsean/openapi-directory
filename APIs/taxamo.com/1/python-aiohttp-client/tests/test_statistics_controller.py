# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_daily_settlement_stats_out import GetDailySettlementStatsOut
from openapi_server.models.get_settlement_stats_by_country_out import GetSettlementStatsByCountryOut
from openapi_server.models.get_settlement_stats_by_taxation_type_out import GetSettlementStatsByTaxationTypeOut
from openapi_server.models.get_transactions_stats_by_country_out import GetTransactionsStatsByCountryOut
from openapi_server.models.get_transactions_stats_out import GetTransactionsStatsOut


pytestmark = pytest.mark.asyncio

async def test_get_daily_settlement_stats(client):
    """Test case for get_daily_settlement_stats

    Settlement stats over time
    """
    params = [('interval', 'interval_example'),
                    ('date_from', 'date_from_example'),
                    ('date_to', 'date_to_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/stats/settlement/daily',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_settlement_stats_by_country(client):
    """Test case for get_settlement_stats_by_country

    Settlement by country
    """
    params = [('date_from', 'date_from_example'),
                    ('date_to', 'date_to_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/stats/settlement/by_country',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_settlement_stats_by_taxation_type(client):
    """Test case for get_settlement_stats_by_taxation_type

    Settlement by tax type
    """
    params = [('date_from', 'date_from_example'),
                    ('date_to', 'date_to_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/stats/settlement/by_taxation_type',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_transactions_stats(client):
    """Test case for get_transactions_stats

    Transaction stats
    """
    params = [('date_from', 'date_from_example'),
                    ('date_to', 'date_to_example'),
                    ('interval', 'interval_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/stats/transactions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_transactions_stats_by_country(client):
    """Test case for get_transactions_stats_by_country

    Settlement by country
    """
    params = [('global_currency_code', 'global_currency_code_example'),
                    ('date_from', 'date_from_example'),
                    ('date_to', 'date_to_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/stats/transactions/by_country',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

