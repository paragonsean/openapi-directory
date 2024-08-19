# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_filter_values_response import ListFilterValuesResponse
from openapi_server.models.list_filters_response import ListFiltersResponse


pytestmark = pytest.mark.asyncio

async def test_list_filter_values(client):
    """Test case for list_filter_values

    Lists values for a specific filter
    """
    params = [('limit', 25),
                    ('page', 1),
                    ('filters[]', ['filters_example']),
                    ('timeframe[]', ['timeframe_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/data/v1/filters/{filter_id}'.format(filter_id='abcd1234'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_filters(client):
    """Test case for list_filters

    List Filters
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/data/v1/filters',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

