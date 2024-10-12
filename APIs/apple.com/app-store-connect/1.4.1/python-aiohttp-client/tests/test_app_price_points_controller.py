# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.app_price_point_response import AppPricePointResponse
from openapi_server.models.app_price_points_response import AppPricePointsResponse
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.territory_response import TerritoryResponse


pytestmark = pytest.mark.asyncio

async def test_app_price_points_get_collection(client):
    """Test case for app_price_points_get_collection

    
    """
    params = [('filter[priceTier]', ['filter_price_tier_example']),
                    ('filter[territory]', ['filter_territory_example']),
                    ('fields[appPricePoints]', ['fields_app_price_points_example']),
                    ('limit', 56),
                    ('include', ['include_example']),
                    ('fields[territories]', ['fields_territories_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/appPricePoints',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_price_points_get_instance(client):
    """Test case for app_price_points_get_instance

    
    """
    params = [('fields[appPricePoints]', ['fields_app_price_points_example']),
                    ('include', ['include_example']),
                    ('fields[territories]', ['fields_territories_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/appPricePoints/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_price_points_territory_get_to_one_related(client):
    """Test case for app_price_points_territory_get_to_one_related

    
    """
    params = [('fields[territories]', ['fields_territories_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/appPricePoints/{id}/territory'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

