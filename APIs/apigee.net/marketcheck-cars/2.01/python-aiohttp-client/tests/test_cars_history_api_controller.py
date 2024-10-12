# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.historical_listing import HistoricalListing


pytestmark = pytest.mark.asyncio

async def test_get_car_history(client):
    """Test case for get_car_history

    Get a cars online listing history
    """
    params = [('api_key', 'api_key_example'),
                    ('fields', 'fields_example'),
                    ('page', 3.4),
                    ('include_duplicates', True),
                    ('sort_order', 'sort_order_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/history/car/{vin}'.format(vin='vin_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_history_car_uk_vrm_get(client):
    """Test case for history_car_uk_vrm_get

    Get a cars online listing history
    """
    params = [('api_key', 'api_key_example'),
                    ('page', 3.4),
                    ('include_duplicates', True),
                    ('sort_order', 'sort_order_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/history/car/uk/{vrm}'.format(vrm='vrm_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

