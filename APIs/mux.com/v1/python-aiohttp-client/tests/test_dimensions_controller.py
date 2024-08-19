# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_dimension_values_response import ListDimensionValuesResponse
from openapi_server.models.list_dimensions_response import ListDimensionsResponse


pytestmark = pytest.mark.asyncio

async def test_list_dimension_values(client):
    """Test case for list_dimension_values

    Lists the values for a specific dimension
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
        path='/data/v1/dimensions/{dimension_id}'.format(dimension_id='abcd1234'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_dimensions(client):
    """Test case for list_dimensions

    List Dimensions
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/data/v1/dimensions',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

